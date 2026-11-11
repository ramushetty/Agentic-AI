# Deep Agents is built on LangChain agents, which you can also use directly.
# Use LangChain (create_agent) for a highly customizable harness, easily tailored to your use case and data.
# Use LangGraph, our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows.
# Use LangSmith to trace, debug, and evaluate agents built with any of these frameworks.
# 🔗 LangChain
# 🕸️ LangGraph
# 🤖 OpenAI Agents SDK
# 🏗️ Google ADK
# ⚡ AWS Strands
# 👥 CrewAI
# 🦙 LlamaIndex
# 🔄 n8n
# 🌊 LangFlow

# Langchain has multiple offerings(Lang Family) - langChain, langGraph, Deep agents, langSmith 

# LangFuse is not part of Lang family

# analogy
# LangGraph (foundation) --> LangChain(Rooms) --> Deep Agents(Furnished) --> LangSmith(Watches all)

# langGraph powers langChain
# Deep Agents built on langChain


# Models are just raw power 
# Agent = Model + Harness
# The harness is what turns raw power into something that can actually race

# An agent is a model calling tools in a loop until the task is done

# Bare model + system prompt + tools + middleware

# oct 2022 when langChain launced  (prompt | input) chain
# dec 2022 ReAct - reason and act 
# Feb 2024 LangGraph released - low level orchestration (HITL,short term memory,streaming,durable)
# Oct 2024 langGraph became the preferred way to build anything , most old langChain chains deprecated
# Oct 2025 LangChain V1.0 released one agent abstraction, build on langGraph
# Mar 2026 Deep Agents released , batteries included (everything is ready)(less level of control)(subagent spwaning)


# core components

# model, skills, memory, subagents,context,tools,system prompt



# Models

# models generate text,translate,summarize apart from this it can support
# tool calling
# Structured output
# Multimodality
# Reasoning
# https://docs.langchain.com/oss/python/langchain/models


# open source -  weights/parameters know to public and we can host that model in your own infra 
# closed source - weights or parameters are private we need to pay and use can not host them

# LangChain provides one consistent way to talk to a model, no matter which company built it. 
# You call init_chat_model() with a string in the format "provider:model", and everything after 
# that — invoking it, streaming it, binding tools to it — works identically regardless of the provider.

# The string before the colon is the PROVIDER. The string after is the specific MODEL.
# openai_model = init_chat_model("openai:gpt-5-mini")

# Messages: System, Human, AI, and Tool

# You could, in theory, send a model one long string containing your instructions and the user's question mixed together. This is a bad idea, because the model has no reliable way to tell which part of that string is an instruction and which part is what the user actually said.

# The fix is a message list — a sequence of objects, where each one is explicitly labeled with who "said" it:
# SystemMessage — instructions for how the model should behave. The model treats this differently from user input; it's the "director's note," not something spoken in the scene.
# HumanMessage — what the user actually said or asked.
# AIMessage — what the model said in a previous turn (we cover this object in depth below, it's the richest of the four).
# ToolMessage — the result of a tool call, sent back to the model so it can continue reasoning with that new information 

