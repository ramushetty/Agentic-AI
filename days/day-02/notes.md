# Day 02 Notes — LLM Internals: Tokens, Context, Embeddings & Transformers

**Module:** Module 2 · **Objectives covered:** tokens/tokenization · context windows · embeddings ·
transformer architecture & attention · training vs. inference

## TL;DR (short version)

- **Tokens** = the small chunks of text an LLM actually reads — not letters, not whole words, usually
  word-pieces. Roughly 1 token ≈ 4 English characters.
- **Context window** = the total number of tokens (input + output together) a model can "see" in one
  request. Anything outside it is invisible to the model.
- **Embeddings** = turning text into a list of numbers that captures its *meaning*, so similar meanings
  end up as nearby numbers.
- **Transformers** = the architecture behind every modern LLM. The key trick is **attention** — every
  token directly looks at every other token to figure out what matters.
- **Training vs. inference** = training is the (very expensive, rare) process of teaching the model by
  adjusting its weights. Inference is the (cheap, constant) process of actually using the already-trained
  model to answer you.

---

## 1. Tokens and Tokenization

**Tokenization, in one line: breaking text into small pieces the model can actually read.**

Here's the root problem it solves: a computer doesn't understand words or letters at all — it only
understands numbers. So before any text can reach an LLM, it has to be chopped into small chunks
(**tokens**), and each chunk gets converted into a number.

**On what basis does a piece of text become a specific number? Two completely different bases, in two
steps — this is the part that's easy to blur together:**

**Step 1 — text piece → token ID. This number is 100% arbitrary, just a position in a list.** Think of
a class roster: every student gets a roll number (1, 2, 3...) that has nothing to do with who they
are — it's just "which row of the list are you." A tokenizer's vocabulary is built the same way: scan
a huge amount of text, find the ~100,000 most common chunks, and write them down as a numbered list.
```
"un" is the 1918th entry in this particular list  →  so "un" = token ID 1917
```
That's the whole basis: **position in a prebuilt list.** If the list had been built in a different
order, "un" could just as easily have been ID 40 or ID 90,000 — the number itself means nothing.

> **One line to remember this by: a token ID is just a word-piece's position number in the model's
> vocabulary list — nothing more.**

**Step 2 — token ID → embedding vector. This is where real meaning enters, and it's *learned*, not
arbitrary** (full detail in Section 3): the model looks up row 1917 in a separate table, and that
row — a list of many decimal numbers — is what actually got tuned during training so that
similar-meaning tokens end up with similar rows.

**Concrete example, both steps together:**
```
"unhappiness"  →  "un"+"happi"+"ness"  →  IDs [1917, 4102, 655]  →  each ID's row in the embedding table
     (text)          (tokens: 3 pieces)    (arbitrary list positions)      (the meaningful vectors)
```

Sometimes a token is a whole word, sometimes it's just part of a word, and sometimes it's a single
punctuation mark — depends on how common that chunk turned out to be when the list was built.

**Why not just make each token a whole word?** Human language has effectively unlimited "words" —
names, typos, slang, brand names, other languages. You can't build a fixed numbered list containing
every possible word. By breaking words into common sub-pieces instead, the model can handle a word it
has *never seen before* by assembling it from familiar pieces, the same way you could sound out an
unfamiliar word from its parts. Try it yourself: a tokenizer that's never seen "flibbertigibbet" can
still handle it, because it can break it into pieces it *has* seen — like "flib" + "ber" + "ti" +
"gibbet" — instead of getting stuck.

> **Why / How / Where / When**
> - **Why:** a model can't have a vocabulary entry for every possible word — human language is
>   effectively infinite (names, typos, slang, new brands).
> - **How:** subword algorithms (BPE, WordPiece, SentencePiece) break text into a fixed set of common
>   chunks, so any word — even one never seen before — can be assembled from familiar pieces.
> - **Where:** the very first step of every LLM pipeline. Nothing reaches the model as raw text — it's
>   always tokens first. Also drives API pricing, since most providers bill per token.
> - **When:** every single time text goes in or comes out of a model — during training AND inference,
>   with no exceptions.

**Types of tokenization:**

- **Word-level** — one token per word. Simple, but the vocabulary list becomes huge, and the model is
  completely stuck on any word it hasn't seen before.
