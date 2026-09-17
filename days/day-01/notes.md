# Day 01 Notes — AI, ML, DL, NLP & the Road to Agentic AI

**Module:** Module 2 · **Objectives covered:** AI/ML/DL/NLP/Gen AI differences, history & types · evolution to Agentic AI · what "agentic" means · real-world use cases

## TL;DR (short version)

- **AI** = making a computer act smart. It's the big goal. Started: **1956**.
- **ML** = one way to build AI — instead of writing rules by hand, you show the computer lots of examples and it learns the pattern itself. Started: **1959**.
- **DL** = one way to do ML — using "neural networks" (layers of math units loosely copying brain neurons). Good at messy raw data like photos, audio, text. Took off: **2012**.
- **NLP** = not a box inside AI/ML/DL. It's a *job*: making computers understand human language. You can do this job with old rules, with ML, or with DL. Started: **1950**.
- **Gen AI** = a newer job: instead of sorting or predicting, it *creates new content* — text, images, audio, code. Went mainstream: **2020–2022** (GPT-3, DALL-E, ChatGPT).
- **Agentic AI** = the newest step. Instead of answering one question and stopping, the system plans multiple steps, uses tools, checks its own work, and keeps going until a goal is done — mostly on its own. Took off: **2023–now**.

---

## 1. AI vs ML vs DL vs NLP vs Gen AI (in plain words) — with history and types

Think of AI, ML, DL as boxes inside boxes, like Russian nesting dolls:

- **AI** is the biggest box — the goal.
- **ML** is a smaller box inside AI — one way to reach that goal.
- **DL** is an even smaller box inside ML — one specific method inside ML.

**NLP is different.** It is not a box inside the others. It's a *job* — "make computers understand
human language." You can do that job the old way (hand-written rules), the ML way, or the DL way.

![AI contains ML contains DL, with NLP as a cross-cutting domain and Gen AI as a newer generative job — full reference card with definitions, start dates, and examples for each](assets/ai-ml-dl-nlp.svg)

### What is AI?

AI means making a computer do something that normally needs a human brain — recognize a face, play
chess, answer a question. AI does **not** have to learn anything. Old AI programs were just long lists
of rules written by a human.

**Example:** In 1997, a chess program called Deep Blue beat the world chess champion. It never
"learned" anything from data. Humans wrote the rules, and the computer just searched millions of
possible moves very fast using those rules.

**When did AI start?** People started using the name "Artificial Intelligence" in **1956**, at a
summer workshop at Dartmouth College in the US. That workshop is usually treated as the official
birth of AI as a field of study — even though the *idea* of "thinking machines" is older than that.

### What is ML (Machine Learning)?

ML is a way of building AI where, instead of a human writing every rule, the computer looks at a lot
of examples (data) and figures out the pattern by itself.

**Example:** To build a spam filter, you don't write a rule like "if the email has the word
'lottery', mark it as spam." Instead, you show the computer a million emails that are already labeled
"spam" or "not spam," and it works out the pattern on its own.

**When did ML start?** The name "Machine Learning" was first used in **1959** by Arthur Samuel, who
built a program that learned to play checkers by playing against itself over and over. ML stayed a
mostly academic/statistics topic for decades, until computers got fast enough and data got big enough
(roughly from the 2000s onward) for it to become genuinely useful in products.

**Types of ML (how a computer can learn — this is the classification you asked about):**

![Types of Machine Learning: supervised (classification/regression), unsupervised (clustering/dimensionality reduction), reinforcement, semi/self-supervised — with the named algorithms for each](assets/ml-types.svg)

There are **four** common ways a computer can learn from data:

**1. Supervised Learning** — you give the computer examples *and* the correct answers, like a teacher
checking homework.

- **Classification** = sorting things into categories.
  Example: Is this email spam or not spam? Is this photo a cat or a dog? Is this loan application
  risky or safe?
  **Common algorithms:** Logistic Regression, Decision Tree, Random Forest, SVM (Support Vector
  Machine), Naive Bayes, K-Nearest Neighbors (KNN), Gradient Boosting (XGBoost/LightGBM).
- **Regression** = predicting a number.
  Example: What will this house sell for? How many customers will show up tomorrow?
  **Common algorithms:** Linear Regression, Ridge/Lasso Regression, Decision Tree/Random Forest
  Regression, SVR (Support Vector Regression).

You train the model on examples where you already know the right answer, so it learns the pattern.
Then you show it something new, and it makes its own guess.

