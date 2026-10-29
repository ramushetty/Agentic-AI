# Day 09 — LangGraph Fundamentals & State

**Module:** Module 5

## Objectives
- [ ] Understand LangGraph fundamentals
- [ ] Define state schemas and reducers

## Notes
Full write-up: [notes.md](notes.md)

## Resources
<!-- Docs, articles, videos you used today -->
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)

## Key Learnings
<!-- Write this in your own words after studying/building. This is the part that goes public. -->

Reflection prompts (answer in your own words, after reading notes.md):
1. Sketch a graph (nodes + edges) for a task of your own choosing that needs at least one loop.
2. Design a state schema for that graph, and say which fields need a custom reducer and why.
3. What would go wrong, concretely, if you forgot to add an append reducer to a message-history field?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson, and
[code/day09_langgraph_fundamentals.ipynb](code/day09_langgraph_fundamentals.ipynb) for a hands-on
notebook (a real 2-node graph, run end to end, with both reducer types shown in actual output — no API
key needed).

## Tomorrow
<!-- One line: what's next -->
Day 10 — Branching graphs, checkpoints, and human-in-the-loop approval gates.
