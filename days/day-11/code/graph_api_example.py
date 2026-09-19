"""Day 11 - a LangGraph graph behind an API (companion to notes.md, Section 2).

A server can't run inside notebook cells, so this lives as a plain script.

Run it (the --factory flag tells uvicorn to call create_app() to build the app):
    uvicorn graph_api_example:create_app --factory --reload

Try it (same thread_id twice -> the second reply remembers the first message):
    curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" \
         -d "{\"thread_id\": \"raj-1\", \"message\": \"hi, I like tea\"}"

No API key needed: the chatbot node is a simple function. To make it a real assistant, replace it
with a node that calls a model (see Day 05 / Day 09).
"""

import os
import sqlite3
from typing import Annotated, TypedDict

from fastapi import FastAPI
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from pydantic import BaseModel


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: ChatState) -> dict:
    said = [m.content for m in state["messages"] if m.type == "human"]
    return {"messages": [AIMessage(content=f"You have said {len(said)} thing(s) so far: {said}")]}


class ChatRequest(BaseModel):
    thread_id: str  # which conversation this message belongs to
    message: str


def create_app(db_path: str | None = None) -> FastAPI:
    # Memory is saved in this file, so it survives a server restart.
    db_path = db_path or os.getenv("CHAT_DB_PATH", "chat_memory.sqlite")

    builder = StateGraph(ChatState)
    builder.add_node("chatbot", chatbot)
    builder.add_edge(START, "chatbot")
    builder.add_edge("chatbot", END)

    connection = sqlite3.connect(db_path, check_same_thread=False)
    graph = builder.compile(checkpointer=SqliteSaver(connection))

    app = FastAPI(title="Day 11 graph API")

    @app.post("/chat")
    def chat(request: ChatRequest) -> dict:
        config = {"configurable": {"thread_id": request.thread_id}}
        result = graph.invoke({"messages": [HumanMessage(request.message)]}, config)
        return {"thread_id": request.thread_id, "reply": result["messages"][-1].content}

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok"}

    return app