**2. Unsupervised Learning** — you give the computer examples but **no** correct answers. It has to
find patterns or groups on its own. There are two common jobs here too:

- **Clustering** = grouping similar things together.
  Example: an online store groups customers into clusters by purchase history — like "people who
  mostly buy baby products" and "people who mostly buy gym gear" — without anyone telling it those
  groups exist ahead of time.
  **Common algorithms:** K-Means, Hierarchical Clustering, DBSCAN, Gaussian Mixture Model (GMM).
- **Dimensionality Reduction** = squeezing a large number of features down to a smaller number, while
  keeping most of the useful information.
  Example: a dataset with 100 columns about a customer gets compressed to 10 columns that still
  capture almost everything important — makes the data faster to work with and easier to visualize.
  **Common algorithms:** PCA (Principal Component Analysis), t-SNE, UMAP.

**3. Reinforcement Learning** — the computer learns by trial and error, getting a reward or a penalty,
similar to training a dog with treats. It tries an action, sees if the result was good or bad, and
adjusts.

*Example: AlphaGo, the AI that beat the world champion at the game Go in 2016, learned by playing
millions of games against itself — winning was the reward, losing was the penalty. Self-driving cars
also use this to learn things like smooth braking.*

**Common algorithms:** Q-Learning, Deep Q-Network (DQN), Policy Gradient methods, PPO (Proximal Policy
Optimization).

This becomes important later when we build agents that improve from feedback.

**4. Semi-supervised / Self-supervised Learning** — a mix: a small amount of labeled data plus a huge
amount of unlabeled data. **This is the one that's easy to miss, but it's the most important one for
this course** — it's exactly how today's large language models are pre-trained. They read huge amounts
of plain text with no human labels at all, and just learn to predict the next word, over and over,
across billions of sentences.

### What is DL (Deep Learning)?

DL is one specific way of doing ML. It uses a "neural network" — layers of small math units stacked
on top of each other, loosely copying how neurons connect in a brain. DL is especially good when the
input is messy and raw, like a photo, an audio clip, or a page of text — data where you can't easily
write down what "the pattern" looks like in advance.

**Example:** A DL model looks directly at the pixels of an X-ray image and decides if there's a
tumor. Nobody tells it "look for a round white shape" — it works out what to look for by seeing
thousands of labeled X-rays.

**When did DL start?** The idea of a computer "neuron" goes back to **1943**, and the first working
neural network (called the Perceptron) was built in **1958**. But none of that worked well until
**2012**, when a neural network called AlexNet won an image-recognition contest by a huge margin.
That moment is usually seen as the real start of the deep learning boom, because it proved stacking
many layers actually works once you have enough data and computing power.

**Types of DL (classified by the shape of the network):**

- **CNN** (Convolutional Neural Network) — good at images (spotting shapes, edges, objects).
  *Example: Face ID unlocking your iPhone by recognizing your face.*
- **RNN / LSTM** (Recurrent Neural Network) — an older method for sequences like text or time series;
  reads one step at a time, so it's slow and forgets long sequences.
  *Example: the old-style predictive keyboard on phones, before modern autocomplete got smarter.*
- **Transformer** — today's standard for sequences (text, and now images/audio too); reads the whole
  sequence at once using "attention" — you'll go deeper into this on Day 02.
  *Example: ChatGPT, Claude, Google Translate's current version.*
- **GAN** (Generative Adversarial Network) — two networks compete against each other to generate
  realistic new content.
  *Example: "This Person Does Not Exist" — a website that generates a realistic human face that has
  never actually existed, using a GAN.*
- **Autoencoder** — learns to compress data down and rebuild it, often used to spot unusual/abnormal data.
  *Example: a bank's fraud-detection system flagging a transaction because it looks nothing like the
  customer's normal spending pattern.*

### What is NLP (Natural Language Processing)?

NLP is not a box inside AI/ML/DL — it's a job: making computers understand and use human language
(text or speech). That job can be done with old-style rules, with ML, or with DL.

**Example:** Google Translate in 2006 used statistics and phrase-matching — an older method. Today's
Google Translate uses deep learning (a "transformer" model) and produces much more natural sentences.

**When did NLP start?** NLP is often traced back to **1950**, when Alan Turing asked "can machines
think?" and proposed the Turing Test. Early NLP (1950s–1980s) was rule-based. Statistical NLP took
over in the 1990s–2000s. Neural/deep-learning NLP took over from about **2013** onward, and the
"Transformer" architecture introduced in **2017** changed everything — it's the direct ancestor of
today's LLMs.

