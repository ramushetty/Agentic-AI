# Agentic AI — 30 Day Learning Log

A lean, 30-day, hands-on path through modern agentic AI engineering: LLM foundations,
LangChain/LangGraph, agentic RAG, GraphRAG with Neo4j, MCP, guardrails, evaluation/observability,
Databricks governance, and production deployment.

This repo is my daily build-in-public log — written to double as **interview prep for Agentic AI and
Gen AI roles**, not just a personal journal. Each day has a folder with objectives, what I actually
learned, links to code, and a set of interview Q&A for that day's topics. Six real-time projects are
built along the way and tie multiple modules together.

## How this is organized

- [`days/`](days) — one folder per day (`day-01` ... `day-30`). Each has a `README.md` log
  (objectives → resources → key learnings → links) and a `notes.md` with the actual write-up for
  that day's objectives, diagrams for anything structural/hierarchical, and an **Interview Q&A**
  section — the part meant to be read by other learners (and re-read before an interview).
- [`projects/`](projects) — one folder per real-time project, built across the days that reference it.
- Source code for a given day/project lives inside that day's or project's own folder.

## 30-Day Roadmap

| Day | Module | Focus | Log |
|----:|--------|-------|-----|
| 01 | Module 2 | AI, ML, DL, NLP & the Road to Agentic AI | [days/day-01](days/day-01/README.md) |
| 02 | Module 2 | LLM Internals: Tokens, Context, Embeddings & Transformers | [days/day-02](days/day-02/README.md) |
| 03 | Module 2 | LLM App Frameworks & Prompt Engineering | [days/day-03](days/day-03/README.md) |
| 04 | Module 3 | Agentic Architectures | [days/day-04](days/day-04/README.md) |
| 05 | Module 3 | Agentic Design Patterns & ReAct | [days/day-05](days/day-05/README.md) |
| 06 | Module 4 | Data Ingestion & Splitting for LLM Pipelines | [days/day-06](days/day-06/README.md) |
| 07 | Module 4 | Embeddings, Vector DBs & LCEL Composition | [days/day-07](days/day-07/README.md) |
| 08 | Module 4 | Structured Outputs, Reliability & API Deployment | [days/day-08](days/day-08/README.md) |
| 09 | Module 5 | LangGraph Fundamentals & State | [days/day-09](days/day-09/README.md) |
| 10 | Module 5 | Branching Graphs, Checkpoints & Human-in-the-Loop | [days/day-10](days/day-10/README.md) |
| 11 | Module 5 | Agent Memory & Deployment | [days/day-11](days/day-11/README.md) |
| 12 | Project 2 (build) | Multi-Agent Collaboration System — Build Day 1 | [days/day-12](days/day-12/README.md) |
| 13 | Project 2 (build) | Multi-Agent Collaboration System — Build Day 2 & Writeup | [days/day-13](days/day-13/README.md) |
| 14 | Module 6 | Agentic RAG: Adaptive Retrieval | [days/day-14](days/day-14/README.md) |
| 15 | Module 6 | Evidence-First Answers & RAG Evaluation | [days/day-15](days/day-15/README.md) |
| 16 | Module 7 | Knowledge Graph Modeling with Neo4j | [days/day-16](days/day-16/README.md) |
| 17 | Module 7 | Provenance, Constraints & Governance-Ready Graphs | [days/day-17](days/day-17/README.md) |
| 18 | Module 8 | GraphRAG: Multi-Hop Traversal & Hybrid Retrieval | [days/day-18](days/day-18/README.md) |
| 19 | Module 8 | GraphRAG: Explainable Reasoning Paths | [days/day-19](days/day-19/README.md) |
| 20 | Project 1 (build) | GraphRAG Knowledge System — Build Day 1 | [days/day-20](days/day-20/README.md) |
| 21 | Project 1 (build) | GraphRAG Knowledge System — Build Day 2 & Writeup | [days/day-21](days/day-21/README.md) |
| 22 | Module 9 | MCP: Standardized Tool Contracts | [days/day-22](days/day-22/README.md) |
| 23 | Project 3 (build) | MCP Tool-Augmented Agent — Build & Writeup | [days/day-23](days/day-23/README.md) |
| 24 | Module 10 | No-Code Agents with n8n | [days/day-24](days/day-24/README.md) |
| 25 | Module 11 | Safety Engineering & Guardrails | [days/day-25](days/day-25/README.md) |
| 26 | Module 12 | Evaluation & Observability with Langfuse | [days/day-26](days/day-26/README.md) |
| 27 | Project 5 (build) | LLM Evaluation and Observability — Build & Writeup | [days/day-27](days/day-27/README.md) |
| 28 | Module 13 | Databricks Governance & Text-to-SQL Agents | [days/day-28](days/day-28/README.md) |
| 29 | Project 4 (build) | Databricks Ask-to-Query Agent — Build & Writeup | [days/day-29](days/day-29/README.md) |
| 30 | Module 14 + Project 6 | Production Deployment: Docker, FastAPI, CI/CD & Capstone | [days/day-30](days/day-30/README.md) |

