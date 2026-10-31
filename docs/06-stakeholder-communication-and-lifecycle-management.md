# Domain 6: Stakeholder Communication & Lifecycle Management

[← Back to index](../README.md)

## Exam objectives covered

1. Conduct structured discovery and requirement gathering, including identifying business objectives, stakeholders, user workflows, functional and non-functional requirements, data sources, technical constraints, security and compliance requirements, business risks, and measurable success criteria.
2. Communicate architectural decisions and trade-offs through architecture decision records, technical design documentation, diagrams, cost/benefit explanations, risk communication to non-technical stakeholders, alternative comparisons, technology justification, and scalability/performance implications.
3. Manage stakeholder feedback and expectations by establishing feedback loops, defining SLAs, agreeing on measurable performance targets, communicating system limitations, managing expectations around probabilistic outputs, communicating model upgrades/changes, and translating feedback into improvements.
4. Document architectures and implementation guidance, including technical specifications, integration documentation, data flow diagrams, security documentation, API contracts, deployment instructions, operational runbooks, testing and evaluation documentation, and knowledge transfer.
5. Support the complete solution lifecycle, spanning discovery, architecture and design, implementation, testing and validation, deployment, monitoring, handover, continuous improvement, model migration, and decommissioning.

---

### Q1.
A retail chain's VP of customer experience requests an AI assistant that "automatically resolves 80% of customer support tickets." What should the architect do before committing to any number?

A. Accept the 80% figure and begin implementation immediately
B. Establish a measured baseline of current resolution rates, define which ticket types are realistically automatable, and propose a phased target validated by a pilot
C. Tell the VP the goal is impossible and should be abandoned
D. Promise 90% instead, to exceed expectations

**Answer:** B
**Explanation:** Good discovery and expectation management replace an unvalidated aspirational number with a baseline-driven, phased target confirmed through piloting. Immediately accepting (A) or inflating the number (D) sets up failure, and outright rejection (C) skips the discovery work needed to find a realistic path forward.

### Q2.
During discovery for the ticket-automation project above, the architect learns that some ticket categories (e.g., billing disputes) carry legal and financial risk if mishandled. How should this finding influence the design?

A. It should be ignored since automation goals take priority
B. It should be documented as a business risk requiring a human-in-the-loop review gate for that specific ticket category
C. It should cause the entire project to be cancelled
D. It should only be mentioned informally in a hallway conversation

**Answer:** B
**Explanation:** Business risk findings from discovery must be formally captured and translated into concrete design controls, such as mandatory human review for high-risk categories. Ignoring the risk (A) is dangerous, cancelling the whole project (C) is an overreaction, and informal handling (D) risks the finding being lost.

### Q3.
The architect needs to explain to the retail VP why a hybrid design (AI auto-resolution for simple tickets, human handoff for complex ones) was chosen over full end-to-end automation. What is the best communication approach?

A. Present only a technical diagram with no business framing
B. Produce an ADR and a plain-language summary showing the trade-off: higher automation coverage with full automation versus lower risk and higher accuracy with the hybrid approach, tied to the ticket-risk categories identified in discovery
C. State that hybrid designs are "industry standard" with no further justification
D. Avoid explaining the trade-off to prevent pushback

**Answer:** B
**Explanation:** Strong architectural communication combines a durable record (ADR) with a business-framed explanation connecting the decision back to concrete findings (risk by ticket category). A bare diagram (A), appeal to authority (C), or avoidance (D) fail to give stakeholders what they need to understand and accept the trade-off.

### Q4.
What SLA structure is most appropriate for the new hybrid ticket-automation assistant?

A. A guarantee of zero incorrect resolutions
B. Defined targets for automation rate, average handling time, escalation accuracy, and system availability, each with measurement methodology and review cadence
C. No SLA, since AI performance can't be measured
D. An SLA based solely on customer compliments received

**Answer:** B
**Explanation:** A sound SLA for a probabilistic AI system defines multiple measurable, system-appropriate targets with a clear measurement approach, rather than an impossible zero-error guarantee (A), no SLA at all (C), or an unreliable informal proxy (D).