**Types of NLP tasks (classification):**

- **Text Classification** — sorting text into categories.
  *Example: Gmail deciding an email is spam, or Twitter/X flagging a tweet as likely harmful.*
- **Named Entity Recognition (NER)** — finding names of people, places, or companies inside text.
  *Example: LinkedIn automatically pulling your job title and company name out of your profile text.*
- **Machine Translation** — translating between languages.
  *Example: Google Translate, DeepL.*
- **Question Answering** — answering a question using a document as the source.
  *Example: asking Alexa or Siri "what time does the store close?" and it reads the answer off a webpage.*
- **Summarization** — shortening a long piece of text without losing the key points.
  *Example: an app like Otter.ai turning a 1-hour meeting recording into a 5-bullet summary.*
- **Text Generation** — writing brand-new text (this is where NLP and Gen AI meet).
  *Example: ChatGPT or Claude writing an email for you from a short instruction.*

### What is Gen AI (Generative AI)?

Older AI/ML/DL mostly did one of two jobs: **predict a number**, or **sort something into a category**
(classification). Gen AI does something different — it **creates brand-new content** (text, images,
audio, video, or code) that didn't exist before, instead of just labeling or predicting.

**Example:** You type "a cat wearing a spacesuit, photorealistic" into an image generator, and it
creates a picture that has never existed before. Or you ask an LLM to write an email, and it
generates original sentences word by word.

**When did Gen AI start?** Early generative models existed as far back as **2014** (GANs) and **2013**
(Variational Autoencoders), but "Generative AI" as most people know it today really took off between
**2020 and 2022**: GPT-3 (2020) showed large language models could write fluent, useful text; DALL-E
(2021) and Stable Diffusion (2022) showed AI could turn a text description into a realistic image; and
ChatGPT (November 2022) put all of this in front of ordinary people through a simple chat window.

**Types of Gen AI (classification, by what it generates):**

- **Text generation** — LLMs like GPT, Claude, Gemini (writing, chatting, coding)
- **Image generation** — diffusion models like Stable Diffusion, DALL-E, Midjourney
- **Audio/speech generation** — text-to-speech, music generation
- **Video generation** — turning a text prompt into a short video clip
- **Code generation** — tools like GitHub Copilot and Claude Code (writing and editing software)

Gen AI is built using deep learning (mostly Transformers for text, and diffusion models for images).
It's also the technology that made agentic AI possible — an agent needs to *generate* a plan, a piece
of code, or a reply, not just sort things into categories.

### Quick comparison

