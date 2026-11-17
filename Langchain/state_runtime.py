# NovaBank agent
# State — What is happening in this conversation?
# - User messages
# - Assistant responses
# - Tool calls and results
# - Conversation history
# Runtime Context — What information is available for this run?
# - Account tier
# - Customer ID
# - Permissions
# - Database/service dependencies
# The simplest way to remember:
# - State = What has happened?
# - Runtime = What information and resources are available while executing?

# What is State?
# State is the agent's working data.



# Question	     State	                 Runtime Context
# What is it?	Agent's working data	Per-run application context



# Hi, my name is Ramu.
# My account number is NB-12345678.
# Please check my balance.

# {
#     "messages": [
#         HumanMessage(content="Hi, my name is Ramu."),
#         AIMessage(content="Hello Ramu!"),
#         HumanMessage(content="Please check my balance.")
#     ]
# }

# State can also contain custom fields.

from typing import TypedDict
from langchain.messages import AnyMessage

class BankState(TypedDict):
    messages: list[AnyMessage]
    account_id: str
    balance: float


# {
#     "messages": [...],
#     "account_id": "NB-12345678",
#     "balance": 75000.0
# }

# You can access this information inside a tool using runtime.state.

from langchain.tools import tool, ToolRuntime

@tool
def get_customer_details(runtime: ToolRuntime[BankContext]) -> str:
    """Get customer details from agent state."""

    account_id = runtime.state["account_id"]

    return f"Checking account: {account_id}"

# What is Runtime Context?
# Runtime context is information that your application provides when invoking the agent.

# For example, your backend already knows that Ramu is a premium customer.


from dataclasses import dataclass

@dataclass
class BankContext:
    customer_id: str
    account_tier: str

response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    },
    context=BankContext(
        customer_id="CUST123",
        account_tier="premium"
    )
)

@tool
def greet_customer(runtime: ToolRuntime[BankContext]) -> str:
    """Greet customer based on account tier."""

    tier = runtime.context.account_tier

    if tier == "premium":
        return "Welcome to NovaBank Premium!"

    return "Welcome to NovaBank Standard!"





from typing import TypedDict
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.checkpoint.memory import InMemorySaver

# STATE: Agent's working data
class BankState(TypedDict):
    account_id: str

# RUNTIME CONTEXT: Application-provided information
@dataclass
class BankContext:
    account_tier: str

# Tool accesses BOTH
@tool
def get_bank_info(runtime: ToolRuntime[BankContext]) -> str:
    """Get bank account information."""

    # Read from STATE
    account_id = runtime.state["account_id"]

    # Read from RUNTIME CONTEXT
    tier = runtime.context.account_tier

    return (
        f"Account: {account_id}. "
        f"Customer tier: {tier}."
    )

# Create agent
agent = create_agent(
    model="openai:gpt-4.1-mini",
    tools=[get_bank_info],
    state_schema=BankState,
    context_schema=BankContext,
    checkpointer=InMemorySaver(),
)

# Invoke
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Tell me my account information."
            }
        ],
        "account_id": "NB-12345678",
    },
    config={
        "configurable": {
            "thread_id": "customer-123"
        }
    },
    context=BankContext(
        account_tier="premium"
    )
)

print(response["messages"][-1].content)