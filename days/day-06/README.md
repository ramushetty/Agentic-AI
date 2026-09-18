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
1. Pick any RAG pipeline's ingestion code (your own, or an open-source one) and explain, in your own
   words, what its `chunk_size`/`chunk_overlap` settings actually do to a document.
2. Describe a document type where structure-aware splitting (keeping tables separate) would matter a
   lot, and one where it wouldn't matter at all.
3. Why might splitting by token count give a different result than splitting by character count?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson, and
[code/day06_document_loaders_and_splitting.ipynb](code/day06_document_loaders_and_splitting.ipynb) for
a hands-on notebook (loads a real file, compares fixed-size vs. recursive splitting, shows chunk
overlap in actual output — no API key needed).

## Tomorrow
<!-- One line: what's next -->
Day 07 — Embeddings with vector databases, and building pipelines with LCEL.
