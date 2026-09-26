# Extra: LangGraph Practice Notebooks

These two notebooks are self-study, course-along practice with LangGraph — not part of the 30-day
curriculum in [`days/`](../../days) and not one of the 6 portfolio projects in [`projects/`](../../projects).
They're kept here for personal reference, since the actual daily notes (see
[Day 09](../../days/day-09/notes.md), [Day 10](../../days/day-10/notes.md), and
[Day 11](../../days/day-11/notes.md)) are the polished, from-scratch write-ups meant for other learners.

## What's here

| File | What it covers |
|---|---|
| [Langraph_intro.ipynb](Langraph_intro.ipynb) | The basics: a `StateGraph`, nodes, edges. |
| [Langraph_introduction.ipynb](Langraph_introduction.ipynb) | A longer walkthrough: tool-calling agents (Tavily web search), a small RAG pipeline (HuggingFace embeddings + Chroma), and Groq as the LLM. |
| [Data/sample.txt](Data/sample.txt) | Sample text the RAG cells load with a `DirectoryLoader`. |

## Setup

Needs two packages not otherwise used elsewhere in this repo:
```
pip install langchain-groq langchain-tavily
```
And two free API keys in a `.env` file at the repo root:
```
GROQ_API_KEY=...      # console.groq.com
TAVILY_API_KEY=...    # app.tavily.com
```

## Reference links

- [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain documentation](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain: Groq integration](https://docs.langchain.com/oss/python/integrations/chat/groq)
- [LangChain: Tavily search tool](https://docs.langchain.com/oss/python/integrations/tools/tavily_search)
- [LangChain: Chroma vector store](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma)
- [LangChain: HuggingFace embeddings](https://docs.langchain.com/oss/python/integrations/text_embedding/huggingfacehub)
- [Groq console (free API key)](https://console.groq.com)
- [Tavily (free API key)](https://app.tavily.com)
