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
4. Run Part 2 on a different PDF of your own. Which content types (text / table / figure / ocr_text) did
   it find, and where did the pipeline struggle?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson, and
[code/day06_document_loaders_and_splitting.ipynb](code/day06_document_loaders_and_splitting.ipynb) for
a hands-on notebook in two parts (no API key needed):

- **Part 1 — simple:** loads a small text file, compares fixed-size vs. recursive splitting, shows chunk
  overlap in actual output. Fully offline.
- **Part 2 — a real PDF, step by step:** seven small steps on a real 58-page research paper (the
  DeepSeek-V4 technical report, downloaded once into a git-ignored folder): keep page numbers, chunk
  without losing them, pictures and charts, why tables are hard, OCR for scanned pages, and handling
  broken files. OCR needs the free [Tesseract](https://github.com/tesseract-ocr/tesseract) program
  installed; without it, that one cell just says so and the rest still runs.

## Tomorrow
<!-- One line: what's next -->
Day 07 — Embeddings with vector databases, and building pipelines with LCEL.