- **Character-level** — one token per letter. Tiny vocabulary, but sequences become very long, which
  makes it slower and harder for the model to learn structure.
- **Subword tokenization** (what every modern LLM actually uses) — breaks words into common chunks
  that balance the two extremes above. The real, named algorithms:
  - **BPE (Byte Pair Encoding)** — used by GPT models. Starts from individual characters and
    repeatedly merges the most frequent pair, building up a vocabulary of common chunks.
  - **WordPiece** — used by BERT. Same basic idea as BPE, but picks merges that best improve the
    model's ability to predict the training data, not just raw frequency.
  - **SentencePiece** — used by many models (T5, LLaMA, and others). Treats the raw text (including
    spaces) as one stream, which makes it work well for languages without clear word boundaries, like
    Japanese or Chinese.

![Word-level vs. character-level vs. subword tokenization of the same sentence](assets/tokenization-explained.svg)

**Rule of thumb for interviews:** 1 token ≈ 4 characters in English, or roughly ¾ of a word — so 100
tokens ≈ 75 words. OpenAI's own tokenizer for GPT models is called `tiktoken`.

**Is the vocabulary preset, or does the model learn it while training?** Preset — every model has a
fixed vocabulary decided *before* training even starts:
```
Huge text corpus  →  run BPE/WordPiece/SentencePiece ONCE  →  fixed vocabulary (e.g. 100K entries)
                                                                        ↓
                                             THEN the model's actual weight-training begins
```
That vocabulary is then frozen for the model's whole lifetime — every model family builds its own from
its own data, so sizes differ (GPT-4o ≈ 200K tokens, LLaMA ≈ 32K, BERT ≈ 30K). Because subword
tokenizers can always fall back to smaller and smaller pieces (down to individual characters/bytes),
nothing is ever truly "out of vocabulary" — unlike old word-level tokenizers, which would get stuck on
any word missing from their fixed list.

## 2. Context Windows

The **context window** is the maximum number of tokens — input plus output, combined — that a model
can work with in a single request. Anything outside that window simply doesn't exist to the model: it
has no memory of anything that isn't explicitly included in the current context.

**This is one shared pool, not separate budgets for asking and replying:**
```
GPT-3.5 window = 16,000 tokens total
Your conversation + question used  =  15,000 tokens
Tokens left for the model's reply  =   1,000 tokens   ← even if it "wants" to say more, it can't
```
So it's never "16K to ask, 16K to reply" — it's 16K total, split between the two. The more you've
already used on input/history, the shorter the model's possible reply gets.

**Analogy:** think of it as the size of a whiteboard. Once the whiteboard is full, something has to be
erased to fit new writing — older parts of a long conversation get dropped or summarized once you go
past the limit.

