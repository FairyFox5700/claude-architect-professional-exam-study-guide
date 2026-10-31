# Objective 32: Communicate Architectural Decisions and Trade-Offs

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Communicate architectural decisions and trade-offs through architecture decision records, technical design documentation, diagrams, cost/benefit explanations, risk communication to non-technical stakeholders, alternative comparisons, technology justification, and scalability/performance implications.

---

### Q1.
An architect chooses Claude with a retrieval-augmented generation (RAG) pipeline over fine-tuning for a healthcare documentation assistant. What is the best way to formally capture this decision for future engineers?

A. A verbal explanation in the project kickoff meeting
B. An Architecture Decision Record (ADR) stating the context, decision, alternatives considered, and consequences
C. A comment in the codebase repository README
D. An email to the project sponsor

**Answer:** B
**Explanation:** ADRs are the standard, durable artifact for recording the context, alternatives, and rationale behind architectural choices so future teams understand why a decision was made. Verbal explanations, code comments, and emails are not structured, discoverable, or long-lived.

### Q2.
A manufacturing client's CFO asks why the proposed Claude-based quality-inspection assistant costs more than a traditional rules engine. What is the best communication approach?

A. Show only the technical architecture diagram and let the CFO infer the cost rationale
B. Explain the cost in terms of the business value delivered (reduced defect escape rate, labor savings) versus the rules engine's lower accuracy and higher maintenance burden
C. Tell the CFO that cost comparisons are an engineering concern
D. Downplay the cost difference to avoid a difficult conversation

**Answer:** B
**Explanation:** Non-technical stakeholders need costs translated into business outcomes and trade-offs they can weigh, not raw technical detail or evasion. Options A, C, and D fail to give the CFO the information needed for a sound business decision.

### Q3.
An architect must explain to a retail company's board why a multi-agent Claude architecture was chosen over a single large prompt for inventory forecasting. Which explanation is MOST appropriate for a non-technical board?

A. "We used orchestrated sub-agents with tool-calling and a supervisor pattern for context window optimization"
B. "We split the problem into specialized steps — demand analysis, supply constraints, and recommendations — so each part is more accurate and easier to verify, much like having specialists instead of one generalist"
C. "It's a standard design pattern recommended by Anthropic"
D. "The architecture is proprietary and cannot be explained"

**Answer:** B
**Explanation:** Translating technical patterns into relatable, business-oriented analogies communicates the trade-off (accuracy/verifiability vs. simplicity) in terms a board can evaluate. Option A is too technical, C is an appeal to authority without substance, and D avoids transparency.

### Q4.
A legal services firm is comparing Claude against a competing LLM vendor for contract review. The architect's comparison document should primarily focus on which of the following to support a sound decision?

A. Marketing claims from each vendor
B. A structured comparison of accuracy on representative legal tasks, cost per document, data residency/compliance posture, and integration effort
C. Which vendor has the most press coverage
D. Personal preference of the lead engineer

**Answer:** B
**Explanation:** A sound technology comparison evaluates measurable, decision-relevant criteria tied to the firm's actual requirements. Marketing claims, press coverage, and personal preference are not defensible bases for an architectural decision.

### Q5.
A telecom company's operations team is concerned that a new Claude-based network-incident-summarization tool might scale poorly during a major outage when ticket volume spikes 50x. How should the architect communicate the scalability design?

A. Assure them nothing will ever go wrong
B. Explain the specific scaling strategy (e.g., request queuing, rate-limit handling, graceful degradation) and the tested or expected behavior under peak load, including what happens if capacity is exceeded
C. State that Claude is "infinitely scalable" so there is no concern
D. Avoid the topic since it might alarm stakeholders

**Answer:** B
**Explanation:** Credible scalability communication requires concrete mechanisms and honest boundary conditions, not blanket reassurance or avoidance. Overstating capability (A, C) damages trust when reality diverges from promises.

### Q6.
An architect is documenting a decision to use a smaller, faster Claude model for a real-time insurance quote assistant instead of the largest available model. Which trade-off explanation best belongs in the ADR?

A. "We like the smaller model better"
B. "The smaller model meets the 2-second latency SLA required for real-time quoting; the larger model's higher accuracy on edge cases was outweighed by its ~4x latency, which violates the SLA"
C. "The smaller model is cheaper, so no further analysis was needed"
D. "Anthropic recommended the smaller model"

