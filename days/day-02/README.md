# Day 02 — LLM Internals: Tokens, Context, Embeddings & Transformers

**Module:** Module 2

## Objectives
- [ ] Understand tokens and tokenization (and the named algorithms: BPE, WordPiece, SentencePiece)
- [ ] Learn about context windows — real sizes, cost/latency impact, "lost in the middle"
- [ ] Understand embeddings and vector representations (cosine similarity, the king/queen example)
- [ ] Learn the basics of transformer architecture and attention mechanisms
- [ ] Differentiate between training and inference

## Notes
Full write-up: [notes.md](notes.md)

## Resources
<!-- Docs, articles, videos you used today -->
- [Attention Is All You Need (arXiv, 2017)](https://arxiv.org/abs/1706.03762)
- [The Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/)

## Key Learnings
<!-- Write this in your own words after studying/building. This is the part that goes public. -->

Reflection prompts (answer in your own words, after reading notes.md):
1. Explain to a non-technical friend why ChatGPT sometimes "forgets" something you said earlier in a
   long conversation — without using the words "token" or "context window."
2. Pick a sentence with a pronoun in it (like "it," "they," "this") and explain what self-attention
   would need to do to resolve what that pronoun refers to.
3. Why is training rare and expensive while inference is constant and cheap-per-call? What would break
   if it were the other way around?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson.

## Tomorrow
<!-- One line: what's next -->
Day 03 — LLM app frameworks (LangChain, LangGraph, LangSmith, Langfuse) and prompt engineering.