*(A quick term: a "turn" just means one back-and-forth exchange — you send a message, the model
replies, that's one turn. "Turn 20" = the 20th such exchange in an ongoing chat.)*

```
Turn 1:   [System 80] + [History 120] + [Msg 40] + [free space] + [Reserved reply 80]  → mostly free
Turn 20:  [System 80] + [History 520] + [Msg 40] + [little free] + [Reserved reply 80] → nearly full
```

> **Why / How / Where / When**
> - **Why:** a model has a fixed amount of compute/memory it can spend per request — it cannot look at
>   an unlimited amount of text at once, no matter how powerful it is.
> - **How:** measured in tokens, and input + output share the *same* budget — a bigger reply leaves
>   less room for input, and vice versa.
> - **Where:** shows up directly in chat app design (how much history to keep), RAG (how many
>   retrieved documents you can stuff in), and long-document summarization.
> - **When:** it bites you the moment a conversation runs long or you try to paste in a large document
>   — that's when truncation, summarization, or "lost in the middle" problems start to appear.

**Real numbers (as of this course):**

- GPT-3.5: 4K–16K tokens
- GPT-4 / GPT-4o (OpenAI): 128K tokens
- Claude (Anthropic): 200K tokens, with some models supporting up to 1M
- Gemini 1.5/2.0 (Google): up to 1M–2M tokens

**Why it matters:**

- **Cost** — most APIs charge per token, so a bigger context sent on every request means a bigger bill.
- **Latency** — a bigger context takes longer to process before the model even starts answering.
- **"Lost in the middle"** — research has repeatedly shown models are best at using information placed
  at the *start* or *end* of a long context, and are more likely to miss something buried in the
  middle, even if it technically "fits."
- **Long conversations** — once a chat's history grows past the window, older messages have to be
  dropped or summarized to make room for new ones.

![How a context window fills up with a system prompt, conversation history, and the current message, and what happens when it overflows](assets/context-window-explained.svg)

## 3. Embeddings and Vector Representations

**Embedding vector, in one line: a list of numbers that describes a word's meaning** — the same way
you'd describe a person with height, weight, and age instead of just their name. Similar meaning →
similar number-list, even with zero shared letters ("cat" and "kitten").

**Quick contrast with Section 1:** a **token ID** (like 1917) is just a locker *number* — random, means
nothing by itself. An **embedding vector** (`[0.12, -0.87, ..., 0.05]`) is what's *inside* that locker
— the real meaning, built up during training.

**How does a word get its number-list? Two simple steps:**
1. Tokenization gives the word an ID (Section 1) — just a position in a list, no meaning yet.
2. The model looks up that ID's row in a big table (its "meaning table"). That row is the word's
   starting vector.
```
"cat"  →  token ID 5023  →  row 5023 in the meaning table  →  [0.12, -0.87, ..., 0.05]
```
That table starts as random numbers. During training, the model keeps guessing things (like the next
word), gets corrected when it's wrong, and slowly adjusts these numbers — across billions of examples
— until words used in similar situations end up with similar rows. Nobody tells the model "cat and dog
are both animals"; it works that out just from how those words tend to appear near similar company
(pet, vet, feed, cute).

**Why a vector, and not just the ID number?** Because the ID is random — "cat" = 5023 tells you
nothing. A vector is *trained* so that simple math on it (checking how close two vectors are) actually
tells you whether two words mean something similar. The ID can't do that; the vector can.

**A word's vector isn't always exactly the same everywhere:**
- The starting vector (the table lookup) is identical every time, in the same model.
- As a sentence passes through attention (Section 4), the vector gets adjusted by context — so "bank"
  ends up slightly different in "river bank" vs. "bank account."
- Nothing is learned live when you send a message — the model only *uses* what it already learned.

**What does "4096 dimensions" mean?** Just the count of numbers in the list — 4096 numbers per word,
instead of 3 (height/weight/age). More numbers = more detail the model can capture about meaning. You
can't picture 4096 numbers at once (humans max out at 3), so just think "way more traits than usual."

**What about a whole sentence, not just one word?** That's what RAG actually uses — a separate
**embedding model** turns an entire sentence into ONE vector in a single step:
```
"The cat sat on the mat"  →  embedding model (e.g. text-embedding-3)  →  [0.44, -0.12, ..., 0.91]
```

**How do you check if two vectors are similar?** With **cosine similarity** — it compares the *angle*
between two vectors, not their length. Close to **1** = very similar meaning. Close to **0** =
unrelated.

**Famous example (2013):** `vector("king") − vector("man") + vector("woman") ≈ vector("queen")`. The
model learned ideas like "royalty" and "gender" as directions in this number-space, purely from reading
text — nobody told it what a king or queen actually is.

> **Why / How / Where / When**
> - **Why:** computers can't compare "meaning" directly — they need numbers to do math on.
> - **How:** train a model so similar-meaning text lands as similar vectors, then compare with cosine
>   similarity.
> - **Where:** semantic search, RAG (Modules 4 &amp; 6), recommendations, clustering.
> - **When:** computed once for every document you store, and again for every new question someone
>   asks.

![2D map of word embeddings clustering by meaning, plus the king - man + woman ≈ queen vector arithmetic](assets/embeddings-explained.svg)

**Why this matters here:** instead of matching exact words, you turn both the question and every
document into vectors, then find the documents whose vectors sit closest to the question's vector — so
"how do I get my money back" can still find a document titled "refund policy," with zero shared words.

**Common embedding models:** OpenAI's `text-embedding-3`, Cohere Embed, open-source
`sentence-transformers` — plus the older ones that started it all, Word2Vec and GloVe.

**Is an "embedding model" the same as a Transformer?** Not quite — a Transformer is a *design*
(Section 4), an embedding model is a *job* (turn a sentence into one vector). Most modern embedding
models are built using the Transformer design, just trained for a different job than a chatbot:
```
Chatbot (GPT, Claude):               predicts the next word  →  writes text, one word at a time
Embedding model (text-embedding-3):  maps a WHOLE sentence to ONE vector  →  writes nothing, just compares
```
Word2Vec and GloVe are older and don't use Transformers at all.

## 4. Transformer Architecture and Attention

**What is a Transformer, in simple words?** It's the design used to build almost every AI chatbot
today — GPT, Claude, Gemini. Its one big idea: look at the **whole sentence at once**, instead of
reading it word by word like older systems (RNNs, Day 01) did.

**What is "attention"?** Attention is how the model decides which words matter most for understanding
one specific word.

**Simple example:** *"The animal didn't cross the street because it was too tired."*
The word "it" is confusing on its own — what does it point to? Attention lets the model ask: *"which
word does 'it' really mean?"* — and it correctly lands on "animal," not "street."

```
"it" gives every other word a score, showing how much that word helps explain "it":
animal → 0.72 (very important)
tired  → 0.12
was    → 0.08
street → 0.01 (barely matters)
```
Bigger score = more important for understanding that word.

> **Why / How / Where / When**
> - **Why:** older systems (RNNs) read one word at a time and often forgot earlier words. Attention
>   lets the model connect any two words directly, however far apart they are, and process a whole
>   sentence at once instead of word by word — which also makes it much faster to train.
> - **How:** every word scores every other word. This scoring happens many times side by side, and the
>   whole thing repeats through many layers (sometimes almost 100), getting a little sharper each time.
> - **Where:** inside every major AI language model today — GPT, Claude, Gemini, LLaMA, BERT.
> - **When:** invented in 2017. Used both while the model is learning (training) and while it's
>   answering you (inference).

**The main parts inside a Transformer, one at a time:**

- **Turn words into numbers.** Each word becomes a token, then a number-list (Sections 1 &amp; 3). A
  small tag also gets added showing *where* the word sits in the sentence (1st, 2nd, 3rd...), since
  attention alone has no sense of order.
- **Attention.** Explained above — every word looks at every other word and decides what matters.
- **A small extra thinking step.** After attention, each word's number-list passes through one more
  tiny processing step to refine it further.
- **Repeat, many times.** This whole cycle (attention + thinking step) runs over and over — up to
  around 96 times in GPT-3 — understanding the sentence a little better each round.

![A simplified Transformer block, plus an attention-weight example showing "it" attending strongly to "animal"](assets/transformer-attention-explained.svg)

**A full example, step by step:** `"The cat sat because it was tired."`
*(Numbers below are made up to teach the idea, not real model output.)*

1. Break the sentence into pieces and give each piece a number (Section 1):
   `The, cat, sat, because, it, was, tired, .` → `[464, 3797, 7731, 780, 340, 373, 10032, 13]`
2. Look up each number's starting number-list from the model's table (Section 3):
   `cat (3797) → [0.55, 0.12, -0.40, 0.08, 0.71, -0.09]`
3. Add a small tag for word order (1st word, 2nd word, ...).
4. Let every word look at every other word (attention): `"it" → cat: 0.68, tired: 0.15, was: 0.09, ...`
   — "it"'s number-list now leans heavily toward "cat."
5. Tidy up the numbers a bit, so they stay in a stable range.
6. Run each word's numbers through the small extra thinking step.
7. Tidy up again.
8. Repeat steps 4–7 many times — each round understands the sentence a bit more deeply.
9. Use the final numbers to guess the next word. Feed in `"The cat sat because it was"` and "tired"
   comes out as the best guess — it gets written, then fed back in to guess the *next* word after that.
   This is why a chatbot writes one word at a time.

**Is what I just described an "encoder" or a "decoder"?** Good question — it's a decoder. The original
2017 design actually had two halves:

- **Encoder** — reads the *whole* sentence at once, and every word can see every other word,
  including ones that come later. Good at *understanding* a full piece of text.
- **Decoder** — *writes* the answer one word at a time, and can only look at words already written —
  never ones that don't exist yet. Good at *generating* text.

```
Encoder looking at "it":  can see every word in the sentence (before AND after "it")
Decoder looking at "it":  can only see words that came before "it" — nothing after
```

In plain terms:
- **BERT** = encoder only → great at understanding text, but doesn't write new text.
- **GPT, Claude, LLaMA** = decoder only → write text one word at a time. Almost every chatbot you use
  is this type.
- **The original 2017 Transformer** = both halves together → used for translation (read one language,
  write another).

The 9-step example above is the decoder type — that's exactly why it writes one word, looks at what it
just wrote, then writes the next word, and keeps going.

## 5. Training vs. Inference

**Training** = teaching the model. You feed it a huge amount of data, it makes a prediction, you
compare that prediction to the real answer (the difference is called the **loss**), and you nudge
millions or billions of internal numbers (**weights**) slightly to make the next prediction a bit
better. Repeat this process billions of times. This is extremely expensive — training a large model
can cost tens of millions of dollars in compute — and it happens rarely: once for pre-training, then
occasionally again for fine-tuning or updates.

**Inference** = using the model. You give the already-trained, **frozen** model a new input, and it
produces an output in a single pass — no weights change. This is what happens every single time you
send a message to ChatGPT or Claude. It's far cheaper per use than training, but it happens millions of
times a day across every user.

**Analogy:** training is like years of medical school — expensive, slow, and mostly a one-time thing.
Inference is like a doctor seeing a patient — fast, drawing on everything already learned, with no
re-studying required for each visit.

```
Training:   Data → Predict → Compare to correct answer (Loss) → Adjust weights → repeat billions of times
Inference:  Your input → Frozen model (same weights) → Output          → one pass, no weight changes
```

> **Why / How / Where / When**
> - **Why:** a model has to *learn* a language and a huge amount of world knowledge before it's useful
>   (training), and then needs a fast, cheap way to actually be used by millions of people afterward
>   (inference) — these are two very different jobs with very different cost profiles.
> - **How:** training repeats forward pass → loss → backpropagation → weight update, billions of times.
>   Inference is one forward pass through the already-trained, frozen weights — no learning happens.
> - **Where:** training happens inside the model creator's own data centers (OpenAI, Anthropic, Google,
>   etc.). Inference happens wherever the model is deployed — an API call, a chat app, an agent's tool
>   call — anywhere a request reaches the model.
> - **When:** training happens rarely — once for pre-training, occasionally again for fine-tuning.
>   Inference happens constantly — every single message you send is one inference call.

