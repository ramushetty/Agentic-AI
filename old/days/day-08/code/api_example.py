"""Day 08 — deploying a pipeline as an API service (companion to notes.md Section 3).

FastAPI apps run as a server, not as notebook cells, so this lives as a plain script.

Run it with:
    uvicorn api_example:app --reload

Then try it:
    curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" \
         -d "{\"question\": \"How do I get a refund?\"}"

Needs an OPENAI_API_KEY (or ANTHROPIC_API_KEY) in a .env file up the directory tree to actually answer;
without one, the endpoint returns a clear error instead of crashing.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Day 08 example API")


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    model_used: str


def _get_model():
    """Build a chat model from whichever API key is available. Returns None if none is set."""
    if os.getenv("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model="gpt-4o-mini", temperature=0), "gpt-4o-mini"
    if os.getenv("ANTHROPIC_API_KEY"):
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(model="claude-3-5-haiku-latest", temperature=0), "claude-3-5-haiku-latest"
    return None, None


@app.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest) -> AskResponse:
    """Schema-validated in (AskRequest) and out (AskResponse) -- Day 08 Section 1, applied to a whole API."""
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="question cannot be empty")

    model, model_name = _get_model()
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="No API key configured (set OPENAI_API_KEY or ANTHROPIC_API_KEY in .env)",
        )

    response = await model.ainvoke(request.question)
    return AskResponse(answer=response.content, model_used=model_name)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
