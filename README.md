# Claude Certified Architect – Professional (CCAR-P): Exam Study Guide

A community-style study guide built from the 7 official exam domains and 38
task-area objectives of the *Claude Certified Architect – Professional (CCAR-P)*
certification blueprint — Anthropic's advanced certification for professionals
who design, integrate, secure, evaluate and operate Claude-based solutions at
enterprise scale. Domains are grouped by blueprint weighting, each with
10–22 certification-style multiple-choice practice questions, answers, and
explanations.

**Total: 137 domain-level practice questions** across all 7 domains.

For deeper, focused practice, every individual task-area objective also has
its own dedicated page: see the
**[Objectives Index](docs/objectives/README.md)** (38 pages, 640 questions).

**Grand total: 777 practice questions**, including supplementary questions added
after cross-referencing other independently published CCAR-P study materials to
close topic gaps (see [Acknowledgements](#acknowledgements)).

## Domains

| # | Domain | Weight | Objectives covered | Questions |
|---|--------|--------|---------------------|-----------|
| 1 | [Solution Design & Architecture](docs/01-solution-design-and-architecture.md) | 17% | 1–6 | 21 |
| 2 | [Claude Models, Prompting & Context Engineering](docs/02-claude-models-prompting-and-context-engineering.md) | 13% | 7–11 | 18 |
| 3 | [Integration](docs/03-integration.md) | 19% | 12–19 | 25 |
| 4 | [Evaluation, Testing & Optimization](docs/04-evaluation-testing-and-optimization.md) | 16% | 20–25 | 21 |
| 5 | [Governance, Safety & Risk Management](docs/05-governance-safety-and-risk-management.md) | 14% | 26–30 | 19 |
| 6 | [Stakeholder Communication & Lifecycle Management](docs/06-stakeholder-communication-and-lifecycle-management.md) | 14% | 31–35 | 19 |
| 7 | [Developer Productivity & Operational Enablement](docs/07-developer-productivity-and-operational-enablement.md) | 7% | 36–38 | 12 |

Integration, Solution Design & Architecture, and Evaluation/Testing/Optimization
together represent 52% of the exam blueprint and have the deepest coverage here.

## Per-objective pages

For deeper, focused practice, every individual task-area objective also has
its own dedicated page: see the
**[Objectives Index](docs/objectives/README.md)** (38 pages, 640 questions).

## PDF versions

Every page above can also be rendered as a branded, print-ready PDF (Manrope
typeface, navy/peach/orange color palette) using [`build_pdfs.py`](build_pdfs.py),
which mirrors the same folder structure under `pdf/`:

- `pdf/README.pdf`
- `pdf/docs/` — the 7 domain pages
- `pdf/docs/objectives/` — all 38 objective pages + index

## How to use this guide

- Each page is self-contained: question, four answer options (A–D), the
  correct answer, and a short explanation of why it's correct (and why the
  others aren't).
- Work through a domain, then revisit only the questions you got wrong.
- Domain weights, task-area wording, and exam structure come from the
  published CCAR-P exam blueprint (63 questions, 120 minutes, 720/1,000
  passing score, 12-month validity).

## Exam structure reference

| Characteristic | Details |
|---|---|
| Certification | CCAR-P |
| Questions | 63 |
| Duration | 120 minutes |
| Question types | Multiple choice and multiple response |
| Passing score | 720 / 1,000 scaled |
| Validity | 12 months |
| Prerequisite | No mandatory Foundations certification |

## Disclaimer

This is an independent, community-authored study aid and is not affiliated
with, endorsed by, or sponsored by Anthropic. It is generated from the
publicly described CCAR-P exam blueprint for self-study purposes only.

## Source

Generated from the published *Claude Certified Architect – Professional
(CCAR-P)* exam blueprint's 7 competency domains and 38 task-area objectives.

## Acknowledgements

After the initial 685-question draft, we cross-referenced several other
independently published, unofficial CCAR-P study resources purely to identify
*topic coverage gaps* (concepts/scenarios our set didn't yet test) — no text
was copied from these sources, only topic ideas that informed new original
questions:

- [vkorost/claude-certified-architect-professional-guide](https://github.com/vkorost/claude-certified-architect-professional-guide)
- [Amey-Thakur/CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS)
- [EnkrateiaLucca/claude-architect-pro-cert](https://github.com/EnkrateiaLucca/claude-architect-pro-cert)
- [preporato/claude-certification-guide](https://github.com/preporato/claude-certification-guide)
- [sarveshtalele/claude-architect-exam-guide](https://github.com/sarveshtalele/claude-architect-exam-guide)
- [juanmartincoma-collab/claude-certified-architect-es](https://github.com/juanmartincoma-collab/claude-certified-architect-es)

92 additional original questions were added across all 38 objective pages and
7 domain pages as a result, covering gaps such as prompt-cache breakpoint
mechanics, MCP vs. Agent Skill decision criteria, token-passthrough auth
anti-patterns, optional-stopping bias in A/B tests, sycophancy as a distinct
failure mode, and settings-precedence/fail-closed behavior in Claude Code.
