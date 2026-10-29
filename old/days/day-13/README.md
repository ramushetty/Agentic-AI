# Day 13 — Project 2: Multi-Agent Refund Desk (Days 12 + 13 combined)

**Module:** Project 2 (build)

I built the whole project in one day, so this day covers both the Day 12 and Day 13 objectives.

## Objectives
- [x] Implement supervisor-to-worker orchestration with retry mechanisms *(from Day 12)*
- [x] Integrate human approval workflows along with audit logging *(from Day 12)*
- [x] Enable governed tool usage using allowlists *(from Day 12)*
- [x] Finish and harden the supervisor-worker system
- [x] Write up learnings: what broke, what patterns held up

## Notes
Full write-up, with the 30-second interview pitch and 11 interview questions: [notes.md](notes.md)

## Project
The code lives in [projects/02-multi-agent-collaboration/](../../projects/02-multi-agent-collaboration/README.md):
a customer refund desk with a supervisor, five workers, an allowlist gateway, a human approval pause, an
audit log, and optional Gemini. It has 17 tests and a 6-ticket demo, and runs without an API key.

## Resources
<!-- Docs, articles, videos you used today -->
- [LangGraph: Human-in-the-loop / interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [LangGraph: Persistence (checkpointers)](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph: Multi-agent overview](https://docs.langchain.com/oss/python/langchain/multi-agent)
- [LangChain: Google Gemini integration](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai)

## Key Learnings
<!-- Write this in your own words after studying/building. This is the part that goes public. -->

Reflection prompts (answer in your own words, after reading notes.md):
1. Which rule in this project would be *unsafe* if it lived only in the prompt? Which would be fine there?
2. Try explaining the 30-second pitch to a friend. Where did you get stuck? That is where to study more.
3. Pick a different domain (IT incidents, expense approvals, hiring). What would the workers, the allowlist,
   and the human approval gate be?

## Notes / Code
- [notes.md](notes.md) — the lesson and the interview Q&A
- [projects/02-multi-agent-collaboration/](../../projects/02-multi-agent-collaboration/README.md) — the code

## Tomorrow
<!-- One line: what's next -->
Day 14 — Agentic RAG: adaptive retrieval.