### Q5.
Three months after launch, the retail client's support leads report the assistant is escalating too many simple password-reset tickets to humans, reducing expected cost savings. What should the architect do?

A. Dismiss the feedback since the system is "working as designed"
B. Investigate via the established feedback loop and monitoring data, identify the root cause (e.g., an overly conservative confidence threshold for that category), and propose a tuning fix with a measurable improvement target
C. Immediately disable all escalation logic to force more automation
D. Blame the support leads for misusing the system

**Answer:** B
**Explanation:** Turning stakeholder feedback into a data-driven root-cause investigation and a measurable fix is the correct continuous-improvement response. Dismissing (A) or blaming stakeholders (D) damages trust, and removing escalation logic entirely (C) reintroduces the risk the hybrid design was meant to control.

### Q6.
A hospital's clinical informatics team is piloting a Claude-based note-summarization tool. During discovery, which non-functional requirement is MOST critical to capture given the clinical setting?

A. The visual theme of the summarization interface
B. Maximum acceptable latency during active patient encounters and required availability, including defined behavior if the system is unreachable
C. The number of supported languages for marketing purposes
D. Whether clinicians prefer serif or sans-serif fonts

**Answer:** B
**Explanation:** In a clinical setting, latency and availability directly affect patient care workflows and safety, making them the critical non-functional requirement to capture early. UI styling details (A, D) and marketing-driven language counts (C) are far less consequential.

### Q7.
The hospital's compliance officer insists that AI-generated summaries must be reviewed by a licensed clinician before entering the medical record. How should this requirement be documented and carried through the lifecycle?

A. As an informal verbal agreement only
B. As a formal compliance requirement captured in discovery, reflected in the architecture and design (mandatory review gate), and validated during testing before go-live
C. As an optional feature clinicians can turn off
D. As a decommissioning consideration only

**Answer:** B
**Explanation:** A regulatory mandate must flow formally through the lifecycle — captured in discovery, embedded in design, and verified in testing — rather than remaining informal (A), optional (C), or irrelevantly deferred to decommissioning (D).

### Q8.
Which artifact should the architect produce to show hospital IT staff and non-technical administrators how patient data flows from intake through the summarization service and into the EHR?

A. A raw database schema export
B. A data flow diagram with narrative describing data classification and retention at each step, understandable to both technical and non-technical audiences
C. A verbal-only briefing with no written record
D. The vendor's generic security brochure

**Answer:** B
**Explanation:** A diagram paired with plain-language narrative is the standard way to make data handling legible across both technical and non-technical stakeholders for compliance review. A raw schema (A) is too technical for administrators, and verbal-only (C) or generic vendor material (D) lack the specificity and durability required.

### Q9.
Anthropic announces deprecation of the Claude model version the hospital's summarization tool currently uses. What should the architect do?

A. Wait until the model is shut off, then scramble to fix things
B. Proactively plan and execute a migration: evaluate the successor model, run regression tests against clinical summarization quality benchmarks, and communicate the timeline and testing results to the client before cutover
C. Assume there's no urgency since "models rarely actually get deprecated"
D. Switch models quietly without informing the client

**Answer:** B
**Explanation:** Model migration in a regulated, safety-sensitive domain requires proactive evaluation, regression testing, and transparent stakeholder communication well before the deprecation deadline. Waiting (A), assuming no urgency (C), or silent switching (D) all create unacceptable risk.

### Q10.
A manufacturing company's plant manager reports that the AI quality-inspection assistant's accuracy appears to have degraded after six months in production. What is the correct first step in the continuous improvement process?

A. Immediately swap in a different vendor's model
B. Pull monitoring data to compare current accuracy against the original baseline, check for input data drift (e.g., new camera hardware, lighting changes), and document findings before deciding on a remediation
C. Tell the plant manager the system cannot degrade
D. Ignore the report since no formal SLA breach has been declared

