# Objective 2: Design End-to-End Architectures

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design complete end-to-end architectures that trace the full lifecycle from input through processing to output and feedback, clearly identifying where Claude, backend services and human reviewers each participate, incorporating validation and error-handling paths at every stage, and closing the loop with feedback mechanisms that improve future system performance.

---

### Q1.
An architect is designing a system for a bank that processes loan applications. Which design correctly reflects a complete end-to-end lifecycle?

A. Claude reads the application and immediately returns an approval decision to the customer
B. Intake validates document completeness deterministically, Claude extracts and normalizes applicant data, a deterministic underwriting engine applies lending rules, a human underwriter reviews edge cases, and outcomes are logged to retrain the extraction prompts
C. Claude performs intake, decisioning and customer notification in a single call with no logging
D. A human manually performs every step and Claude is used only for formatting the final letter

**Answer:** B
**Explanation:** This option traces input (document intake) through processing (extraction, rule-based underwriting, human review of exceptions) to output (decision) and feedback (logged outcomes improving future prompts), matching a complete, auditable lifecycle. A and C collapse decisioning into a single ungoverned step, and D underuses Claude for a task it is well suited to (extraction).

### Q2.
A healthcare provider's clinical documentation assistant occasionally produces summaries with incorrect medication dosages extracted from handwritten notes. Where should validation be added in the end-to-end design?

A. Only at the very end, by having the patient verify dosages
B. Immediately after Claude's extraction step, cross-checking extracted dosage values against a structured pharmacy database before the summary is finalized
C. Nowhere, since Claude's extraction is already highly accurate
D. Before the input is sent to Claude, by validating the handwriting quality of the scanned note

**Answer:** B
**Explanation:** Validation should occur as close as possible to the point where an error is introduced, so cross-referencing extracted dosages against an authoritative structured source immediately after extraction catches mistakes before they propagate into the finalized summary. A pushes a safety-critical check too late, C ignores a known failure mode, and D does not actually validate dosage correctness.

### Q3.
A telecom company's architecture routes customer chat messages to Claude for intent classification, then to a backend fulfillment API. During a peak outage, the fulfillment API becomes unavailable. What is the BEST error-handling design?

A. Let the conversation fail silently with no customer-facing message
B. Retry the fulfillment call indefinitely in a tight loop
C. Catch the failure, inform the customer transparently, log the incident, and offer a fallback path such as a callback request or human escalation
D. Have Claude guess a plausible fulfillment outcome and present it as successful

**Answer:** C
**Explanation:** Graceful degradation that is transparent to the user and provides a fallback preserves trust and operational continuity during backend failures. A harms user experience, B risks cascading failures and wasted cost, and D is dangerous because it fabricates a false success state.

### Q4.
In an end-to-end architecture for an e-commerce returns process, where should a human reviewer MOST appropriately be placed?

A. Reviewing every single return request regardless of value or risk
B. Reviewing only high-value or policy-ambiguous return requests flagged by deterministic business rules after Claude has classified the return reason
C. Reviewing nothing, since Claude's classification is always trustworthy
D. Reviewing the system's infrastructure logs instead of return requests

**Answer:** B
**Explanation:** Targeting human review at genuinely ambiguous or high-risk cases, identified through deterministic thresholds applied after classification, is the efficient placement of scarce human attention within the lifecycle. A wastes human capacity on low-risk routine cases, C removes a necessary safety net, and D misapplies review effort to the wrong artifact.

### Q5.
A manufacturing client wants its defect-detection pipeline to improve over time. Which feedback loop design is MOST effective?

A. Collect human-corrected labels when reviewers override Claude's classification, and periodically use this corrected dataset to refine prompts, examples or fine-tuning
B. Re-run the exact same prompt on the same images every quarter
C. Allow Claude to silently update its own instructions after every session
D. Discard all review history to keep storage costs low

**Answer:** A
**Explanation:** Capturing human corrections creates a structured, labeled signal that can systematically improve prompts or few-shot examples, closing the feedback loop with evidence rather than guesswork. B produces no new information, C is not a real capability and would be unsafe if it were, and D destroys the very data needed for improvement.

### Q6.
An architect is mapping an insurance claims system and must decide where backend services, rather than Claude, should own a step. Which step is the BEST candidate for a backend service rather than Claude?

A. Interpreting an ambiguous written accident description
B. Looking up the policyholder's current coverage limits from the policy database
C. Summarizing an adjuster's lengthy notes for a manager
D. Drafting a plain-language explanation of a coverage decision

