# HalachaBench v1: early results (provisional)

*1 November 2026, updated 6 November 2026* · Hebrew summary: [בעברית, בקצרה](#בעברית-בקצרה)

> **Fork proposal:** a [historical semicha reference track](#historical-semicha-reference-track-proposal) is proposed
> for future benchmarking. It is metadata-only, with no new Q&A or scores. The original results below are unchanged.

**6 November:** three of Meta's Muse models added, run through Meta's Muse Code CLI: Muse Wonder Full, Muse Wonder
and Muse Spark 1.3. Muse Wonder Full places 8th (60.8); see [Results](#results).

**3 November:** two earlier GPT models added, GPT-5.6 Sol and GPT-6 Sol. The older one scored far higher; see
[Results](#results).

**2 November:** five models added, all scored on the same questions, rubrics and judge: Gemini 4 Argon, Grok 4.7,
Grok 4.3, Claude Opus 4.8 and Claude Sonnet 4.6. See [Checks on the Grok results](#checks-on-the-grok-results).

HalachaBench tests how well AI models answer real questions from the semicha (rabbinic ordination) exams of the Chief
Rabbinate of Israel. These early results cover 27 models on the **test set: the 60 questions of five papers of the
Cheshvan 5787 sitting** (Niddah, Chuppah v'Kiddushin, Mitzvot HaTeluyot BaAretz, Mikvaot, Tefillah u'Brachot), a
sitting that began on 12 October 2026. Each model answered every question three times, in Hebrew, closed-book.

> **These results are provisional, and they are not exam grades.** A score of 80 does not mean a model would pass the
> semicha exam, or that its answers can be relied on to pasken. One AI judge (GPT-6 Astra, itself a contestant) has
> graded the answers so far. The rubrics were written by an AI model and reviewed by AI models; no rabbi has reviewed
> them, and no rabbi has graded any answer yet. Five more registered runs are not in this table yet and will be added
> whatever they score: Gemma 4 26B-A4B, Mistral Small 4 119B, Nemotron 3.5
> Lightning 30B, Nemotron 3.5 Super VL 120B, and a second, disclosed Qwen3.8 27B run with a larger output limit, added
> after the first run's results were seen. Four other pre-registered open-weight models (Granite 4.2 30B, Hermes 4.3
> 36B, Nanbeige4.3 33B, Olmo 3.1 32B Think) were dropped before answering any question: three did not fit the GPU at the
> registered context, and the runtime could not separate Olmo's reasoning from its answer. Claude Opus 5.5 will grade
> as a second judge. Read the caveats below before quoting a number.

![HalachaBench early results: bar chart of the 27 models' scores with 95% intervals](results.png)

## Results

Score: how much of the rubric an answer achieves, 0–100 (see [Scoring](#scoring)), averaged over 60 questions × 3
attempts. Worst of 3: the lowest of the three attempts at each question, averaged.

| # | Model | Score | 95% interval | Worst of 3 | How it ran |
|---|---|---|---|---|---|
| 1 | Claude Fable 5.1 | 79.7 | 75.8 – 83.4 | 70.4 | Claude Code CLI, effort high |
| 2 | Gemini 4 Argon † | 78.2 | 74.3 – 81.9 | 70.7 | Antigravity CLI, effort high ³ |
| 3 | GPT-5.6 Sol † | 77.3 | 72.4 – 81.3 | 68.5 | Codex, effort high ⁵ |
| 4 | GPT-6 Astra | 73.3 | 69.4 – 77.0 | 66.2 | Codex, effort high |
| 5 | GPT-6.1 Sol | 72.8 | 69.1 – 76.2 | 63.9 | Codex, effort high |
| 6 | Claude Opus 5.5 | 69.1 | 64.7 – 73.3 | 60.0 | Claude Code CLI, effort high |
| 7 | Gemini 3.8 Flash | 64.4 | 59.7 – 68.9 | 54.3 | Antigravity CLI, effort high |
| 8 | Muse Wonder Full † | 60.8 | 56.4 – 65.2 | 47.9 | Muse Code CLI, effort high ⁶ |
| 9 | GPT-6 Sol † | 48.7 | 44.1 – 53.3 | 37.2 | Codex, effort high ⁵ |
| 10 | Muse Wonder † | 48.2 | 43.4 – 53.1 | 35.5 | Muse Code CLI, effort high ⁶ |
| 11 | Claude Opus 4.8 † | 48.0 | 43.3 – 52.7 | 36.3 | Claude Code CLI, effort high |
| 12 | Muse Spark 1.3 † | 36.2 | 32.2 – 40.4 | 22.0 | Muse Code CLI, effort high ⁶ |
| 13 | GPT-6.1 Terra | 34.6 | 30.8 – 38.5 | 25.6 | Codex, effort high |
| 14 | GPT-6 Luna | 32.4 | 28.5 – 36.4 | 21.8 | Codex, effort high |
| 15 | Grok 4.7 † | 29.9 | 26.3 – 33.6 | 16.4 | xAI API, effort high ⁴ |
| 16 | Claude Sonnet 4.6 † | 29.6 | 25.4 – 33.9 | 19.9 | Claude Code CLI, effort high |
| 17 | Claude Sonnet 5.5 | 28.7 | 24.2 – 33.3 | 18.3 | Claude Code CLI, effort high |
| 18 | Grok 4.3 † | 10.8 | 8.1 – 13.6 | 4.8 | xAI API, effort high ⁴ |
| 19 | Muse Glimmer 30B | 10.5 | 7.6 – 13.7 | 4.4 | local, llama.cpp, Q4_K_M |
| 20 | Claude Haiku 5.5 | 8.6 | 6.0 – 11.5 | 3.6 | Claude Code CLI, effort high |
| 21 | Ling 3.0 Flash | 6.1 | 4.4 – 8.0 | 0.9 | local, llama.cpp, Q4_K_M |
| 22 | Qwen3.8 27B | 6.0 | 4.1 – 8.2 | 1.6 | local, llama.cpp, UD-Q4_K_M ¹ |
| 23 | gpt-oss-120b | 4.4 | 2.6 – 6.4 | 2.1 | local, llama.cpp, MXFP4 |
| 24 | DictaLM 3.0 24B Thinking | 4.3 | 2.8 – 6.0 | 0.8 | local, llama.cpp, Q4_K_M ¹ |
| 25 | Gemma 4 31B | 4.3 | 2.5 – 6.4 | 2.0 | local, llama.cpp, Q4_K_M |
| 26 | Llama 4 Scout 17B-16E | 4.2 | 2.6 – 6.0 | 1.4 | local, llama.cpp, Q4_K_M ² |
| 27 | gpt-oss-20b | 1.2 | 0.5 – 2.1 | 0.0 | local, llama.cpp, MXFP4 |

† Added on 2, 3 or 6 November 2026, after the first results were published, each by a recorded amendment to the
pre-registration made before its answers were collected. Claude Opus 4.8, Claude Sonnet 4.6, GPT-5.6 Sol and GPT-6 Sol
are earlier generations, added to see how the scores change across model versions.

95% intervals come from a bootstrap over questions (resampled within each paper, a question's three attempts kept
together; 10,000 replicates). They cover only the choice of questions, not judge or rubric error, which is likely
larger here. Overlapping intervals do not by themselves mean two models are tied, so models were also compared question
by question:
- **Not clearly apart:** Claude Fable 5.1, Gemini 4 Argon and GPT-5.6 Sol (Fable ahead of Argon by 1.5 points, 95%
  interval −1.8 to 4.9, and of GPT-5.6 Sol by 2.5, −2.5 to 7.9); GPT-5.6 Sol with GPT-6 Astra (3.9, −0.9 to 8.5) and
  GPT-6.1 Sol (4.5, −0.5 to 8.9); Gemini 4 Argon and GPT-6 Astra (4.9, −0.3 to 10.0); GPT-6 Astra, GPT-6.1 Sol and
  Claude Opus 5.5; Gemini 3.8 Flash and Muse Wonder Full (3.6, −1.2 to 8.1); GPT-6 Sol, Muse Wonder and Claude Opus
  4.8 (GPT-6 Sol ahead of Opus 4.8 by 0.6, −4.6 to 5.4, and Muse Wonder within 0.4 of both); Muse Spark 1.3 with
  GPT-6.1 Terra (1.6, −3.3 to 6.8) and GPT-6 Luna (3.9, −0.6 to 8.3); GPT-6 Luna, Grok
  4.7, Claude Sonnet 4.6 and Claude Sonnet 5.5; GPT-6.1 Terra and GPT-6 Luna; Grok 4.3, Muse Glimmer 30B and Claude
  Haiku 5.5, and Claude Haiku 5.5 with Qwen3.8 27B; most pairs among ranks 19 to 24.
- **Clearly apart:** Claude Fable 5.1 is ahead of every model except Gemini 4 Argon and GPT-5.6 Sol (by 6.4 points
  over GPT-6 Astra, 1.6 to 11.1); GPT-5.6 Sol is ahead of Claude Opus 5.5 (8.2, 2.0 to 14.1) and every model below it; Gemini 4 Argon is ahead of GPT-6.1 Sol (5.5, 0.8 to 10.2) and every model below it; GPT-6.1 Terra is
  ahead of Grok 4.7 (4.7, 0.5 to 9.1), Claude Sonnet 4.6 (5.0, 0.1 to 10.0) and Claude Sonnet 5.5 (5.9, 0.8 to 10.9);
  Claude Opus 5.5 is ahead of Muse Wonder Full (8.3, 4.5 to 12.0), and Muse Wonder Full is ahead of GPT-6 Sol (12.1,
  7.8 to 16.6) and every model below it; Claude Opus 4.8, GPT-6 Sol and Muse Wonder are apart from every other model
  but one another; Muse Spark 1.3 is ahead of Grok 4.7 (6.4, 2.2 to 10.7) and every model below it; gpt-oss-20b is
  below every other model.
- **Across generations:** Claude Opus 5.5 is 21.0 points above Claude Opus 4.8 (17.4 to 24.9); Claude Sonnet 5.5 and
  Claude Sonnet 4.6 are not clearly apart (0.9, −3.0 to 4.9). In the other direction, GPT-5.6 Sol is 28.6 points above
  the newer GPT-6 Sol (24.2 to 33.2), and ahead of it on 57 of the 59 questions both answered. GPT-6 Sol did not make
  more errors; it wrote shorter answers (a median of about 200 words against about 310, with less thinking) that covered
  fewer of the sources and rulings the rubrics ask for (48% of the requirements, against 77%).
- **Within the Muse models:** Muse Wonder Full is 12.5 points above Muse Wonder (9.3 to 15.8), and Muse Wonder 12.0
  above Muse Spark 1.3 (7.5 to 16.6). Muse Glimmer 30B, the open-weight Muse model run locally, is 25.7 below Muse
  Spark 1.3 (21.7 to 30.0).

¹ Some runs produced no answer text. The model used up the output limit we set while still thinking (DictaLM 9 of 180
and Qwen3.8 27B 9 of 180; the limits were 57,088 and 65,536 tokens, the latter below what Qwen's model card allows), or
stopped after thinking without writing an answer (Qwen3.8 27B 10 of 180). Each such run was tried once more; those
still without an answer score 0, as every failed answer does.

² Llama 4 Scout failed one pre-run check: asked whether it had any tools, it claimed a web-search tool it did not have. It
ran in a sealed container with no network and no tools, so it was kept, and the failure is disclosed here.

³ Gemini 4 Argon's run stopped when the account's usage quota ran out, and finished on purchased Google AI credits (a
recorded amendment; the credits change billing only). During the run, a manual check of the Antigravity program
triggered its auto-update, so 84 of Argon's 180 answers (on 28 questions) ran on version 1.4.12 instead of the
registered 1.4.10. On those 28 questions, Argon's gap to the four models nearest it is within 2.6 points of its gap on
the other 32 (permutation p 0.57 to 0.82), so the version made no visible difference. The answers were kept and are
disclosed here.

⁴ Grok 4.7 and Grok 4.3 ran through xAI's Responses API: no tools in the request, responses not stored, reasoning
effort high, xAI's recommended sampling (temperature 0.7, top_p 0.95). Every response was checked: none used a tool or
a source, and none was cut off. See [Checks on the Grok results](#checks-on-the-grok-results).

⁵ GPT-5.6 Sol and GPT-6 Sol ran on Codex like the other GPT models, with the same settings. GPT-5.6 Sol's Codex
exposes a different set of tool definitions, which is recorded. On all three attempts at one question
(`5787-cheshvan-teluyot-yishum-q11`), for both models, OpenAI's safety system flagged the answer partway through and
signalled a switch to a smaller model. The harness stops any run that receives an event it does not recognise, so that
no answer by another model is recorded under this one's name; those three answers per model score 0, as every failed
answer does. These two runs used a later version of the runner code; the only changes are the pre-run check terms and
an option to rerun a single attempt, and the code that sends the question and records the answer is unchanged.
GPT-5.4 and GPT-5.5 are not offered on the Codex sign-in used here.

⁶ Muse Wonder Full, Muse Wonder and Muse Spark 1.3 ran through Meta's Muse Code CLI on a Muse Code subscription: a
pinned program version (1.4.14), effort high, a fresh process with its own home folder for each answer, the empty
preset, and the web, shell and file-writing tools switched off. Every run was monitored live, and any action other
than writing the answer would have disqualified it; none was. All 180 answers of each model were completed. Muse Code
keeps its tool definitions and built-in instructions in the model's context. Some Muse answers (about 25 of 540) format
their citations as Markdown links to placeholder file paths or web addresses, as a coding assistant would; the citations
themselves are ordinary, and the answers were graded as written.

The local models ran at 4-bit quantization on the maintainer's own hardware. gpt-oss runs in MXFP4, the precision its
weights were released in; the other local models may lose some points against full-precision versions. All 27 models
had every one of their 180 test answers scored.

## Checks on the Grok results

Grok 4.7 scores well below the leaders, so its result was checked more than the others. In short: its answers are
short, and the low score holds up when the grading or the rubrics are changed.

- **Its answers were complete.** All 180 Grok 4.7 answers finished normally, in Hebrew, with no output limit set and
  none cut off; reasoning effort was high on every one. One request failed with a server error and was run again.
- **It writes short answers.** Grok 4.7 thought at length (a median of about 18,000 reasoning tokens per answer) but
  wrote a median of 213 words, against 368 for Claude Sonnet 4.6 and 664 for Gemini 4 Argon. The rubrics give points
  for each source, step and ruling an answer gives, so a short answer that is right on the bottom line still scores low.
- **A blind second grader agreed with the judge.** Claude Opus 5.5, without knowing which model wrote which answer,
  re-graded 30 answers: 15 by Grok 4.7 and 15 by Claude Sonnet 5.5 to the same questions. It agreed with GPT-6 Astra on
  287 of 326 criterion decisions (88%), equally for both models. Grok 4.7's mean was 34.1 from Astra and 32.6 from the
  second grader, so Astra was not harder on Grok.
- **The rubrics Grok disputed don't explain its score.** After the results, Grok 4.7 reviewed all 60 sealed rubrics
  and asked to change or remove 405 of their 661 criteria. Scored again with those criteria taken out, Grok 4.7's
  score goes down, not up, and every model's place barely changes:

  Ranks in this table are among the 22 models scored on 2 November.

  | Scored on | Grok 4.7 | Rank | Gemini 4 Argon | Rank |
  |---|---|---|---|---|
  | All criteria (the results above) | 29.9 | 10 | 78.2 | 2 |
  | Without the 274 criteria Grok said cite a wrong source or should go (59 questions) | 28.5 | 10 | 76.8 | 2 |
  | Only the 256 criteria Grok accepted as written (53 questions) | 26.0 | 12 | 75.3 | 2 |

  Questions left with no criterion to score drop out of that row, for every model alike.
- **Most of Grok's critique did not hold up, and the errors it did find don't move the scores.** Each point Grok made
  that would change a grade was checked against the sources on Sefaria (the Shulchan Aruch, Rambam, Mishnah, Gemara
  and their commentaries). 24 were confirmed as real rubric errors, in 29 criteria; 11 were refuted by the sources,
  and the rest changed only wording or citations. Most confirmed errors are an "also accept" that was too generous,
  for example crediting a lenient ruling no source supports. A few gave points for something the question did not
  ask. Scored without those 29 criteria, Grok 4.7 stays at 29.9, and no model moves by more than 0.7 points.
- **Grok as the judge gives the same result.** Grok 4.7 graded the first attempt at each question by Grok 4.7,
  Claude Sonnet 5.5 and GPT-6 Luna, with the same sealed rubrics and the same instructions GPT-6 Astra had. On the 56
  questions graded for all three, it agreed with Astra on 92% of 1,937 criterion decisions, and its scores were Grok
  4.7 29.7, Claude Sonnet 5.5 30.3 and GPT-6 Luna 28.6 (Astra: 30.5, 30.3 and 31.8). Grok did not score its own
  answers higher than Astra did, relative to the others (+0.8 points, 95% interval −2.9 to 4.3). Four of its 180
  gradings failed on server errors and are left out.

None of this changes the scores above: the rubrics stay as sealed. Any rubric error found is listed and corrected for
every model at once, in the next version.

## How it works

- **Questions.** The papers were transcribed twice from the page images by two Claude models (Claude Fable and Claude
  Opus), and Claude Fable 5.1 settled every difference against the image. No person has proofread the text yet. The
  questions are the Chief Rabbinate's own and are not reproduced here; the papers are published on gov.il. Item ids
  such as `5787-cheshvan-niddah-iyun-q03` name the paper, part and question.
- **Answering.** Each answer was written in a fresh process with nothing from the project but the question, the exam
  rules (answer in Hebrew, cite sources, at most 600 words; the limit is an instruction and longer answers were not cut)
  and a fixed instruction to answer closed-book. No web search. The Claude models ran with every tool switched off; 6 of
  their 1,086 runs still tried to call a tool and were stopped and run again. The GPT and Gemini programs cannot switch
  all their tools off, so tool use was forbidden and every run was monitored live; none of their test runs used a tool.
  A run that tried to use a tool, or ended without an answer, was run once more, and a second failure scores 0. The
  local models ran in sealed containers with no network and no tools. The Grok models ran through xAI's API with no
  tools in the request, and every response was checked for tool or source use (none had any). The Muse models ran
  through Muse Code with its web, shell and file-writing tools switched off and every run monitored live; none of
  their test runs used a tool. The prompts were not identical across programs: the Claude and Grok models saw only a
  short neutral system prompt, the GPT models also saw Codex's built-in instructions and an added instruction not to
  use tools, the Gemini models saw Antigravity's built-in instructions, and the Muse models saw the same neutral system
  prompt along with Muse Code's built-in instructions and tool definitions.
- **Rubrics.** There is no official answer key. Each of the 60 rubrics was drafted by Claude Fable 5.1 as a rabbi would
  write one (sources, Rishonim, ruling, other accepted views, common errors), with 9–12 criteria per question: 7–11
  requirements worth points and 1–3 errors that cost points. A second Claude Fable 5.1 pass critiqued each draft and it
  was revised. Three models from three companies (Claude Fable 5.1, GPT-6 Astra, Gemini 4 Argon) then reviewed every
  rubric: changes at least two of them asked for were applied, and Claude Fable 5.1, the drafter, decided each point
  only one reviewer raised, with a written reason. Claude Opus 5.5 checked the cited sources that Sefaria carries (about
  2,000 lookups, in four rounds); sources Sefaria does not carry are marked unverified, and four minor issues were left
  open. Nobody who wrote or reviewed a rubric saw any model's answer. The rubrics were sealed with a salted cryptographic
  commitment on 29 October 2026 (the date is the seal log's own record; the commitments become public with this
  repository, and the salts that open them will be published when the review round closes), after the Claude and GPT
  models had answered and before any test answer was graded.
- **Grading.** GPT-6 Astra (effort high) decided, for every criterion of every answer that had text, whether the answer
  meets it, under one fixed judge protocol. 5% of the answers (244) were graded twice to check consistency; that result
  will be reported with the second judge.
- **Pre-registration.** The questions, exam rules and model list were recorded locally by hash before each model's
  answers were collected; the sealed rubrics, the judge protocol and the analysis code before any test answer was
  graded. Later changes are recorded as amendments with their reasons. These records are private; their hashes are
  published here for the first time, so from today they show that the records do not change, but they cannot by
  themselves prove when the records were made.

### Scoring

An answer earns the points of each requirement it meets and loses the points of each error in its question's rubric
that it makes; its score is that total divided by the total points of the requirements, times 100, kept between 0 and
100. The judge protocol also has six general checks that apply to every answer (for example, citing a source that does
not exist); they are still drafts, so the judge recorded them but they do not count in these scores. A refused, failed
or disqualified answer scores 0.

## Caveats

- **The judge is also a contestant.** GPT-6 Astra graded every answer that had text and is also on the list, as are
  other GPT models;
  a judge may prefer answers like its own. The second judge (Claude Opus 5.5) and the rabbis' grading will show how much
  this matters.
- **The rubric writer is also a contestant.** Claude Fable 5.1 drafted every rubric, made every revision, decided which
  single-reviewer suggestions to accept, and also scored highest; Claude Opus 5.5, another contestant, checked the
  rubrics' sources. A rubric written by a model may favour that model's way of answering. The other two rubric
  reviewers, GPT-6 Astra and Gemini 4 Argon, are contestants too, and placed fourth and second.
- **Some models were added later.** Gemini 4 Argon, both Grok models, Claude Opus 4.8, Claude Sonnet 4.6, GPT-5.6 Sol,
  GPT-6 Sol and the three Muse Code models were added
  after the first results were published. Each was recorded as an amendment before its answers were collected, and was
  run on the same questions and graded with the same sealed rubrics and judge.
- **Not contamination-free.** Rabbinate questions often recur from earlier sittings, whose papers (and some unofficial
  answers) are online, and these 60 have not yet been checked for repeats. A model may have seen a close version of a
  question in training.
- **No rabbi has checked anything yet.** Rabbis will review the rubrics and grade a random sample of answers; their grades
  will correct the AI scores (prediction-powered inference), and the results will be called validated only if the AI
  judges agree with them well enough. Until then every number here is provisional.
- **Not a pass mark.** These scores are not a semicha exam grade, do not say whether a model "passes semicha", and are not
  authority to pasken.

## The bundle

[`bundle/`](bundle/) fixes, by hash, the data these results come from, without the exam text:

| File | What it is |
|---|---|
| `criteria.json` | Every criterion's id, points, axis and status (no criterion text) for all 96 sealed questions: the 60 test questions, and 36 development questions from the Iyar 5786 papers, which are not scored here. `approved` means approved by the AI review panel, not by a rabbi. It also lists the judge protocol's six general checks (status draft, not scored). |
| `commitments.json`, `seal-log.jsonl` | The salted commitments to all 96 sealed rubrics, and the hash-chained log that sealed them on 29 October 2026. |
| `prereg.json` | The SHA-256 of each pre-registration record. |
| `scores.json` | The judge's mean score per model. |
| `withheld.json` | The SHA-256 of the per-answer files: each answer's salted commitment, every verdict, and the 244 repeat gradings. |
| `MANIFEST.json` | The SHA-256 of every file. |
| `.gitattributes` | Keeps every file byte-exact on checkout, so the hashes match. |

Publishing every verdict now would let a rabbi who is grading blind match an answer to its model, so the per-answer
files wait for the end of the review round; `withheld.json` fixes them now. Until the code, the salts and the withheld
files are published, the bundle cannot be used to recompute a score or open a commitment: it fixes these files so that
any later change can be detected.

## Historical semicha reference track (proposal)

This fork proposes a separate **historical reference and calibration track**, with a 36-question pilot:
12 from the [Nisan 5765 Issur veHeter paper with answers](https://www.smicha.co.il/gallery/mivchanim_categories-17.doc),
12 across sittings in [Orel Shivni's Issur veHeter collection](https://www.smicha.co.il/gallery/mivchanim_categories-46.docx),
and 12 from [Adiel Kapach's Niddah collection](https://www.smicha.co.il/gallery/mivchanim_categories-42.pdf).
These are proposed allocations; no questions have been selected.

- **Included now:** the [source catalog](datasets/historical-reference/sources.json) and a
  [curation, rights and evaluation plan](docs/historical-reference.md), including the proposed item metadata.
- **Before Q&A release:** confirm reuse rights under the [site's terms](https://www.smicha.co.il/terms.php),
  verify question/answer alignment and citations, obtain rabbinic review, and audit duplicates and overlap.
  No source documents or Q&A text are copied here. The answers are attributed references, not verified official keys.
- **Separate reporting:** older public questions may have appeared in model training. This track would support
  calibration, not a claim of unseen-question performance. It adds no scores to the current leaderboard.

This proposed pilot is distinct from both the **60 Cheshvan 5787 test questions** and the **36 Iyar 5786 development
questions** already committed in `bundle/`. The bundle and original results are unchanged. No evaluation harness
or ingestion pipeline is supplied by this proposal, and upstream has not adopted it.

## Contact

halachabench@gmail.com. Anyone who would like to review the rubrics or grade answers is welcome to write. If you are
interested in collaborating on expanding the test (more papers, more models, more rabbinic review), please reach out at
the same address.

HalachaBench is an independent project, not connected to or endorsed by the Chief Rabbinate of Israel or by any model
developer; model names are their owners' trademarks.

<div dir="rtl">

## בעברית, בקצרה

מבחן HalachaBench בודק עד כמה מודלים של בינה מלאכותית (AI) יודעים לענות על שאלות אמיתיות ממבחני ההסמכה של הרבנות
הראשית לישראל. אלה תוצאות ראשונות של 27 מודלים על 60 השאלות של חמישה שאלונים ממועד חשוון תשפ"ז. כל מודל ענה על כל
שאלה שלוש פעמים, בעברית, בלי ספרים ובלי אינטרנט.

**התוצאות זמניות, והן אינן ציוני מבחן.** עד כה בדק את התשובות רק שופט ממוחשב אחד, GPT-6 Astra, שהוא גם אחד המודלים
הנבחנים. המחוונים נכתבו בידי Claude Fable 5.1, שקיבל את הציון הגבוה ביותר, ונבדקו בידי מודלי AI; אף רב עדיין לא עבר
עליהם, ואף רב עדיין לא בדק תשובה. שאלות רבות במבחני הרבנות חוזרות ממועדים קודמים, ועוד לא נבדק אילו מהשאלות כאן חוזרות, ולכן ייתכן שהמודלים ראו
שאלות דומות.
ב־2 בנובמבר נוספו חמישה מודלים: Gemini 4 Argon,‏ Grok 4.7,‏ Grok 4.3,‏ Claude Opus 4.8 ו־Claude Sonnet 4.6, וב־3 בנובמבר נוספו GPT-5.6 Sol
ו־GPT-6 Sol. ב־6 בנובמבר נוספו שלושה מודלים של Meta, דרך Muse Code:‏ Muse Wonder Full,‏ Muse Wonder ו־Muse Spark 1.3. עוד חמש הרצות רשומות עדיין חסרות, ויתווספו. הציונים אינם ציון במבחן הסמיכה, אינם קובעים
אם מודל "עובר את מבחני הסמיכה", ואין בהם היתר לסמוך על מודל בפסיקת הלכה.

כל מי שמעוניין לעבור על המחוונים או לבדוק תשובות, או לשתף פעולה בהרחבת המבחן, מוזמן לכתוב אל
halachabench@gmail.com. המיזם HalachaBench עצמאי:
אין לו קשר לרבנות הראשית לישראל, והוא אינו פועל מטעמה או בחסותה.

### הצעה במאגר המפוצל: מסלול ייחוס היסטורי

מוצע מסלול נפרד לכיול ולהערכה עתידית, עם פיילוט מתוכנן של 36 שאלות: 12 באיסור והיתר מניסן תשס״ה,
12 מאוסף התשובות של אוראל שיבני באיסור והיתר ממועדים שונים, ו־12 מאוסף התשובות של עדיאל קאפח בנידה.
טרם נבחרו שאלות. נוספו רק [קטלוג מקורות](datasets/historical-reference/sources.json)
ו[תוכנית עבודה](docs/historical-reference.md), ללא העתקת שאלות או תשובות.

לפני פרסום תוכן יש להסדיר זכויות שימוש, לאמת התאמה בין שאלות לתשובות ומראי מקומות, לבצע בדיקה רבנית
ולבדוק כפילויות וחפיפה. התשובות הן מקורות ייחוס מיוחסים, ולא מפתחות רשמיים שאומתו.
אלה חומרים פומביים שעלולים להופיע בנתוני האימון; תוצאותיהם יוצגו בנפרד.
הפיילוט אינו 36 שאלות הפיתוח מאייר תשפ״ו ואינו משנה את 60 שאלות המבחן מחשוון תשפ״ז, את הציונים או את החבילה החתומה.
זו הצעה של המאגר המפוצל, שטרם אומצה על ידי הפרויקט המקורי; אין כאן מנגנון הרצה חדש.

</div>
