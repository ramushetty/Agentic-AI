# Agents



# An agent is a model calling tools in a loop until a given task is complete.

# A harness is everything around that loop: the prompt, the tools, and any middleware that shapes the model’s behavior.

# Agent = Model + Harness

from langchain.agents import create_agent

agent = create_agent(model="openai:gpt-6.1-sol", tools=tools)


# https://docs.langchain.com/oss/python/langchain/agents