**Answer:** B
**Explanation:** Looking up an exact value from a system of record is a deterministic data-retrieval operation best handled by a backend service call, not language generation. The other three tasks require natural-language interpretation or generation, which are Claude's strengths.

### Q7.
A government agency's end-to-end design includes Claude drafting responses to public records requests. Which validation step is MOST important before the response leaves the system?

A. A spell-check pass only
B. A deterministic check or human reviewer confirming no exempted/confidential information is disclosed, per statutory redaction rules
C. A check that the response uses a friendly tone
D. A check that the response is under 500 words

**Answer:** B
**Explanation:** For public records requests, inadvertent disclosure of exempted information carries legal consequences, making a redaction compliance check the critical validation gate before release. The other checks are stylistic and immaterial to legal risk.

### Q8.
Which of the following BEST describes the "processing" stage responsibilities in an end-to-end architecture for an airline rebooking assistant?

A. Only Claude's language generation, with no other systems involved
B. A combination of Claude interpreting the disruption and customer preferences, backend flight-availability and fare-rule services supplying authoritative data, and orchestration logic deciding when to escalate to a human agent
C. Only the backend flight system, with Claude used solely for the final greeting message
D. A single monolithic Claude call that also manages flight inventory state directly

**Answer:** B
**Explanation:** Robust processing stages typically blend LLM reasoning with authoritative backend data and orchestration logic for escalation, each playing to its respective strength. A and C over-concentrate responsibility in one component, and D is architecturally unsound since Claude should not directly own transactional inventory state.

### Q9.
A SaaS company notices that its end-to-end support architecture has no mechanism to detect when Claude repeatedly fails to resolve a category of ticket. What should the architect add?

A. A monitoring and feedback layer that tracks resolution outcomes by category and flags recurring failure patterns for prompt or workflow review
B. A larger context window
C. A second unrelated Claude call to double-check the first call's output with no shared context
D. A policy that silently closes unresolved tickets after 24 hours

**Answer:** A
**Explanation:** Closing the lifecycle loop requires observability into outcomes, and category-level failure tracking enables targeted architecture or prompt improvements rather than guesswork. B does not address the root issue, C adds cost without structured insight, and D hides the problem instead of surfacing it.

### Q10.
In designing a legal document review pipeline, where does input validation MOST appropriately belong?

A. Only after the final output is generated
B. At intake, confirming the uploaded document is a supported format, is not corrupted, and contains the expected document type before any Claude processing begins
C. Nowhere, since Claude can handle malformed input gracefully
D. Only in the feedback loop, after a human has already reviewed the output

**Answer:** B
**Explanation:** Validating inputs at intake prevents wasted processing cost and downstream errors caused by malformed or unexpected documents, which is a foundational error-handling practice. The other options defer or omit a check that should happen as early as possible.

### Q11.
A retail company's architecture has Claude generating product descriptions from supplier spec sheets, with no review before publishing to the live storefront. A factually incorrect description causes a customer complaint. What end-to-end design gap does this reveal?

A. Claude's context window was too small
B. Missing an output validation/review gate between generation and publication, such as automated fact-checking against the spec sheet or human spot-checks
C. The supplier spec sheet format was inconsistent
D. The product catalog database was too large

**Answer:** B
**Explanation:** This incident exposes a missing validation stage between Claude's output and the irreversible action of publishing, which should have caught factual inconsistencies before customer-facing exposure. The other options may be contributing factors but do not address the core architectural gap of an absent review gate.

### Q12.
Which statement BEST captures the role of "feedback loops" in end-to-end Claude architecture design?

A. Feedback loops are optional polish that can be added after launch if time permits
B. Feedback loops are mechanisms that capture real-world outcomes and corrections to systematically improve future prompts, tools or routing decisions
C. Feedback loops exist only to satisfy compliance audit requirements
D. Feedback loops refer exclusively to user satisfaction surveys

**Answer:** B
**Explanation:** Feedback loops are a structural component that convert operational experience into measurable improvement, which is a core architectural responsibility rather than a cosmetic addition. A undervalues their importance, and C and D narrow the concept incorrectly.

### Q13.
An architect is designing a manufacturing predictive-maintenance assistant. Sensor data streams in continuously, and Claude is used to generate human-readable maintenance recommendations. Where should Claude sit in the pipeline?