| Term | In one line | Started | Example |
|---|---|---|---|
| **AI** | Making a computer act smart — with or without learning | 1956 (name coined at Dartmouth) | Deep Blue chess program (hand-written rules, no learning) |
| **ML** | Computer learns a pattern from data instead of being told rules | 1959 (Arthur Samuel's checkers program) | Spam filter trained on labeled emails |
| **DL** | ML using brain-like layered networks — good with messy raw data | 2012 (AlexNet breakthrough) | A neural network reading X-ray images |
| **NLP** | Applying AI/ML/DL to human language | 1950 (Turing Test) | Google Translate |
| **Gen AI** | Creating brand-new content instead of just predicting/sorting | 2020–2022 (GPT-3, DALL-E, ChatGPT) | ChatGPT, Stable Diffusion |

![Timeline: 1950 NLP idea, 1956 AI named, 1959 ML named, 2012 DL takes off, 2017 Transformer, 2020-22 Gen AI mainstream, 2023 Agentic AI](assets/timeline.svg)

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

## Interview Q&A (Day 01)

Short, direct answers you could actually say out loud in an interview.

**Q1. What is the difference between AI, ML, and DL?**
AI is the umbrella goal — a machine acting intelligently, with or without learning. ML is a subset of
AI where the system learns patterns from data instead of being hand-coded. DL is a subset of ML that
uses multi-layer neural networks, and it's especially strong on raw, unstructured data like images,
audio, and text.

**Q2. Where does NLP fit into AI/ML/DL?**
NLP is not a layer inside AI/ML/DL — it's an application domain. It's the task of making a computer
understand or produce human language, and that task can be solved with rules, classic ML, or deep
learning (today, almost always deep learning via transformers).

**Q3. What's the difference between supervised and unsupervised learning?**
Supervised learning trains on labeled data — the model is given the correct answer for every example
(used for classification and regression). Unsupervised learning trains on unlabeled data — the model
has to find structure or groupings on its own (e.g. clustering).

**Q4. What's the difference between classification and regression?**
Classification predicts a category or class (spam vs. not spam). Regression predicts a continuous
number (a house price).

**Q4a. Name a few common classification algorithms, and when would you pick Logistic Regression over
Random Forest?**
Logistic Regression, Decision Tree, Random Forest, SVM, Naive Bayes, KNN, and Gradient Boosting
(XGBoost/LightGBM) are the common ones. Pick Logistic Regression when you want something fast,
interpretable, and the relationship between features and the outcome is roughly linear — e.g. you need
to explain *why* a loan was rejected. Pick Random Forest (or Gradient Boosting) when the relationships
are more complex/non-linear and you care more about accuracy than explainability.

**Q4b. What's the difference between K-Means and Hierarchical Clustering?**
K-Means picks a fixed number of cluster centers ("k") upfront, assigns each point to its nearest
center, and repeats until the centers stop moving — fast, but you have to choose k in advance.
Hierarchical Clustering builds a tree of clusters by repeatedly merging (or splitting) groups, so you
don't have to pick the number of clusters ahead of time, but it's slower on large datasets. DBSCAN is
a common third option — it groups densely packed points and automatically finds outliers, with no
need to specify k at all.

**Q4c. What is PCA used for, and when would you use it?**
PCA (Principal Component Analysis) compresses a large number of features into a smaller number of
"components" that still capture most of the original information. It's used to speed up training,
reduce noise, fight overfitting, and to visualize high-dimensional data in 2D/3D. t-SNE and UMAP are
used more specifically for visualization rather than as a general preprocessing step, since they're
better at preserving local clusters visually but distort global distances more.

**Q5. What is self-supervised learning, and why does it matter for LLMs?**
Self-supervised learning generates its own labels from the raw data itself — for example, predicting
the next word in a sentence using the sentence as its own label. It's how large language models like
GPT and Claude are pre-trained on huge amounts of plain text without any human labeling.

**Q6. What actually triggered the deep learning boom?**
In 2012, a CNN called AlexNet won the ImageNet image-recognition competition by a huge margin,
proving that deep, many-layer networks could beat traditional approaches once there was enough data
and compute (GPUs) to train them.

**Q7. What is Generative AI, and how is it different from traditional ML/DL?**
Traditional ML/DL mostly classifies or predicts a number from existing data. Generative AI creates
new content — text, images, audio, video, or code — that didn't exist before. It's built on deep
learning (transformers for text, diffusion models for images).

**Q8. What makes a system "agentic" rather than just a chatbot or a single model call?**
An agentic system has a goal (not just one instruction), plans its own steps, can take real actions
through tools, remembers what it already tried, checks and corrects its own output, and runs multiple
steps with limited — not zero — human oversight. A single prompt-and-response is not agentic.

**Q9. How did we get from rule-based expert systems to agentic AI?**
Each era removed one limitation from the one before it: rule-based systems needed a human to write
every decision; ML removed the need to hand-code logic by learning from data; DL removed the need to
hand-engineer features; LLMs removed the need for a separate trained model per task; agentic AI
removed the need for a human to prompt every single action — the system now plans and acts across
multiple steps on its own.

**Q10. Give an example of an agentic workflow vs. a non-agentic one.**
Non-agentic: asking an LLM to translate one sentence — one input, one output, done. Agentic: asking an
assistant to "find flights, check my calendar for conflicts, and book the cheapest one that fits" — it
has to plan, call several tools (search, calendar, payment) in the right order, and adapt if something
doesn't fit.

**Q11. Why does the CNN vs. Transformer distinction come up so often in interviews?**
CNNs are built for grid-like data (images) — they use convolution filters to detect local patterns
like edges. Transformers process a whole sequence at once using "attention," which lets them capture
long-range relationships between words far apart in a sentence. That's why transformers, not CNNs or
RNNs, became the backbone of modern LLMs — full detail on Day 02.

## Sources

- [Building Effective AI Agents — Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [Agentic AI vs. Traditional AI — GeeksforGeeks](https://www.geeksforgeeks.org/artificial-intelligence/agentic-ai-vs-traditional-ai/)
- [Agentic AI vs Traditional AI: Key Differences — FullStack Blog](https://www.fullstack.com/labs/resources/blog/agentic-ai-vs-traditional-ai-what-sets-ai-agents-apart)
