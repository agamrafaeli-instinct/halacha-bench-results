# Historical semicha reference track (proposal)

**Status: metadata-only proposal.** This fork proposes a separate historical reference and calibration track,
`historical-semicha-v0`, for future benchmarking. No questions, answer texts, rubrics, model runs or scores are
released by this change. No items have been selected or cleared for redistribution.

The published HalachaBench v1 results still cover the original 60 Cheshvan 5787 test questions. The proposed
36-question pilot is also **different from the existing 36 Iyar 5786 development questions** in `bundle/`.
This proposal does not change that bundle, its commitments, the original pre-registration or the leaderboard,
and has not been adopted or endorsed by upstream HalachaBench or the Chief Rabbinate.

## Why use historical material?

Published worked answers can help reviewers compare reference coverage, check citations, identify repeated
questions and calibrate grading. They can also help test extraction and Hebrew transcription before a larger
release. They should be treated as attributed reference answers that need review, not automatically as an
official answer key or the only acceptable halakhic position.

Because these materials are public and older than many models, this track cannot establish performance on
unseen questions. Use it for reference-based evaluation and calibration, and report it separately from fresh
or held-out exam results. An independent later-sitting track would need its own contamination audit.

## Candidate sources and pilot allocation

The machine-readable [source catalog](../datasets/historical-reference/sources.json) records URLs, attributed
authors, subject, exam-date scope, format, source-file hashes, rights status and proposed counts. These are source records, not
benchmark items. Attributions were checked against the site's [Issur veHeter listing](https://www.smicha.co.il/mivchanim_categories.php?it=2)
and [Niddah listing](https://www.smicha.co.il/mivchanim_categories.php?it=6) on 7 November 2026.

| Candidate | Attribution and scope | Proposed pilot |
|---|---|---:|
| [Nisan 5765 Issur veHeter paper with answers](https://www.smicha.co.il/gallery/mivchanim_categories-17.doc) | The site attributes the questions and answers to Rabbi Yitzchak Oshinsky. The document header also credits Rabbi Zechariah Tovi as an editor. Preserve these distinct roles; this is not evidence of an official institutional answer key. | 12 questions |
| [Issur veHeter answer collection](https://www.smicha.co.il/gallery/mivchanim_categories-46.docx) | Attributed by the site to Orel Shivni (אוראל שיבני). The inspected document covers 5780–5786. Select across sittings, after mapping each answer to its exact question. | 12 questions |
| [Niddah answer collection](https://www.smicha.co.il/gallery/mivchanim_categories-42.pdf) | Attributed by the site to Adiel Kapach (עדיאל קאפח). The first sitting is Cheshvan 5780; complete sitting coverage and question-to-answer alignment still need an inventory. | 12 questions |
| **Total** | **24 Issur veHeter + 12 Niddah** | **36 proposed questions** |

Counts are allocation targets, not verified unique or eligible item counts. A numbered multipart exam question
counts as one item, with all subparts retained. Do not cherry-pick easier subparts. If a bucket has fewer than
12 eligible duplicate families, report the shortfall and revise the proposal before running models.

For each bucket, first inventory eligible items; balance topic, reasoning demand, subpart structure and citation
density. Use a recorded seed to sample within those strata. Publish selected item IDs and exclusions, and freeze
the selection, scoring rules and model settings before collecting answers. No scores may guide selection.

## Rights gate before copying or releasing text

The site's [terms, clauses 8–10](https://www.smicha.co.il/terms.php) restrict use to personal use, require full
attribution and reserve rights to contributors. Public availability is not a redistribution license.

Keep this contribution link-and-metadata only. Before ingesting, adapting or publishing Q&A, obtain and record
permission or another verified legal basis for both the exam questions and contributed answers. Check whether
it covers benchmark use, redistribution, derivative rubrics and third-party model/API processing. One permission
may not cover all rights holders. Attribution alone does not clear those rights. Do not commit source documents,
OCR text, excerpts or paraphrased answer datasets while clearance is pending.

Record the rights holder, permission evidence/reference, allowed uses, required attribution, restrictions and
review date for each source and item. Sensitive correspondence should remain private; publish only an appropriate
permission reference. A permission request is a later task, not something this proposal claims has been sent.

## Proposed item metadata contract

The following is a design for a later, rights-cleared release, not a claim that records already exist:

| Field | Meaning |
|---|---|
| `id`, `track`, `dataset_version` | Stable ID, the historical track name, and immutable release version. |
| `source_id`, `source_url`, `source_sha256`, `retrieved_at` | Link to the catalog plus a pinned authorized source version. Hashes identify bytes; they do not grant rights. |
| `author`, `attribution`, `answer_provenance` | Credited question/answer authors and editors, with role and evidence. Use `contributed_reference`; use `official_key` only with verified institutional evidence. |
| `subject`, `topic_tags`, `exam_date_hebrew`, `exam_date_iso` | Exam subject, topics and sitting. Leave an unverified Gregorian date null rather than inferring an exact day from a month. |
| `question_number`, `subparts`, `question_locator`, `answer_locator` | Original item number and exact page/section locators for each side, including where questions must be sourced separately. |
| `question_he`, `reference_answer_he`, `citations` | Rights-cleared Hebrew text and structured references; preserve an original transcription separately from normalized matching text. |
| `rights_status`, `permission_reference`, `allowed_uses` | Item-level clearance and restrictions. A source-level decision cannot silently clear another author's text. |
| `review_status`, `reviewers`, `reviewed_at`, `review_notes` | Transcription and rabbinic review evidence; unresolved disputes or missing citations remain explicit. |
| `rubric`, `accepted_views`, `rubric_version` | Reviewed criteria, source-grounded alternative positions and version. A worked answer is evidence, not an exhaustive rubric. |
| `duplicate_family_id`, `overlap_status`, `related_item_ids`, `split` | Cross-source duplicates, overlap with original test/development sets, and the family-level partition. |
| `exposure_status`, `earliest_known_public_date`, `exposure_evidence` | Known public availability and evidence; use unknown where the first public date is unverified. |

## Curation and evaluation protocol

1. **Clear rights and inventory.** Confirm attribution and version, enumerate sittings, and align each worked answer
   to a complete question. A collection of answers is not necessarily a complete collection of exam prompts.
2. **Check transcription.** Independently transcribe/compare against the authorized source, including Hebrew
   abbreviations, footnotes, citations and all subparts. Preserve edits and their reasons. Quarantine uncertain items.
3. **Review substance.** Have qualified rabbinic reviewers verify references, scope, reasoning and accepted
   alternative rulings. Record adjudication and unresolved disagreement. Do not describe unreviewed material as gold.
4. **Audit overlap.** Compare exact text and normalized Hebrew, then review near-duplicates and shared cases across
   all three collections. Group repeated questions and substantive variants into one duplicate family. Compare
   with both the 60 Cheshvan 5787 test items and the 36 Iyar 5786 development items when authorized text is available.
   Hash-only bundle records cannot establish textual non-overlap. Until checked, mark overlap `unknown`.
5. **Partition by family.** Keep a family in only one development/calibration/evaluation split. Exclude known overlap
   from any proposed new holdout; retain it only in clearly labeled overlap analyses. No split of public historical
   material should be called contamination-free. Report counts before and after deduplication and exclusions.
6. **Freeze before evaluation.** Version the item manifest, rights record, reviewed rubrics, split and evaluation plan.
   Keep reference answers out of closed-book model prompts. If retrieval/open-book runs are later added, register
   and report those as a different condition.
7. **Report separately.** Publish historical-track results by subject and source, with sample sizes, exclusions,
   judge/rabbi agreement and uncertainty. Distinguish source coverage from correctness and accepted alternatives.
   Do not pool scores with the existing leaderboard or interpret them as semicha pass/fail grades or practical psak.

## Acceptance checklist for a later dataset PR

- [ ] Maintainers agree on scope and the provisional 12/12/12 allocation.
- [ ] Rights and permitted processing are recorded for every question and answer.
- [ ] Every selected item has stable source/question/answer locators and verified attribution.
- [ ] Hebrew transcription and citations are checked; rabbinic review status is explicit.
- [ ] Duplicate families and overlap with existing development/test sets are reviewed.
- [ ] Selection, splits, rubrics and evaluation settings are versioned before model runs.
- [ ] Release documentation labels public exposure and distinguishes historical scores from v1.

This repository publishes results and commitments, not a runnable evaluation harness. The steps above describe
future work; this PR adds no runner, automatic ingestion, training data or benchmark integration.

## Validation for this metadata-only proposal

Run `python -m unittest discover -s tests -v` from the repository root. The checks validate the source catalog,
pilot totals, local documentation links and the bilingual Pages section. They do not evaluate models or prove
rights clearance, answer correctness, contamination status or source availability.