![Training loop (data -> prediction -> loss -> backpropagation -> updated weights, repeated billions of times) vs. inference (frozen model, one input, one output, no weight changes)](assets/training-vs-inference-explained.svg)

### Quick comparison

| | Training | Inference |
|---|---|---|
| Goal | Learn the weights | Use the weights |
| Data needed | Huge amounts (often self-supervised, see Day 01) | Just your one input |
| Cost | Very high, mostly a one-time/rare cost | Low per request, but happens constantly |
| Changes the model's weights? | Yes | No |
| Real example | Pre-training GPT-4 on a huge text corpus | You asking ChatGPT a question right now |

## Interview Q&A (Day 02)

**Q1. What is a token, and why don't LLMs just use whole words?**
A token is a chunk of text — sometimes a whole word, often a piece of one. LLMs use subword tokens
instead of whole words because human language has effectively unlimited possible words (names, typos,
slang); subword tokenization lets the model handle a word it has never seen by assembling it from
familiar pieces, instead of getting stuck.

**Q1a. Is a model's vocabulary preset, or learned during training?**
Preset. The vocabulary is built once, before the model's actual weight-training even starts, by
running BPE/WordPiece/SentencePiece over a large text corpus. It's then frozen for the model's
lifetime. Every model family builds its own vocabulary from its own data (GPT-4o ≈ 200K tokens, LLaMA
≈ 32K, BERT ≈ 30K), so vocabularies differ across models but are fixed within a given model.

