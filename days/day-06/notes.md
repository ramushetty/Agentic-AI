# Day 06 Notes — Data Ingestion & Splitting for LLM Pipelines

**Module:** Module 4 · **Objectives covered:** document loaders · text splitting strategies

## TL;DR (short version)

- **Document loaders** turn a messy file (PDF, Word doc, webpage) into clean text + metadata, so the
  rest of your pipeline doesn't have to care what format the file started in.
- **Text splitting** breaks that clean text into small chunks, because both context windows (Day 02)
  and RAG retrieval work better on small, focused pieces than one giant blob.
- **Chunk size + overlap** are the two settings that matter most — a typical real pipeline uses
  something like `chunk_size=2000`, `chunk_overlap=120`.
- **Production-grade loading** = one pipeline that handles everything a real PDF throws at it: scanned
  pages (OCR), tables, figures, corrupted files — and never lets one bad file crash the whole run
  (Section 3, with a real 58-page paper in the notebook).

---

## 1. Data ingestion with document loaders

A **document loader** reads a file and converts it into a standard format — usually plain text plus
metadata (filename, page number) — that the rest of your pipeline can work with, no matter what the
file originally was.

**Why this is needed:** a PDF, a Word doc, and a webpage are all *completely* different internally — a
PDF has fonts, layout, and embedded images; a webpage is full of HTML tags; a Word doc is its own
zipped XML format. Without a loader, your pipeline would need custom parsing code for every file type.
The loader hides all of that mess.

```
Raw PDF file  →  document loader (parses layout, pulls out text/tables/images)  →  clean text + metadata
```

**Named loaders you'll actually use:**
- **PDFs** — PyMuPDF, pdfplumber, PyPDFLoader
- **Word docs** — Docx2txtLoader
- **Webpages** — WebBaseLoader
- **Spreadsheets/CSVs** — CSVLoader
- **Scanned/handwritten PDFs** — OCR tools like `pytesseract`, since there's no real text layer to
  extract — the loader has to read the pixels, not a text stream.

![Different file types (PDF, DOCX, webpage, CSV) each go through their own loader, converging into the same clean text-plus-metadata format](assets/document-loaders-explained.svg)

> **Why / How / Where / When**
> - **Why:** every downstream step (splitting, embedding, retrieval) expects plain text, not a raw
>   PDF's internal byte structure.
> - **How:** each file type gets its own loader that knows how to read that specific format; all of
>   them output the same shape — text plus metadata like filename and page number.
> - **Where:** the very first step of any RAG pipeline — before splitting, before embeddings.
> - **When:** every time a new document enters your system, whether that's once during setup or
>   continuously as new files arrive.

## 2. Text splitting strategies

A loaded document is often huge — way bigger than a context window (Day 02) or an embedding model can
handle well in one piece. **Splitting** breaks it into smaller chunks before anything else happens to
it.

