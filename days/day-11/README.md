# Day 11 — Agent Memory & Deployment

**Module:** Module 5

## Objectives
- [ ] Manage memory using short-term and long-term storage
- [ ] Deploy graph-based workflows
- [ ] Orchestrate reliable multi-step systems

## Notes
Full write-up: [notes.md](notes.md)

## Resources
<!-- Docs, articles, videos you used today -->
- [LangGraph: Memory overview](https://docs.langchain.com/oss/python/concepts/memory)
- [LangGraph: Persistence (checkpointers)](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph: Stores](https://docs.langchain.com/oss/python/langgraph/stores)
- [LangGraph: Run a local server (`langgraph dev`)](https://docs.langchain.com/oss/python/langgraph/local-server)

## Key Learnings
<!-- Write this in your own words after studying/building. This is the part that goes public. -->

Reflection prompts (answer in your own words, after reading notes.md):
1. Pick a chatbot you use. Which things does it remember within one chat, and which things would you want
   it to remember across chats? Which of the two needs a store instead of a checkpointer?
2. Why does putting the memory in a database (instead of the API server) let you run 10 copies of the
   server without losing conversations?
3. Name one step in a real workflow that would be dangerous to run twice. How would you make it safe to
   repeat?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson, and
[code/day11_memory_deploy_reliability.ipynb](code/day11_memory_deploy_reliability.ipynb) for a hands-on
notebook in 7 small steps (short-term memory, long-term memory, saving to a SQLite file, calling a
FastAPI graph, retry, step cap, and resume after a crash — no API key needed).

The API used in step 4 is in [code/graph_api_example.py](code/graph_api_example.py). A server can't run
inside a notebook cell, so to try it yourself from the `code/` folder:
```
uvicorn graph_api_example:create_app --factory --reload
```

## Tomorrow
<!-- One line: what's next -->
Day 13 — Project 2: build a multi-agent collaboration system (Days 12 and 13 combined).