**Answer:** B
**Explanation:** A strong ADR trade-off statement ties the decision to a measurable constraint (the SLA) and quantifies what was given up and why it was acceptable. The other options lack the reasoning and evidence an ADR requires.

### Q7.
A government agency's non-technical steering committee asks the architect to explain the risk of "hallucination" in an AI assistant that answers policy questions. What is the best communication approach?

A. Use the term "hallucination" without further explanation, assuming it is well known
B. Explain in plain language that the model can generate plausible-sounding but incorrect answers, describe the specific mitigation (e.g., citation requirements, retrieval grounding, human review for high-stakes answers), and quantify observed error rates from testing
C. State that hallucination is a solved problem with modern models
D. Recommend the committee not worry about it since Anthropic handles safety

**Answer:** B
**Explanation:** Explaining risk to non-technical stakeholders requires plain language, a concrete description of impact, and the specific mitigations in place with supporting evidence. Jargon without explanation (A), claiming the problem is solved (C), and deflecting responsibility (D) all undermine informed decision-making.

### Q8.
Which artifact is MOST appropriate for visually communicating how data flows between a customer's CRM, Claude, and a human-review queue to both engineers and business stakeholders?

A. A verbal walkthrough only
B. An architecture/data-flow diagram showing systems, data direction, and decision points
C. A raw JSON schema file
D. The vendor's generic marketing diagram

**Answer:** B
**Explanation:** Diagrams are the standard way to make system relationships and data flow legible to mixed technical/business audiences. JSON schemas and generic marketing diagrams don't represent the specific solution, and verbal-only explanations aren't durable or shareable.

### Q9.
A finance firm's risk committee wants to understand why the architect rejected an alternative of using Claude with no guardrails for autonomous trade-recommendation generation. What should the architect's explanation emphasize?

A. That guardrails are always required by Anthropic's terms of service
B. The specific business risk (unreviewed autonomous trades causing financial or regulatory harm) and how the chosen design (human approval gate, confidence thresholds) mitigates it compared to the rejected alternative
C. That the rejected alternative was simply "not best practice"
D. Nothing — the decision doesn't need justification to the risk committee

**Answer:** B
**Explanation:** Justifying a rejected alternative to a risk committee requires concretely connecting the alternative's risk to business/regulatory consequences and showing how the chosen design mitigates it. Vague appeals to best practice (C) or terms of service (A) don't address the committee's actual concern, and skipping justification (D) undermines stakeholder trust.

### Q10.
An architect is asked to justify choosing Claude over an in-house-trained smaller model for a logistics company's route-exception-handling assistant. Which justification is strongest?

A. "Claude is newer"
B. "Claude's reasoning on exception cases outperformed the in-house model in our benchmark by a measurable margin, and in-house training would require 6 months and a dedicated ML team the client doesn't have"
C. "Everyone uses Claude now"
D. "Our engineers prefer working with Claude's API"

**Answer:** B
**Explanation:** A defensible technology justification cites measured performance differences and concrete resource/time trade-offs relevant to the client's situation. Popularity (A, C) and engineer preference (D) are not substantive justifications for a client-facing architecture decision.

### Q11.
When documenting technical design for a SaaS company's AI-powered analytics copilot, what should an ADR's "Consequences" section primarily capture?

A. A list of all possible future features
B. The resulting benefits as well as the accepted downsides/risks of the chosen approach, including what becomes harder to change later
C. The names of everyone who attended the design meeting
D. The marketing copy for the feature launch

**Answer:** B
**Explanation:** The Consequences section of an ADR documents both the positive and negative downstream effects of the decision, including constraints it creates — this is the record's core value. Attendee lists and marketing copy do not belong in an ADR.

### Q12.
A hospital executive asks the architect to compare "build vs. buy" for a clinical-documentation Claude integration. What should the comparison transparently include?

A. Only the upfront licensing cost
B. Total cost of ownership (build effort, maintenance, compliance validation) versus vendor cost, time-to-value, and long-term flexibility trade-offs for each option
C. Only the vendor's claimed accuracy numbers
D. A recommendation with no supporting rationale

**Answer:** B
**Explanation:** A credible build-vs-buy comparison weighs total cost of ownership, time-to-value, and flexibility on both sides, not a single cherry-picked metric. Presenting a bare recommendation (D) without rationale fails the stakeholder's need to understand the trade-off.