**Why smaller chunks help retrieval, not just size limits:** in RAG, you're matching a user's specific
question against chunks by similarity (Day 02's embeddings). A whole book as one chunk is too broad to
match a specific question well. A small, focused chunk about one topic matches much better.

**Splitting strategies, from worst to best default:**
- **Fixed-size splitting** — cut every N characters, no matter what. Simple, but it can slice a
  sentence or even a word right in half, breaking meaning.
- **Recursive character splitting** (the common default — what your own project uses) — tries to
  split on natural boundaries first: paragraph breaks, then sentence breaks, then word breaks, only
  falling back to a hard cut if nothing else works. Keeps chunks readable.
- **Token-based splitting** — splits by token count (Day 02) instead of character count, since tokens
  are what actually count against context windows and API cost.
- **Semantic splitting** — uses embeddings to find natural topic-boundary points in the text, so each
  chunk stays about one coherent idea. More accurate, more expensive to compute.
- **Structure-aware splitting** — splits along headers/sections, and keeps tables or images as their
  own separate chunks instead of mixing them into surrounding text. A multi-modal RAG pipeline often
  tags each chunk with a `content_type` (`text`, `table`, `image`) so retrieval can treat them
  differently later.

**The two settings that matter most: chunk size and overlap.**
```
50,000-character document  →  split with chunk_size=2000, chunk_overlap=120  →  ~25 overlapping chunks
```
**Overlap** means consecutive chunks share a small strip of text at the boundary, so a fact or sentence
that happens to sit right at a cut point doesn't get lost — it still appears whole in at least one
chunk.

![Fixed-size splitting cutting mid-sentence vs. recursive splitting respecting natural boundaries, plus what chunk overlap looks like between two consecutive chunks](assets/text-splitting-explained.svg)

> **Why / How / Where / When**
> - **Why:** context windows and embedding models both have size limits, and retrieval accuracy drops
>   when chunks are too broad or cut mid-thought.
> - **How:** pick a splitting strategy (recursive is the safe default), set a chunk size that fits
>   comfortably within your embedding model's limit, and add a small overlap so boundary content isn't
>   lost.
> - **Where:** right after loading (Section 1), right before embedding (Day 02) — the "ingestion" step
>   of any RAG pipeline.
> - **When:** every document, every time it's ingested — this isn't a one-off setting, it's a step
>   that runs for every new file.

## 3. Production-grade ingestion: what real documents throw at you

The simple loader from Section 1 works on clean files. Real PDFs are much messier. Part 2 of the
notebook runs **one pipeline on a real 58-page research paper** (the DeepSeek-V4 technical report) to
show every case in action.

**What real documents contain — and the path each one needs:**

| What you meet | The problem | The fix |
|---|---|---|
| Normal text pages | You need page numbers for citations | Extract text per page, keep `page` in metadata |
| Scanned pages (a photo of a page) | No text layer at all — extraction returns nothing | Detect "no text + a big picture", then run OCR (Tesseract) |
| Tables with grid lines | Flattening loses rows and columns | PyMuPDF table finder, then a **quality check** |
| Tables without grid lines (most papers) | The finder finds nothing — or invents fake tables from charts | Rebuild rows from word positions, under the "Table N" caption |
| Embedded images | Text extraction ignores them | Save the original image, skip tiny decorative logos |
| Charts drawn as shapes ("vector figures") | They aren't images at all, so image extraction misses them | Find drawing clusters, render that region to a PNG |
| Corrupted / wrong-type / locked files | One bad file crashes the whole batch | Catch errors per file, log them, keep going |

**How the borderless-table rebuild works (in one line):**
```
words with x/y positions → group into lines by y → split each line at big x-gaps → markdown row
"AGIEval (EM)"  "0-shot"  "80.1"  "82.6"  "83.1"   →   | AGIEval (EM) | 0-shot | 80.1 | 82.6 | 83.1 |
```

**Real numbers from the notebook run** (58 pages, about 6 seconds):
```
8 tables recovered from word positions  |  45 fake "tables" (chart labels, diagrams) rejected
20 vector figures rendered + 5 raster images (decorative logos skipped), each with its caption
simulated scanned page → OCR → 99.9% match with the real text
corrupted.pdf and logo.png → reported and skipped, and the run still finished
```

**Two surprises worth remembering:**
- The paper has only **5 real embedded images but 20 figures.** Charts in papers are usually drawn as
  vector shapes, not stored as pictures — so a loader that only extracts "images" misses most figures.
- PyMuPDF's built-in table finder found **0 real tables and 45 fake ones.** It works from drawn lines
  (its own docs say borderless tables may fail), and most paper tables have no lines. This is why every
  table candidate needs a **quality gate** instead of blind trust.

![A production PDF ingestion pipeline: safety checks, per-page routing between normal extraction (tables, text, images, vector figures) and OCR, then documents with metadata, splitting of text only, and an ingestion report](assets/production-pdf-pipeline-explained.svg)

**Which loader is best?** There's no single winner — each has a job:

| Tool | Best at | Weak at |
|---|---|---|
| `pypdf` / `PyPDFLoader` | Simple, pure Python, easy to start | Weak layout handling, no tables or images |
| **PyMuPDF** | Fast, accurate text, images, page rendering, figures, ruled tables | Borderless tables and multi-column pages need extra work |
| `pdfplumber` | Precise word coordinates, good table control | Slower, needs tuning |
| `unstructured` | Many file types, element-level structure (titles, tables) | Heavy install, slower |
| Docling / Marker | Layout-aware ML parsing: better tables, reading order, equations | Slower, heavier, newer |
| Cloud services (Azure Document Intelligence, AWS Textract, Google Document AI) | Highest accuracy on tables, forms, scans | Costs money; your data leaves your machine |
| Tesseract | Free OCR for scanned pages | Not perfect on equations or handwriting |

**The practical recommendation:** use **PyMuPDF as the fast backbone** (text, images, figures, page
rendering), add an **OCR fallback** for scans and **quality gates** on tables — then **route only the hard
pages** to a heavier parser. Run cheap methods on everything; pay for expensive ones only where they help.

**Production checklist** (every item is in the notebook's Part 2):
- Validate the input first (exists? really a PDF? locked?).
- Isolate errors **per page** and **per file** — report, don't crash.
- Keep a **whitelist** of metadata (this paper's author field is 3,800+ characters — don't copy it to
  every chunk).
- Store a **file hash** so unchanged files can be skipped on re-ingestion.
- Label extraction confidence (`ruled_table` vs `caption_layout` vs `ocr_text`).
- If a table can't be parsed, **leave its text in the page** instead of dropping it.
- Emit an **ingestion report** (counts, rejected, failed, seconds) for every file.

> **Why / How / Where / When**
> - **Why:** real documents mix text, scans, tables, and figures, and one weak spot (a scanned page, a
>   corrupted file) can silently ruin retrieval quality or crash a whole batch.
> - **How:** a router per page — text layer present → normal extractors; no text + big picture → OCR —
>   with each extractor returning `Document`s that carry a `content_type` and rich metadata.
> - **Where:** the ingestion stage of any serious RAG system, before splitting and embedding.
> - **When:** as soon as your documents stop being clean text files — which, for real business data
>   (contracts, reports, papers, invoices), is almost immediately.

## Interview Q&A (Day 06)

**Q1. What does a document loader actually do, and why can't you skip it?**
It converts a specific file format (PDF, DOCX, webpage) into a standard shape — plain text plus
metadata — that the rest of the pipeline can work with. Skipping it would mean every downstream step
needs its own custom parsing logic for every possible file type, which doesn't scale.

**Q2. Why does RAG need text splitting at all — why not just embed the whole document?**
Two reasons: size limits (a whole document often exceeds context window and embedding model limits),
and retrieval quality (a whole document as one chunk is too broad to match a specific question well —
smaller, focused chunks retrieve more accurately).

**Q3. What's the difference between fixed-size and recursive character splitting?**
Fixed-size splitting cuts every N characters regardless of content, which can slice a sentence or word
in half. Recursive splitting tries natural boundaries first — paragraphs, then sentences, then words —
only falling back to a hard cut as a last resort, which keeps chunks more coherent.

**Q4. What is chunk overlap, and why does it matter?**
Overlap means consecutive chunks share a small strip of text at their boundary. It prevents a fact or
sentence sitting right at a cut point from being lost — it still appears whole in at least one chunk,
instead of being split across two chunks that neither fully contain it.

**Q5. Why would you split by token count instead of character count?**
Because context window limits and API costs are both measured in tokens (Day 02), not characters, and
1 token doesn't equal 1 character (roughly 4 characters per token in English) — splitting by character
count can produce chunks that are bigger or smaller than intended in terms of actual token budget.

**Q6. How do you handle scanned PDFs in an ingestion pipeline?**
A scanned page has no text layer — just a picture — so normal extraction returns empty text. Detect
that (almost no extractable text *and* an image covering most of the page), render the page to an
image, run OCR (e.g. Tesseract), and tag the result as OCR'd so it can be trusted a little less than
native text. Checking picture coverage matters: a page that's just a big chart with a short caption also
has little text, but it isn't a scan.

**Q7. Why do tables and figures need special handling in a RAG pipeline?**
Flattening a table into plain text destroys its rows and columns, so a question about one cell can
retrieve garbage. Figures carry information text extraction can't see at all. The standard pattern is to
turn each table into a structured (e.g. Markdown) document, and each figure into a document whose text
is its caption — so text search can find it — with the image path in metadata so an app or a
vision model can show or read the real picture.

**Q8. A research paper has 20 figures but your image extractor finds only 5 images. Why?**
Most charts in papers are drawn as vector graphics (lines and shapes), not stored as embedded pictures,
so "extract images" misses them. You have to detect clusters of drawing commands and render those
regions to images yourself, and grab each figure's caption for searchable text.

**Q9. What makes an ingestion pipeline "production-grade" instead of a notebook demo?**
Input validation, error isolation per page and per file (report, don't crash), a whitelist of metadata,
a file hash so unchanged files can be skipped, confidence labels on heuristic output, quality gates on
uncertain results (like table detection), an ingestion report with counts and failures, and routing only
the hard pages to a heavier parser instead of paying for the expensive path everywhere.

**Q10. Compare PyPDF, PyMuPDF, pdfplumber, and unstructured — when would you pick each?**
PyPDF for simple, dependency-light text extraction. PyMuPDF as a fast, accurate backbone that also gives
images, page rendering, and ruled tables. pdfplumber when you need precise word coordinates and table
control. `unstructured` (or Docling/Marker, or cloud services like Textract) when you need layout-aware,
element-level structure or high-fidelity tables — at the cost of speed, weight, or money. A common
production design runs the fast option on everything and escalates only the hard pages.

## Sources

- [PyMuPDF documentation](https://pymupdf.readthedocs.io/)
- [DeepSeek-V4 technical report (arXiv, used as the real-world test document)](https://arxiv.org/abs/2606.19348)
- [LangChain: Document loader integrations](https://docs.langchain.com/oss/python/integrations/document_loaders)
- [LangChain: Text splitter integrations](https://docs.langchain.com/oss/python/integrations/splitters)