**Answer:** B
**Explanation:** Diagnosing suspected degradation should start with baseline comparison and root-cause investigation (such as data drift) using existing monitoring data, which then informs the right remediation. Switching vendors without diagnosis (A), denying the possibility (C), or waiting for a formal SLA breach to act (D) are all premature or dismissive responses.

### Q11.
The manufacturing client's legal team wants an ADR explaining why the quality-inspection system uses a confidence-threshold-based auto-reject rather than fully autonomous rejection of all flagged parts. What should the ADR emphasize?

A. That auto-reject was simply easier to implement
B. The business risk of false-positive autonomous rejections (wasted good parts, production slowdowns) weighed against the benefit of full automation, and why a confidence threshold with human review for borderline cases was chosen as the balance
C. That full automation is against Anthropic's policies
D. Nothing — ADRs should not be shared with legal teams

**Answer:** B
**Explanation:** A well-reasoned ADR explicitly documents the business trade-off driving the architectural choice — here, balancing automation benefit against false-positive risk. Ease of implementation (A), a false policy claim (C), or withholding ADRs from legal (D) do not reflect sound decision documentation practice.

### Q12.
A telecom's network operations team needs a runbook for the new AI-based incident-summarization tool. What should this document prioritize?

A. Marketing talking points for the feature
B. Step-by-step triage procedures for common failure scenarios, escalation contacts, and rollback instructions
C. The original project proposal
D. A list of unrelated features planned for next year

**Answer:** B
**Explanation:** Runbooks exist to give operational staff concrete, actionable procedures for handling real incidents, which is distinct from marketing content, historical proposals, or unrelated roadmap items (A, C, D).

### Q13.
The telecom's operations director is worried that a sudden 50x spike in incident volume during a major outage could overwhelm the AI summarization tool. How should the architect address this concern?

A. Promise the system can handle unlimited load with no further detail
B. Explain the specific scaling and degradation strategy (e.g., request queuing, prioritization of critical incidents, defined behavior when capacity limits are reached) and what was validated through load testing
C. State that this scenario is too rare to plan for
D. Avoid the topic to prevent alarming the director

**Answer:** B
**Explanation:** Credible scalability communication requires concrete mechanisms and honestly stated limits, validated through testing — not blanket reassurance (A), dismissal of a realistic risk (C), or avoidance (D).

### Q14.
A government benefits agency is decommissioning its legacy keyword-based chatbot in favor of a new Claude-based assistant. What should the transition plan include to protect citizens relying on the service?

A. Immediate shutdown of the legacy system the day the new one launches
B. A parallel-run period where both systems are available, clear citizen communication about the transition, data/record migration as required by policy, and a defined cutover date with fallback support
C. No communication plan, since citizens will "figure it out"
D. Deleting legacy conversation logs immediately to reduce storage costs

**Answer:** B
**Explanation:** Decommissioning in a citizen-facing government context requires a careful parallel-run, communication, and migration plan to avoid service disruption and meet records-retention obligations. Immediate shutdown (A), no communication (C), or premature deletion of records (D) all create service and compliance risk.

### Q15.
An insurance company's underwriting team wants documentation enabling a new internal team to take over maintenance of the AI risk-scoring assistant after the original architect's contract ends. What combination of documents best supports this knowledge transfer?

A. A single slide deck from the kickoff meeting
B. A technical specification, API contracts, an operational runbook, and a recorded walkthrough session covering key design decisions and known limitations
C. The architect's informal notes shared via personal email
D. Nothing formal — the new team can learn by trial and error in production

**Answer:** B
**Explanation:** Effective knowledge transfer combines durable written documentation (spec, API contracts, runbook) with a live walkthrough capturing tacit knowledge and rationale. A kickoff slide deck (A), informal personal notes (C), or learning through live production trial-and-error (D) are inadequate and risky substitutes.

### Q16.
A SaaS company's leadership wants to understand, in business terms, why their AI writing assistant occasionally produces different phrasing for the same prompt across requests. What is the best way to frame this for a non-technical audience alongside the overall feedback and lifecycle process?

