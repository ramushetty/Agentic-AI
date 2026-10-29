# Extra: Memory Management Practice Notebooks

Self-study, course-along notebooks on agent memory — not part of the 30-day curriculum in
[`days/`](../../days) or the 6 portfolio projects in [`projects/`](../../projects). The polished,
from-scratch write-up on memory is [Day 11](../../days/day-11/notes.md) (short-term vs. long-term memory,
trimming/summarizing, and persistence, with a tested notebook). These notebooks go further into memory
*techniques* specifically, and are kept here for personal reference.

## What's here

| File | What it covers |
|---|---|
| [memory_managment(1).ipynb](<memory_managment(1).ipynb>) | The fullest notebook: the problem with keeping full chat history, sliding-window memory, summary + recent messages, a small data-ingestion step, and memory management in LangGraph including persistent (SQLite) storage and `langmem`'s automatic memory manager (an LLM that extracts and stores facts on its own). |
| [memory_managment.ipynb](memory_managment.ipynb) | An earlier, shorter draft of the notebook above (most of its cells also appear in the `(1)` version) — covers the full-history problem, sliding-window memory, and summary + recent messages. |
| [memory_in_langgraph.ipynb](memory_in_langgraph.ipynb) | A focused look at memory inside LangGraph itself: state, checkpointers, and the store — the same ideas as Day 11, from a different angle. |

## Setup

`memory_managment(1).ipynb` needs a few packages not otherwise used elsewhere in this repo:
```
pip install langmem
```
(`faiss-cpu` and `sentence-transformers` are already in the repo's `requirements.txt`.) It also needs an
OpenAI key — it asks for one interactively (`getpass`) if `OPENAI_API_KEY` isn't already set, so no key
ever gets saved into the notebook file:
```
OPENAI_API_KEY=...    # platform.openai.com/api-keys
```

## Reference links

- [LangChain: Memory concepts](https://docs.langchain.com/oss/python/concepts/memory) — the ideas behind sliding-window and summary memory
- [LangGraph: Stores (long-term memory)](https://docs.langchain.com/oss/python/langgraph/stores)
- [LangGraph: Persistence (checkpointers)](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangMem documentation](https://langchain-ai.github.io/langmem/) — the automatic memory manager used in `memory_managment(1).ipynb`
- [LangChain: vector store integrations](https://docs.langchain.com/oss/python/integrations/vectorstores) (FAISS is used here for semantic memory search)
- [LangChain: HuggingFace embeddings](https://docs.langchain.com/oss/python/integrations/text_embedding/huggingfacehub)
- [OpenAI API keys](https://platform.openai.com/api-keys)
