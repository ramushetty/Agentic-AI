"""The refund desk as a LangGraph: one supervisor, four workers, and a human approval gate.

    START -> supervisor -> lookup_worker  --+
                 ^      -> policy_worker  --+
                 |      -> human_approval --+--> back to supervisor
                 |      -> refund_worker  --+
                 |      -> reply_worker -> END
                 +------------------------+

After every worker the graph returns to the supervisor, which looks at what is known so far
and picks the next step. The rules for "what is allowed next" live in next_step_for().
"""

from typing import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

from brain import classify_intent, draft_reply
from governance import call_tool

MAX_STEPS = 8  # safety cap: a supervisor that keeps looping is sent to the reply step


class DeskState(TypedDict, total=False):
    ticket_id: str
    request: str      # what the customer wrote
    order_id: str
    intent: str       # "refund" or "order_status"
    order: dict
    policy: dict
    approval: str     # "approved" or "rejected", set by the human
    approver: str
    refund: dict
    next_step: str
    steps: int
    reply: str


def next_step_for(state):
    """The rulebook. Given what we know so far, which single step is allowed next?"""
    if state.get("steps", 0) >= MAX_STEPS:
        return "reply_worker"
    if "order" not in state:
        return "lookup_worker"
    if not state["order"]["found"]:
        return "reply_worker"
    if state["intent"] == "order_status":
        return "reply_worker"
    if "policy" not in state:
        return "policy_worker"
    policy = state["policy"]
    if not policy["eligible"]:
        return "reply_worker"
    if policy["needs_approval"] and "approval" not in state:
        return "human_approval"
    if state.get("approval") == "rejected":
        return "reply_worker"
    if "refund" not in state:
        return "refund_worker"
    return "reply_worker"


def build_graph(audit, checkpointer=None, llm=None):
    """Wire everything together. `audit` is the audit log, `llm` is Gemini (or None for the fallbacks)."""

    def supervisor(state):
        ticket = state["ticket_id"]
        updates = {"steps": state.get("steps", 0) + 1}
        if "intent" not in state:
            intent, decided_by = classify_intent(state["request"], llm)
            updates["intent"] = intent
            audit.write(ticket, "supervisor", "intent_classified", intent=intent, decided_by=decided_by)
        step = next_step_for({**state, **updates})
        updates["next_step"] = step
        audit.write(ticket, "supervisor", "route", next_step=step)
        if step == "human_approval":
            audit.write(ticket, "supervisor", "approval_requested", amount=state["order"]["amount"])
        return updates

    def lookup_worker(state):
        order = call_tool(audit, state["ticket_id"], "lookup_worker", "get_order", order_id=state["order_id"])
        return {"order": order}

    def policy_worker(state):
        policy = call_tool(audit, state["ticket_id"], "policy_worker", "check_refund_policy", order=state["order"])
        return {"policy": policy}

    def human_approval(state):
        # The graph pauses BEFORE this node. When a person has decided, we only record it.
        if "approval" in state:
            audit.write(state["ticket_id"], state["approver"], "human_decision", decision=state["approval"])
        return {}

    def refund_worker(state):
        approver = state.get("approver") if state.get("approval") == "approved" else None
        refund = call_tool(
            audit, state["ticket_id"], "refund_worker", "issue_refund",
            order_id=state["order_id"], amount=state["order"]["amount"], approved_by=approver,
        )
        return {"refund": refund}

    def reply_worker(state):
        order = state.get("order", {"found": False})
        facts = {
            "order_id": state["order_id"],
            "order_found": order["found"],
            "intent": state["intent"],
            "item": order.get("item"),
            "amount": order.get("amount"),
            "days_since_delivery": order.get("days_since_delivery"),
            "refunded": "refund" in state,
            "approval": state.get("approval"),
            "policy_reason": state.get("policy", {}).get("reason", "we could not finish checking this request"),
        }
        reply, written_by = draft_reply(facts, llm)
        audit.write(state["ticket_id"], "reply_worker", "reply_drafted", written_by=written_by)
        return {"reply": reply}

    # Workers that call flaky services get automatic retries. Only timeouts are retried:
    # a PermissionError (blocked tool) must fail loudly, not be retried.
    retry = RetryPolicy(max_attempts=4, initial_interval=0.1, retry_on=TimeoutError)

    builder = StateGraph(DeskState)
    builder.add_node("supervisor", supervisor)
    builder.add_node("lookup_worker", lookup_worker, retry_policy=retry)
    builder.add_node("policy_worker", policy_worker, retry_policy=retry)
    builder.add_node("human_approval", human_approval)
    builder.add_node("refund_worker", refund_worker, retry_policy=retry)  # safe to retry: the tool is idempotent
    builder.add_node("reply_worker", reply_worker)

    builder.add_edge(START, "supervisor")
    builder.add_conditional_edges("supervisor", lambda state: state["next_step"])
    for worker in ["lookup_worker", "policy_worker", "human_approval", "refund_worker"]:
        builder.add_edge(worker, "supervisor")
    builder.add_edge("reply_worker", END)

    return builder.compile(
        checkpointer=checkpointer or MemorySaver(),
        interrupt_before=["human_approval"],
    )


# ---- three small helpers the demo, the tests and (later) an API would use -----------------------

def _config(ticket_id):
    return {"configurable": {"thread_id": ticket_id}, "recursion_limit": 25}


def open_ticket(graph, ticket_id, request, order_id):
    """Start a ticket. Returns the saved state; if a human is needed it is paused (snapshot.next)."""
    graph.invoke({"ticket_id": ticket_id, "request": request, "order_id": order_id}, _config(ticket_id))
    return graph.get_state(_config(ticket_id))


def waiting_for_human(snapshot):
    return snapshot.next == ("human_approval",)


def resolve_approval(graph, ticket_id, approve, approver):
    """A human decides. Save the decision into the paused state, then let the graph continue."""
    decision = "approved" if approve else "rejected"
    graph.update_state(_config(ticket_id), {"approval": decision, "approver": approver})
    graph.invoke(None, _config(ticket_id))
    return graph.get_state(_config(ticket_id))