**Q2. Name the common tokenization algorithms and one model that uses each.**
BPE (Byte Pair Encoding) — used by GPT models. WordPiece — used by BERT. SentencePiece — used by T5,
LLaMA, and others; it's especially useful for languages without clear word boundaries like Japanese.

**Q3. What is a context window, and what happens when a conversation exceeds it?**
The context window is the maximum number of tokens (input + output combined) a model can process in
one request. Once a conversation's history grows past that limit, older messages have to be dropped or
summarized to make room — the model literally cannot see anything outside the window.

**Q4. What is the "lost in the middle" problem?**
Research shows LLMs are best at using information placed at the very start or very end of a long
context, and are more likely to miss or under-use information buried in the middle — even though it
technically fits within the context window. This matters a lot for RAG system design (Module 6).

**Q5. What is an embedding, and how do you measure whether two embeddings are similar?**
An embedding is a numerical vector representation of text that captures meaning rather than exact
wording — similar meanings produce nearby vectors. Similarity is typically measured with cosine
similarity, which compares the angle between two vectors: close to 1 means very similar, close to 0
means unrelated.

**Q5a. How does a token actually become a vector — is there a vocabulary lookup involved?**
Yes. After tokenization assigns a token an ID (an integer), the model has an embedding matrix — one
row per vocabulary entry, each row a vector of numbers. Getting a token's starting vector is a lookup:
ID 5023 → row 5023 of the table → e.g. `[0.12, -0.87, ..., 0.05]`. That table starts random and is
learned during training. As the vector then flows through the Transformer's attention layers, it gets
reshaped by context — so the same starting row for "bank" ends up as two different final vectors in
"river bank" vs. "bank account." Whole-sentence embeddings (used in RAG) work differently — a separate
embedding model maps the entire sentence to one vector directly, not via a per-token lookup.