A. Tell leadership this indicates the system is broken and needs replacement
B. Explain that language models produce probabilistic outputs so some variation is expected, describe mitigations in place (e.g., retrieval grounding, lower randomness settings) and the acceptable variation threshold agreed in the SLA, and note that this feedback will feed into the ongoing improvement cycle
C. Avoid the topic since it is too technical to explain simply
D. Claim the system is fully deterministic and that leadership is mistaken

**Answer:** B
**Explanation:** Managing expectations around probabilistic outputs requires an honest, plain-language explanation tied to concrete mitigations and the agreed SLA threshold, while connecting the concern to the ongoing feedback/continuous-improvement loop. Mischaracterizing normal behavior as a defect (A), avoiding the explanation (C), or falsely claiming determinism (D) all undermine stakeholder trust.

### Q17.
During discovery for the retail chain's ticket-automation project, a stakeholder says the assistant "just needs to handle the standard tickets." What should the architect do with the word "just" and the phrase "standard tickets"?

A. Accept the statement as a complete requirement and move on, since the stakeholder clearly understands their own process
B. Treat "just" and "standard tickets" as a sign of compressed, unexamined complexity, and ask what happens to the tickets that fall outside that boundary, how many there are, and who handles them today
C. Reword the statement in the requirements document using more formal engineering language, without probing further
D. Ask the engineering team to define "standard" based on what would be easiest to automate

**Answer:** B
**Explanation:** Words like "just," "only," and undefined categories like "standard tickets" routinely hide complexity the speaker has not examined; the correct move is to ask what happens in the excluded case and how often it occurs, not to accept the summary at face value (A), merely restate it formally (C), or let engineering convenience define the boundary (D).

### Q18.
While finalizing the ADR for the hybrid ticket-automation design, a senior engineer suggests trimming the "rejected alternatives" section to shorten the document, since the team already knows why full automation was rejected. Separately, new eval data arrives showing the chosen escalation threshold underperforms what the VP announced to the board. How should the architect handle both situations?

A. Cut the rejected alternatives to save space, and quietly adjust the threshold without telling the VP, since the architect is confident it's the right call
B. Keep the rejected alternatives in the ADR so future readers can distinguish a considered-and-declined path from one that was never evaluated, and present the new eval data to the VP so they can decide how to proceed with full information
C. Cut the rejected alternatives since the current team "already knows," and override the VP's announced threshold unilaterally based on the data
D. Keep the rejected alternatives only if legal requires it, and avoid raising the eval discrepancy with the VP to prevent embarrassment

**Answer:** B
**Explanation:** Rejected alternatives must stay in an ADR so a future reader can tell a deliberately declined option from one nobody considered, and new evidence that contradicts an already-announced decision must be surfaced to the accountable owner rather than concealed or acted on unilaterally. Trimming the ADR for convenience (A, C, D) and either hiding or overriding the VP's decision (A, C, D) both undermine the record's and the stakeholder relationship's long-term value.

### Q19.
A hospital's on-call clinical IT staff keep contacting the departed architect directly whenever the AI documentation assistant misbehaves overnight, because the handover package only included a slide deck and a promise that "the architect is reachable if needed." What should have been delivered instead, and why?

A. Nothing different — a reachable architect is a reasonable long-term support model for a critical clinical system
B. A runbook mapping common failure symptoms to first actions and owners, plus the eval suite and thresholds the on-call team can run themselves, so diagnosis and routine fixes don't depend on the original architect's availability
C. A longer slide deck covering more background on the original design intent
D. A rule requiring all overnight issues to wait until the architect is available the next business day

**Answer:** B
**Explanation:** A handover is only complete when the receiving team can diagnose and resolve issues without the original architect, which requires written runbooks and a runnable eval suite rather than a dependency on a specific person's availability (A) or a thicker slide deck that still lacks operational procedure (C). Forcing clinical issues to wait for business hours (D) is unacceptable in a safety-sensitive environment and doesn't fix the underlying documentation gap.