### Q13.
An architect presents two alternative architectures to a manufacturing client: (1) on-premises deployment for data sovereignty, and (2) cloud deployment for faster scaling. How should the trade-off be framed to the client's leadership?

A. Recommend cloud only, since it is technically superior in all cases
B. Present both options' implications for compliance, cost, latency, and scaling, and let leadership weigh the trade-off against their regulatory and growth priorities
C. Let the engineering team decide without stakeholder input
D. Present only the option the architect personally prefers

**Answer:** B
**Explanation:** When a decision hinges on business priorities (regulatory posture vs. growth speed) rather than purely technical merit, the architect's role is to present trade-offs clearly and let the accountable stakeholders choose. Unilaterally picking an option without the full trade-off (A, D) or excluding stakeholders (C) are poor practice.

### Q14.
A telecom's engineering director asks why a proposed Claude-based customer-churn-prediction assistant uses a streaming response pattern instead of a batch pattern. What is the best explanation?

A. "Streaming is more modern"
B. "Streaming lets agents see partial results within 1-2 seconds, meeting the real-time call-handling requirement identified in discovery, whereas batch processing would take 30+ seconds per case"
C. "We always use streaming by default"
D. "Batch processing is deprecated"

**Answer:** B
**Explanation:** The strongest explanation ties the technical choice directly back to a discovered business/operational requirement (real-time agent support) with a quantified comparison. The other answers are unsubstantiated generalities.

### Q15.
A law firm asks the architect to explain, in a design document intended for both partners and IT staff, the performance implications of expanding the context window used for contract analysis. What should the document include?

A. Only the token limit number with no explanation
B. A plain-language explanation that larger context improves completeness of analysis on long contracts but increases latency and cost per request, with benchmark figures for both
C. A statement that larger context windows have no downsides
D. Omission of performance implications to keep the document short

**Answer:** B
**Explanation:** Good technical design documentation for a mixed audience explains both the benefit and the cost of a configuration change in plain language, backed by data. Claiming no downsides (C) or omitting implications entirely (D) misleads readers responsible for approving the design.

### Q16.
An architect must brief both a hospital's executive sponsor and the engineering team that will build the approved design for a new Claude-based triage assistant, in a single document. How should the briefing be structured?

A. Give both audiences identical depth and detail throughout the entire document
B. Lead with the decision and its business consequence for the sponsor, then descend into the technical rationale and constraints the engineering team needs to implement faithfully
C. Write only for the engineers, since the sponsor already approved the budget verbally
D. Write only for the sponsor, and let engineers infer the rationale from the final design diagram

**Answer:** B
**Explanation:** A well-sequenced briefing descends from the decision and its business impact (what the sponsor must act on) into the technical rationale (what engineers need to build it faithfully), letting each reader stop at the depth they need. Flattening both into equal depth (A) forces each audience to wade through irrelevant material, and serving only one audience (C, D) leaves the other without what they need to approve or implement correctly.

### Q17.
A project team is under pressure to shorten a lengthy ADR for a retail client's inventory-forecasting system before it goes into the shared knowledge base. Which section should the team protect from being cut, even at the cost of trimming other content?

A. The list of meeting attendees
B. The rejected alternatives and the reasoning for why they were not chosen
C. The formatting template used for the document
D. The marketing description of the feature for the launch announcement

**Answer:** B
**Explanation:** Removing the rejected alternatives to save space is a known anti-pattern: without them, a future reader cannot tell whether a path was deliberately weighed and rejected or simply never considered, and the team ends up re-litigating settled ground. Attendee lists, templates, and marketing copy (A, C, D) are packaging, not substance, and can be trimmed without losing decision-making value.

### Q18.
An architect's evaluation results clearly contradict a model-selection decision that the client's VP has already announced publicly to the organization. What should the architect do?

A. Proceed with implementation quietly while privately holding the contrary evidence
B. Present the contradicting evidence directly to the VP, who owns the decision, and let the VP decide how to proceed with full information
C. Override the VP's decision unilaterally and switch to the model the evaluation supports
D. Withdraw from the engagement rather than raise the disagreement

**Answer:** B
**Explanation:** The architect's responsibility is to ensure the accountable decision-maker is fully informed, not to conceal the discrepancy (A), seize authority that isn't theirs (C), or avoid the conversation entirely (D). Surfacing the evidence while leaving the decision with its owner respects accountability while still protecting the organization from an uninformed choice.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
