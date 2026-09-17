# Day 01 Notes — AI, ML, DL, NLP & the Road to Agentic AI

**Module:** Module 2 · **Objectives covered:** AI/ML/DL/NLP differences · evolution to Agentic AI · what "agentic" means · real-world use cases

## TL;DR (short version)

- **AI** = making a computer act smart. It's the big goal.
- **ML** = one way to build AI — instead of writing rules by hand, you show the computer lots of examples and it learns the pattern itself.
- **DL** = one way to do ML — using "neural networks" (layers of math units loosely copying brain neurons). Good at messy raw data like photos, audio, text.
- **NLP** = not a box inside AI/ML/DL. It's a *job*: making computers understand human language. You can do this job with old rules, with ML, or with DL.
- **Agentic AI** = the newest step. Instead of answering one question and stopping, the system plans multiple steps, uses tools, checks its own work, and keeps going until a goal is done — mostly on its own.

---

## 1. AI vs ML vs DL vs NLP (in plain words)

Think of AI, ML, DL as boxes inside boxes, like Russian nesting dolls:

- **AI** is the biggest box — the goal.
- **ML** is a smaller box inside AI — one way to reach that goal.
- **DL** is an even smaller box inside ML — one specific method inside ML.

**NLP is different.** It is not a box inside the others. It's a *job* — "make computers understand
human language." You can do that job the old way (hand-written rules), the ML way, or the DL way.

![AI contains ML contains DL, with NLP as a cross-cutting domain](assets/ai-ml-dl-nlp.svg)

### What is AI?

AI means making a computer do something that normally needs a human brain — recognize a face, play
chess, answer a question. AI does **not** have to learn anything. Old AI programs were just long lists
of rules written by a human.

**Example:** In 1997, a chess program called Deep Blue beat the world chess champion. It never
"learned" anything from data. Humans wrote the rules, and the computer just searched millions of
possible moves very fast using those rules.

### What is ML (Machine Learning)?

ML is a way of building AI where, instead of a human writing every rule, the computer looks at a lot
of examples (data) and figures out the pattern by itself.

**Example:** To build a spam filter, you don't write a rule like "if the email has the word
'lottery', mark it as spam." Instead, you show the computer a million emails that are already labeled
"spam" or "not spam," and it works out the pattern on its own.

There are two common ways a computer can learn from data:

**Supervised Learning** — you give the computer examples *and* the correct answers, like a teacher
checking homework.

- **Classification** = sorting things into categories.
  Example: Is this email spam or not spam? Is this photo a cat or a dog? Is this loan application
  risky or safe?
- **Regression** = predicting a number.
  Example: What will this house sell for? How many customers will show up tomorrow?

You train the model on examples where you already know the right answer, so it learns the pattern.
Then you show it something new, and it makes its own guess.

**Unsupervised Learning** — you give the computer examples but **no** correct answers. It has to find
patterns or groups on its own.

Example: You give an online store all its customers' purchase histories, with no labels at all. The
computer groups customers into clusters by itself — like "people who mostly buy baby products" and
"people who mostly buy gym gear" — without anyone telling it those groups exist ahead of time.

*(There's a third type, Reinforcement Learning — the computer learns by trial and error, getting a
reward or a penalty, similar to training a dog with treats. This becomes important later when we
build agents that improve from feedback.)*

### What is DL (Deep Learning)?

DL is one specific way of doing ML. It uses a "neural network" — layers of small math units stacked
on top of each other, loosely copying how neurons connect in a brain. DL is especially good when the
input is messy and raw, like a photo, an audio clip, or a page of text — data where you can't easily
write down what "the pattern" looks like in advance.

**Example:** A DL model looks directly at the pixels of an X-ray image and decides if there's a
tumor. Nobody tells it "look for a round white shape" — it works out what to look for by seeing
thousands of labeled X-rays.

### What is NLP (Natural Language Processing)?

NLP is not a box inside AI/ML/DL — it's a job: making computers understand and use human language
(text or speech). That job can be done with old-style rules, with ML, or with DL.

**Example:** Google Translate in 2006 used statistics and phrase-matching — an older method. Today's
Google Translate uses deep learning (a "transformer" model) and produces much more natural sentences.

