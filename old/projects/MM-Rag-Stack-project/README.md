# MM-RAG-Stack

A Multi-Modal Retrieval-Augmented Generation (RAG) stack for parsing, ingesting, and querying documents (PDFs, DOCX, tables, and images) with an LLM-powered generation pipeline.

## Project Structure

```
MM-Rag-Stack-project/
├── Data/                # Source documents (PDFs, etc.)
├── config/
│   └── config.yaml      # Application configuration
├── exception/
│   └── custom_exception.py  # Custom exception handling
├── logger/
│   └── custom_logger.py     # Structured logging setup
├── prompt_library/
│   └── prompt.py         # Prompt templates
├── src/
│   ├── parsing.py         # Document parsing (PDF/DOCX/OCR/tables)
│   ├── ingestion.py        # Chunking & indexing pipeline
│   ├── retriever.py        # Retrieval logic
│   └── generation.py       # LLM answer generation
├── get_library_version.py
├── requirments.txt
└── README.md
```

## Tech Stack

- **PDF parsing & document processing**: PyMuPDF, pdfplumber, pypdf, python-docx
- **OCR & image processing**: Pillow, pytesseract
- **Data & table processing**: pandas, tabulate
- **RAG document models**: langchain-core
- **Structured logging**: structlog

## Requirements

- Python **3.12**
- [uv](https://docs.astral.sh/uv/) for Python version and virtual environment management

## Setup

### 1. List available Python versions

```bash
uv python list
```

### 2. Create a virtual environment (Python 3.12)

```bash
uv venv --python 3.12 myvenv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**
```powershell
myvenv\Scripts\Activate.ps1
```

**Windows (cmd):**
```cmd
myvenv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
uv pip install -r requirments.txt
```

## Usage

> Project is under active development — usage instructions will be added as the pipeline (parsing → ingestion → retrieval → generation) is implemented.

## Environment Variables

Create a `.env` file in the project root for secrets and configuration (e.g. API keys). This file is git-ignored and should never be committed.