A. Directly ingesting raw high-frequency sensor streams and performing signal processing itself
B. Downstream of a deterministic anomaly-detection service, consuming summarized anomaly events and generating contextualized, actionable recommendations for technicians
C. Replacing the anomaly-detection service entirely since Claude can interpret any data format
D. Upstream of data collection, deciding which sensors to install

**Answer:** B
**Explanation:** High-frequency signal processing is a deterministic, computationally specialized task unsuited to an LLM; Claude adds the most value synthesizing already-summarized anomaly events into clear human guidance. A and C misapply Claude to a role it is poorly suited for, and D is unrelated to the data pipeline.

### Q14.
A logistics company's end-to-end architecture has a step where Claude generates a shipment exception report, and a human dispatcher acts on it. The dispatcher frequently complains the reports omit root-cause context already available in the warehouse management system. What is the BEST fix?

A. Instruct the dispatcher to accept incomplete reports
B. Enrich Claude's input context by integrating warehouse management system data into the prompt or retrieval step before report generation
C. Remove the human dispatcher from the workflow entirely
D. Increase the frequency of report generation without changing its content

**Answer:** B
**Explanation:** The complaint traces to an input-stage gap — Claude lacks access to relevant context — so the fix is to enrich the input/retrieval stage, directly addressing root cause. A ignores a legitimate process gap, C removes a necessary human decision point, and D does not solve the content problem.

### Q15.
Which architecture best demonstrates proper separation of concerns across the input, processing, output and feedback stages for a multinational insurer's customer email triage system?

A. One Claude call handles classification, drafting, sending and logging immutably, with no stage boundaries
B. Input validation checks email format and language detection; Claude classifies intent and drafts a response; a deterministic policy engine checks compliance disclaimers; a human reviews flagged cases; and all outcomes feed a logging store used for quarterly prompt tuning
C. Humans handle every email manually, with Claude used only to count daily email volume
D. Claude both drafts and auto-sends every email without compliance checks to maximize speed

**Answer:** B
**Explanation:** This design cleanly separates each lifecycle stage, places deterministic compliance checks where they belong, targets human review at flagged cases, and closes the loop with logged outcomes for improvement — a complete, well-architected lifecycle. A collapses all stages into one ungoverned call, C underutilizes Claude, and D removes a necessary compliance safeguard for speed.

### Q16.
A pharmaceutical company's end-to-end design hands a sales team the ability to pass a "selected competitor product" identifier to Claude so it can retrieve previously generated comparison data from an earlier step in the same session. Weeks later, users report that identifiers from one session are occasionally reused for a different, unrelated product in a later session, causing Claude to retrieve and present comparison data for the wrong product with high confidence. What is the BEST fix?

A. Reduce how often the comparison data is regenerated, since staleness is the root cause
B. Never reuse or renumber identifiers once issued; expired or unknown identifiers must return an explicit error so Claude is told the reference is stale rather than silently returning plausible but wrong data
C. Increase the model's context window so it can remember more identifiers
D. Instruct users to double-check Claude's answers manually before relying on them

**Answer:** B
**Explanation:** Any handle passed to the model is a snapshot that can go stale, and because the system cannot detect staleness on its own, the executor must treat identifier reuse as strictly forbidden and return an explicit error for an invalid or stale reference — a silent reuse produces a confidently wrong result, while an explicit error is something the design can handle safely. A addresses a different problem (freshness of content, not identifier collision), C does not address identifier scoping at all, and D offloads a design-level error-handling gap onto end users.

### Q17.
A multinational bank's end-to-end design for new-hire onboarding of a Claude-based KYC document review system is nearing completion, and the original engineering team is rotating off the project. Which set of artifacts BEST demonstrates the handoff stage is actually complete?

A. A full project history including meeting notes, a chronological timeline of decisions, and a slide deck summarizing the build
B. The documented reasoning behind each design decision, the operating procedures for running the system day to day, and a runnable set of checks the incoming team can execute to verify whether a change broke anything
C. A verbal walkthrough from the departing lead engineer with no written materials
D. A list of every bug ever filed against the system during development

**Answer:** B
**Explanation:** Handoff is complete only when the receiving team can run the system, diagnose failures, and safely change it without access to the original builders, which requires design rationale, operating procedures, and executable verification checks — artifacts that are genuinely consumed by the next phase. A and D are historical records that hand nothing forward to day-to-day operation, and C leaves no durable artifact at all once the engineer departs.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