### Quick comparison

| Term | In one line | Example |
|---|---|---|
| **AI** | Making a computer act smart — with or without learning | Deep Blue chess program (hand-written rules, no learning) |
| **ML** | Computer learns a pattern from data instead of being told rules | Spam filter trained on labeled emails |
| **DL** | ML using brain-like layered networks — good with messy raw data | A neural network reading X-ray images |
| **NLP** | Applying AI/ML/DL to human language | Google Translate |

## 2. How we got from rule-based systems to Agentic AI

| Time | What people built | Example | Main weakness |
|---|---|---|---|
| 1950s–80s | Rule-based programs ("expert systems") | MYCIN — diagnosed infections using hand-written if-then rules | Broke on anything the rule-writer didn't think of |
| 1990s–2010s | ML (statistics-based) | Early spam filters, product recommendations | Needed a human to hand-pick which features mattered; only good at one narrow task |
| 2012–2020 | DL (neural networks) | Image classifiers, early chatbots | Great at recognizing things, but still just "one input → one output," no memory or planning |
| 2020–2023 | Large Language Models (LLMs) | GPT-3/4 answering a question or writing code in one go | Smart at reasoning, but passive — waits for you to ask, gives one answer, can't use tools or hold a goal over time |
| 2023–now | **Agentic AI** | A system that makes a plan, uses tools, checks its own answer, and repeats until the goal is done | Needs careful setup (LangGraph, guardrails), but can now do real multi-step work on its own |

**The pattern:** every stage removes one limit from before it.
- Rules → nothing is removed, a human still writes every decision.
- ML → removes "a human has to hand-write the logic" (the computer learns it from data).
- DL → removes "a human has to hand-pick the features" (the network figures that out itself).
- LLMs → remove "you need a separate trained model for every task" (one model handles many tasks via prompting).
- Agentic AI → removes "the system only acts after a human asks it a single question" (now it decides
  the next step itself, again and again, until the goal is met).

## 3. What actually makes a system "agentic"?

If a system answers one question and stops, that is **not** agentic — it's just input in, output out,
done. A system becomes "agentic" when it has some mix of these:

1. **Has a goal, not just one instruction.**
   "Book me the cheapest flight to Delhi next month" (a goal) is different from "Translate this
   sentence" (a single task).
2. **Plans its own steps.** It breaks the goal into steps by itself, instead of following a script a
   human wrote.
3. **Can take action, not just talk.** It can search the web, call an API, run code, or query a
   database — not just generate text.
4. **Remembers what it already tried.** So it doesn't repeat a failed action.
5. **Checks and fixes its own work.** It looks at the result of its own action and adjusts — this is
   called "reflection" (covered in Module 3).
6. **Runs several steps without a human approving every single one** — though good systems still add
   a human check before anything risky (Module 11 covers this).

**Simple test:** if you could screenshot the whole thing as one question and one answer, it's
probably not agentic. If it took several small decisions — plan, act, look at the result, try again —
to get there, it is.

## 4. Real-world examples

- **Automation** — an agent reads a support email, figures out what the customer wants, writes a
  reply, checks the reply against company policy, and only asks a human when it isn't sure. (This
  "check with a human when unsure" idea is the guardrail pattern from Module 11.)
- **Copilots** — tools like GitHub Copilot or Cursor now do more than autocomplete: they read your
  whole codebase, plan a change across multiple files, run your tests, and fix what fails. That loop
  is close to the "planner-executor" pattern from Module 3.
- **Assistants** — ask an assistant to "find flights, check my calendar for conflicts, and book the
  one that fits," and it has to call several tools (flight search, calendar, payment) in the right
  order. That's the same kind of agent loop we build starting in Module 5 (LangGraph) and standardize
  in Module 9 (MCP).

## Sources

- [Building Effective AI Agents — Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [Agentic AI vs. Traditional AI — GeeksforGeeks](https://www.geeksforgeeks.org/artificial-intelligence/agentic-ai-vs-traditional-ai/)
- [Agentic AI vs Traditional AI: Key Differences — FullStack Blog](https://www.fullstack.com/labs/resources/blog/agentic-ai-vs-traditional-ai-what-sets-ai-agents-apart)