**Q6. What's the famous word2vec example that shows embeddings capture meaning, not just words?**
`vector("king") - vector("man") + vector("woman") ≈ vector("queen")`. The model learned concepts like
"royalty" and "gender" as directions in vector space purely from text, without ever being told what a
king or queen actually is.

**Q7. Why did Transformers replace RNNs/LSTMs for language models?**
RNNs process one token at a time and pass a "memory" forward, so they struggle with long-range
dependencies and can't be parallelized well during training. Transformers use self-attention to let
every token directly connect to every other token in one pass, which solves the long-range problem and
trains much faster on modern hardware (GPUs/TPUs) because it's highly parallelizable.

**Q8. Explain self-attention in one sentence, with an example.**
Self-attention lets every token weigh how relevant every other token is to understanding it — e.g. in
"The animal didn't cross the street because it was too tired," attention connects "it" directly and
strongly to "animal" rather than "street," regardless of the distance between them.

**Q9. What is multi-head attention, and why use more than one head?**
Instead of computing attention once, the model computes it several times in parallel ("heads"), and
each head can specialize in a different kind of relationship — e.g. one head tracking grammatical
structure, another tracking coreference (like "it" → "animal"). Combining multiple heads gives the
model a richer understanding than a single attention computation could.

**Q9a. Walk me through what happens to a sentence as it passes through a Transformer.**
Tokenize the text into pieces and look up each piece's arbitrary ID → look up each ID's row in the
embedding table for a context-free starting vector → add a positional encoding so the model knows word
order → self-attention lets every token score and absorb relevant information from every other token
(e.g. "it" pulling in "cat") → add-and-normalize → a feed-forward network refines each token's vector
further → add-and-normalize again → repeat that whole block N times (96 for GPT-3) → the final layer's
output becomes a probability distribution over the vocabulary, and the highest-scoring token is
generated, then fed back in to predict the next one.

**Q9b. Is GPT an encoder or a decoder? What's architecturally different about BERT vs. GPT?**
GPT (and Claude, LLaMA) are decoder-only: causal/masked attention means each token can only see itself
and earlier tokens, never future ones — which is exactly why they generate text one token at a time,
feeding each output back in as input. BERT is encoder-only: bidirectional attention lets every token
see every other token, past and future, which makes it good at understanding a complete input (and why
most embedding models are encoder-style) but unable to generate text token-by-token the way GPT does.
The original 2017 Transformer used both halves together for translation (encoder reads the source
sentence, decoder generates the translation).

**Q10. What's the practical difference between training and inference in terms of cost and frequency?**
Training adjusts the model's weights using huge amounts of data and is extremely expensive but
infrequent — it happens once for pre-training and occasionally for fine-tuning. Inference uses the
already-trained, frozen model to produce an output for a single input, doesn't change any weights, and
is cheap per call but happens constantly — every single chat message is one inference call.

## Sources

- [Attention Is All You Need (arXiv, 2017)](https://arxiv.org/abs/1706.03762)
- [The Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
