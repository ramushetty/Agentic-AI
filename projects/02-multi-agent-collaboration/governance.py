"""Governance: who may call which tool (allowlist) and a record of everything that happened (audit log).

Every tool call in the system goes through call_tool(). Workers never call tools directly.
The rules live in CODE, not in a prompt, so a confused or tricked LLM cannot talk its way past them.
"""

import json
from datetime import datetime, timezone

from tools import TOOLS

# Each worker gets the smallest set of tools it needs. Anything not listed is blocked.
ALLOWLIST = {
    "lookup_worker": {"get_order"},
    "policy_worker": {"check_refund_policy"},
    "refund_worker": {"issue_refund"},
}


class AuditLog:
    """An append-only file with one JSON line per event: who did what, when, on which ticket."""

    def __init__(self, path):
        self.path = path

    def write(self, ticket_id, actor, action, **details):
        event = {
            "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "ticket": ticket_id,
            "actor": actor,
            "action": action,
            "details": details,
        }
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(json.dumps(event) + "\n")

    def read(self, ticket_id=None):
        try:
            with open(self.path, encoding="utf-8") as file:
                events = [json.loads(line) for line in file]
        except FileNotFoundError:
            return []
        if ticket_id is None:
            return events
        return [event for event in events if event["ticket"] == ticket_id]


def call_tool(audit, ticket_id, worker, tool_name, **args):
    """Run a tool for a worker: check the allowlist, log the call, log the result or the error."""
    if tool_name not in ALLOWLIST.get(worker, set()):
        audit.write(ticket_id, worker, "tool_blocked", tool=tool_name, args=args)
        raise PermissionError(f"{worker} is not allowed to use {tool_name}")

    audit.write(ticket_id, worker, "tool_call", tool=tool_name, args=args)
    try:
        result = TOOLS[tool_name](**args)
    except Exception as error:
        audit.write(ticket_id, worker, "tool_error", tool=tool_name, error=repr(error))
        raise
    audit.write(ticket_id, worker, "tool_result", tool=tool_name, result=result)
    return result
