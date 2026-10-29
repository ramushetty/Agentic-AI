# Day 08 — Structured Outputs, Reliability & API Deployment

**Module:** Module 4

## Objectives
- [ ] Generate structured outputs using schema-first JSON
- [ ] Ensure reliability through validation, retries, and fallbacks
- [ ] Deploy pipelines as API services
- [ ] Implement tool integration patterns

## Notes
Full write-up: [notes.md](notes.md)

## Resources
<!-- Docs, articles, videos you used today -->
- [OpenAI: Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [FastAPI documentation](https://fastapi.tiangolo.com/)

## Key Learnings
<!-- Write this in your own words after studying/building. This is the part that goes public. -->

Reflection prompts (answer in your own words, after reading notes.md):
1. Design a schema (field names + types) for extracting structured info from a product review.
2. Describe what should happen, step by step, if an LLM call in production times out three times in a row.
3. Why might two different chains in the same app want to share one tool definition instead of each
   defining their own copy?

## Notes / Code
<!-- Link to code in this folder, or to the relevant project/ folder -->
See [notes.md](notes.md) for the full lesson, plus two runnable pieces of code:
[code/day08_structured_output_and_reliability.ipynb](code/day08_structured_output_and_reliability.ipynb)
(Pydantic schemas, validation errors, and a retry-with-backoff demo — no API key needed) and
[code/api_example.py](code/api_example.py) (a small FastAPI app with a schema-validated `/ask`
endpoint — run with `uvicorn api_example:app --reload`).

## Tomorrow
<!-- One line: what's next -->
Day 09 — LangGraph fundamentals: state schemas and reducers.