## Projects

| # | Project | Modules Covered | Scheduled | Folder |
|---|---------|------------------|-----------|--------|
| 01 | GraphRAG Knowledge System | Module 7, Module 8 | Days 16-21 | [projects/01-graphrag-knowledge-system](projects/01-graphrag-knowledge-system/README.md) |
| 02 | Multi-Agent Collaboration System | Module 3, Module 5, Module 11 | Days 4-13 | [projects/02-multi-agent-collaboration](projects/02-multi-agent-collaboration/README.md) |
| 03 | MCP Tool-Augmented Agent | Module 9, Module 11 | Day 22-23 | [projects/03-mcp-tool-augmented-agent](projects/03-mcp-tool-augmented-agent/README.md) |
| 04 | Databricks Ask-to-Query Agent | Module 13 | Day 28-29 | [projects/04-databricks-ask-to-query-agent](projects/04-databricks-ask-to-query-agent/README.md) |
| 05 | LLM Evaluation and Observability | Module 12 | Day 26-27 | [projects/05-llm-evaluation-observability](projects/05-llm-evaluation-observability/README.md) |
| 06 | Deploying an AI Agent to Production | Module 14 | Day 30 | [projects/06-production-deployment](projects/06-production-deployment/README.md) |

## Progress

- [x] Days 1-3 — Foundations (AI/ML/DL/NLP, LLM internals, frameworks & prompting)
- [x] Days 4-5 — Agentic architectures & design patterns
- [ ] Days 6-8 — Production pipelines with LangChain/LCEL
- [ ] Days 9-11 — Stateful agents with LangGraph
- [ ] Days 12-13 — Project 2: Multi-Agent Collaboration System
- [ ] Days 14-15 — Agentic RAG
- [ ] Days 16-17 — Knowledge graphs with Neo4j
- [ ] Days 18-19 — GraphRAG hybrid retrieval
- [ ] Days 20-21 — Project 1: GraphRAG Knowledge System
- [ ] Day 22 — MCP tool standardization
- [ ] Day 23 — Project 3: MCP Tool-Augmented Agent
- [ ] Day 24 — No-code agents with n8n
- [ ] Day 25 — Safety engineering & guardrails
- [ ] Day 26 — Evaluation & observability (Langfuse)
- [ ] Day 27 — Project 5: LLM Evaluation and Observability
- [ ] Day 28 — Databricks governance & Text-to-SQL
- [ ] Day 29 — Project 4: Databricks Ask-to-Query Agent
- [ ] Day 30 — Production deployment + Project 6 capstone

## Stack

LangChain · LangGraph · LangSmith · Langfuse · Neo4j · MCP · n8n · Databricks (Unity Catalog, Delta) · FastAPI · Docker · GitHub Actions

## Running things locally

Each project/day that ships code includes its own setup notes in its `README.md`. Secrets go in a
local `.env` (never committed — see `.gitignore`).
