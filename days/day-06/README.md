# Day 06 — Data Ingestion & Splitting for LLM Pipelines

**Module:** Module 4

## Objectives
- [ ] Perform data ingestion using document loaders
- [ ] Apply effective text splitting strategies

## Notes
Full write-up: [notes.md](notes.md)

## Resources
<!-- Docs, articles, videos you used today -->
- [LangChain: Document loader integrations](https://docs.langchain.com/oss/python/integrations/document_loaders)
- [LangChain: Text splitter integrations](https://docs.langchain.com/oss/python/integrations/splitters)

## Key Learnings
<!-- Write this in your own words after studying/building. This is the part that goes public. -->

Reflection prompts (answer in your own words, after reading notes.md):
1. Open your `MM-Rag-Stack-project`'s `ingestion.py` and explain, in your own words, what
   `chunk_size=2000, chunk_overlap=120` actually does to a document.
2. Describe a document type where structure-aware splitting (keeping tables separate) would matter a
   lot, and one where it wouldn't matter at all.
3. Why might splitting by token count give a different result than splitting by character count?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson.

## Tomorrow
<!-- One line: what's next -->
Day 07 — Embeddings with vector databases, and building pipelines with LCEL.
