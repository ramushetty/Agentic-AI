# prebuilt 


# custom 


# Middleware provides a way to more tightly control what happens inside the agent. Middleware is useful for the following:
# Tracking agent behavior with logging, analytics, and debugging.
# Transforming prompts, tool selection, and output formatting.
# Adding retries, fallbacks, and early termination logic.
# Applying rate limits, guardrails, and PII detection.

from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware, HumanInTheLoopMiddleware

agent = create_agent(
    model="gpt-6.1-sol",
    tools=[...],
    middleware=[
        SummarizationMiddleware(...),
        HumanInTheLoopMiddleware(...)
    ],
)



# The agent loop
# The core agent loop involves calling a model, letting it choose tools to execute, and 
# then finishing when it calls no more tools:

# request --> before_Agent --> before model --> wrap_model_call --> model_Call --> after_model --> wrap_tool_Call --> tool_execution --> after_agent --> result


# prebuilt - https://docs.langchain.com/oss/python/langchain/middleware/built-in

# custom 

# Node-style hooks run at specific execution points:
# Hook	         When it runs
# before_agent	Before agent starts (once per invocation)
# before_model	Before each model call
# after_model	After each model response
# after_agent	After agent completes (once per invocation)


# Wrap-style hooks run around each call, giving you control over execution:
# Hook	           When it runs
# wrap_model_call	Around each model call
# wrap_tool_call	Around each tool call


