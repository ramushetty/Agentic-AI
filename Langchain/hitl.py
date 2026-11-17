# The Human-in-the-Loop (HITL) middleware lets you add human oversight to agent tool calls. 
# When a model proposes an action that might require review—for example, writing to a file or 
# executing SQL—the middleware can pause
# execution and wait for a decision

# If intervention is needed, the middleware issues an interrupt that halts execution. 
# The graph state is saved using LangGraph’s persistence layer, so execution can pause safely and resume later.

# Decision Type	Description	Example Use Case
# ✅ approve	Execute the tool with the original arguments as proposed by the agent.	Send an email draft exactly as written
# ✏️ edit	Modify the tool arguments before execution.	Change the recipient before sending an email
# ❌ reject	Skip executing this tool call entirely and return rejection feedback to the agent.	Deny file deletion and explain why
# 💬 respond	Return the human’s message directly as a synthetic tool result, skipping execution, for “ask user” style tools.	Answer an "ask_user" prompt with a direct reply


from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware 
from langgraph.checkpoint.memory import InMemorySaver 


agent = create_agent(
    model="gpt-6.1-sol",
    tools=[write_file, execute_sql, read_data],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file": True,  # All decisions (approve, edit, reject, respond) allowed
                "execute_sql": {"allowed_decisions": ["approve", "reject"]},  # No editing allowed
                "read_data": False, # Safe operation, no approval needed
            },
            # Prefix for interrupt messages - combined with tool name and args to form the full message
            # e.g., "Tool execution pending approval: execute_sql with query='DELETE FROM...'"
            # Individual tools can override this by specifying a "description" in their interrupt config
            description_prefix="Tool execution pending approval",
        ),
    ],
    # Human-in-the-loop requires checkpointing to handle interrupts.
    # In production, use a persistent checkpointer like AsyncPostgresSaver or MongoDBSaver.
    checkpointer=InMemorySaver(),
)



# we use command for resuming the interrupt 
# Resume with approval decision
# agent.invoke(
#     Command(
#         resume={"decisions": [{"type": "approve"}]}  # or "reject"
#     ),

# Tool_name : True means any option user can select from 4 options
#  