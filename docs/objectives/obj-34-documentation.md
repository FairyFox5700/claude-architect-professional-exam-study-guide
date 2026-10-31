# Objective 34: Document Architectures and Implementation Guidance

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Document architectures and implementation guidance, including technical specifications, integration documentation, data flow diagrams, security documentation, API contracts, deployment instructions, operational runbooks, testing and evaluation documentation, and knowledge transfer.

---

### Q1.
A bank's engineering team will take over maintenance of a Claude-based fraud-review assistant after the architect's consulting engagement ends. Which document is MOST critical to ensure a smooth handover?

A. A slide deck used in the original sales pitch
B. A comprehensive technical specification and operational runbook covering architecture, configuration, monitoring, and common failure remediation steps
C. A single email summarizing the project
D. The architect's personal notes, informally shared

**Answer:** B
**Explanation:** Durable, structured technical specs and runbooks are what enable another team to operate and maintain a system independently. Sales materials, a summary email, or informal notes (A, C, D) lack the depth and structure needed for real operational handover.

### Q2.
A healthcare software vendor needs to document how patient data moves from intake to the Claude-based summarization service and back to the EHR. What document type is most appropriate?

A. A marketing one-pager
B. A data flow diagram with accompanying narrative describing data classification, transformations, and storage/retention at each step
C. A verbal briefing to the compliance officer only
D. The vendor's standard terms of service

**Answer:** B
**Explanation:** Data flow diagrams paired with narrative detail on classification and retention are the standard way to document and later audit how sensitive data moves through a system — essential for healthcare compliance. The other options are not durable, specific, or auditable artifacts.

### Q3.
A retail company's external developers need to integrate their e-commerce platform with a Claude-powered recommendation API built by the architect's team. What should the API contract documentation include at minimum?

A. Only a list of supported programming languages
B. Request/response schemas, authentication method, rate limits, error codes, and versioning policy
C. A general description of what the API "does" in one paragraph
D. The internal architecture diagram with no interface details

**Answer:** B
**Explanation:** A usable API contract must specify the concrete interface details developers need to integrate correctly and handle failures: schemas, auth, limits, errors, and versioning. A vague description or internal-only diagrams (A, C, D) don't give integrators what they need.

### Q4.
A logistics company's security team requires documentation proving the AI exception-handling system properly isolates customer data between tenants in a multi-tenant deployment. What document should the architect produce?

A. A press release about the product
B. Security documentation describing tenant isolation mechanisms (e.g., data partitioning, access controls, encryption boundaries) with evidence or test results supporting the claims
C. A verbal assurance in a sales call
D. The vendor's generic compliance certificate with no system-specific detail

**Answer:** B
**Explanation:** Security documentation must be specific to the actual system's isolation mechanisms and backed by evidence, since generic certificates or verbal assurances don't demonstrate how this particular deployment enforces tenant separation. Marketing material is irrelevant to a security review.

### Q5.
A manufacturing client's operations staff will run the AI defect-detection assistant day-to-day. Which document helps them respond when the assistant produces an unexpected error during a production shift?

A. The original project charter
B. An operational runbook with step-by-step triage procedures, common error codes, escalation contacts, and rollback instructions
C. The architect's resume
D. A high-level architecture diagram with no procedural detail

**Answer:** B
**Explanation:** Runbooks are specifically designed to give operational staff actionable, step-by-step guidance for real-time incident response. Architecture diagrams (D) show structure but not procedure, and the project charter (A) is a planning artifact, not an operational one.

### Q6.
An insurance company's QA team wants to confirm the claims-summarization assistant meets accuracy requirements before go-live. What should the testing and evaluation documentation include?

A. A statement that "the model passed all tests" with no further detail
B. The evaluation methodology, test dataset composition, metrics used (e.g., precision, recall, hallucination rate), results against defined thresholds, and known edge cases
C. Only screenshots of a few sample outputs
D. The vendor's published benchmark scores on unrelated public datasets

**Answer:** B
**Explanation:** Rigorous evaluation documentation must describe methodology, data, metrics, and results against the client's own thresholds — unrelated vendor benchmarks (D) or unsupported pass/fail claims (A) don't demonstrate fitness for this specific use case.

### Q7.
A SaaS company is deploying a new Claude-powered feature to production for the first time. What should the deployment instructions document specify?

A. Only the final production URL
B. Environment prerequisites, configuration steps, secrets/credential management, rollout sequence (e.g., canary or blue-green), and rollback procedure
C. A generic cloud provider tutorial link
D. The marketing launch date only

**Answer:** B
**Explanation:** Deployment documentation needs to be specific and actionable: prerequisites, config, credential handling, rollout strategy, and rollback — generic links or a bare URL (A, C) are not sufficient for a safe production launch, and launch dates (D) are a project-management detail, not a deployment procedure.

### Q8.
A government agency's new engineering hires need to understand an existing Claude-based citizen-inquiry system built two years ago by a vendor that is no longer engaged. What activity is most critical to prevent knowledge loss?

A. Hoping the new hires can reverse-engineer the system from code alone
B. A structured knowledge-transfer process including documentation review sessions, architecture walkthroughs, and recorded Q&A with any available original team members
C. Relying solely on scattered Slack/Teams message history
D. Skipping onboarding since the system "mostly works"

**Answer:** B
**Explanation:** Effective knowledge transfer combines living documentation with structured walkthroughs and direct access to original context, especially when the original team is no longer available. Scattered chat history or code alone (A, C) is an incomplete and unreliable substitute, and skipping onboarding (D) is a known risk factor for future outages.

### Q9.
A telecom's architecture review board requires a technical specification before approving a new Claude-based network-anomaly-detection system. Which content is essential to include?

A. A list of unrelated systems the architect previously built
B. System purpose, functional and non-functional requirements, component architecture, data sources, integration points, and key design decisions
C. Only a cost estimate
D. The CEO's quote from the press release

**Answer:** B
**Explanation:** A technical specification must comprehensively describe what the system does, how it's built, and why, so a review board can evaluate soundness and completeness. Cost alone, unrelated history, or marketing quotes (A, C, D) don't support a technical approval decision.

### Q10.
A law firm's IT team asks for documentation on how the AI contract-review assistant integrates with their existing document management system (DMS). What should this integration documentation cover?

A. A single diagram with no written explanation
B. Authentication/authorization flow between systems, data exchange format, trigger events (e.g., document upload), and error-handling behavior for failed syncs
C. Only the DMS vendor's generic API documentation
D. A promise that "it just works"

**Answer:** B
**Explanation:** Integration documentation needs to explain the specific, bespoke connection between the two systems — auth flow, data format, triggers, and failure handling — none of which is covered by generic vendor docs (C) or vague assurances (D).

### Q11.
An architect is documenting the security posture of a Claude deployment for a financial services client subject to regulatory audit. Which element is MOST important to include?

A. A statement that "the system is secure" without elaboration
B. Specific controls in place: data encryption at rest/in transit, access control model, logging/audit trail, data retention policy, and incident response procedure
C. The vendor's general marketing claims about safety
D. A list of unrelated certifications held by the consulting firm

**Answer:** B
**Explanation:** Audit-ready security documentation must enumerate concrete, verifiable controls specific to the deployment. Generic marketing assurances or unrelated certifications (C, D) do not satisfy regulatory audit requirements, and a bare "it's secure" claim (A) provides no evidence.

### Q12.
A manufacturing company wants API contract documentation to also specify backward-compatibility guarantees for their internal tools consuming the AI assistant's output. What should this section address?

A. Nothing, since APIs never change
B. The versioning scheme, deprecation timeline for old versions, and the policy for introducing breaking vs. non-breaking changes
C. A disclaimer that all changes may break integrations with no warning
D. An assumption that consumers will monitor for changes themselves

**Answer:** B
**Explanation:** Clear versioning and deprecation policies let integrators plan around change safely, which is the purpose of documenting backward compatibility. Assuming no process is needed (A, D) or offering no guarantees at all (C) creates unnecessary integration risk for consumers.

### Q13.
During a knowledge-transfer session, a hospital's internal team asks why certain design decisions were made for their AI documentation assistant, but the original design meeting notes are missing. What should the architect have done differently earlier in the project?

A. Nothing — oral history is sufficient for complex systems
B. Maintained ADRs and design documentation contemporaneously throughout the project so rationale is preserved independent of personal memory or meeting attendance
C. Relied on the client to take their own notes
D. Assumed decisions are self-evident from the code

**Answer:** B
**Explanation:** This scenario highlights why ADRs and design docs should be created as decisions are made, not reconstructed later from memory. Relying on oral history, client note-taking, or code alone (A, C, D) risks losing critical rationale needed for future maintenance and trust.

### Q14.
A telecom's QA lead wants the evaluation documentation to distinguish between the AI assistant's performance on common cases versus rare edge cases. Why is this distinction important to document?

A. It isn't important — an overall average score is sufficient
B. Aggregate scores can mask poor performance on high-impact rare scenarios (e.g., emergency service outage reports), so documenting stratified results helps stakeholders assess real-world risk
C. Edge cases should be excluded from testing entirely
D. Only common-case performance matters for sign-off

**Answer:** B
**Explanation:** Stratified evaluation reporting reveals risk that a single aggregate metric can hide, which matters greatly when rare cases carry outsized business or safety impact. Excluding edge cases (C) or ignoring them in sign-off (D) is a significant testing and documentation gap.

### Q15.
A retail company's new vendor-management team asks the architect to supply documentation enabling them to evaluate the AI assistant's ongoing total cost of ownership. What should be included?

A. Only the initial one-time license cost
B. A breakdown of compute/token costs, licensing, maintenance effort, and expected scaling cost as usage grows, alongside assumptions used in the estimate
C. A single lump-sum number with no breakdown
D. A promise that costs will never increase

**Answer:** B
**Explanation:** Useful cost documentation itemizes the cost drivers and underlying assumptions so stakeholders can evaluate and re-forecast total cost of ownership as conditions change. A single undifferentiated figure or a no-cost-growth promise (A, C, D) doesn't support informed ongoing vendor management.

### Q16.
As part of a handover package for a logistics client's AI routing assistant, the departing architect includes a note offering a dedicated office-hours slot and a named contact for any future questions, in place of writing out certain configuration rationale. Why is this an inadequate substitute for documentation?

A. It is adequate, since a live contact can always answer more thoroughly than a document
B. A route for asking a question is not the same as answering it; it converts written knowledge into a dependency on a specific person being available, which fails once that person leaves or is unavailable
C. Office hours are a documented and auditable artifact under most compliance frameworks
D. It is inadequate only because office hours are inconvenient to schedule

**Answer:** B
**Explanation:** A named contact or office-hours slot supplies a way to ask a question, not an answer, and a question that still has to be asked has not actually been documented — the knowledge quietly depends on one person's continued availability. This is a known handover anti-pattern regardless of how convenient the contact's schedule is (D) or how thorough they might be in person (A, C).

### Q17.
A telecom's on-call engineers are repeatedly paging the architect at all hours after a production AI assistant's answer quality degrades following unrelated upstream changes. What is the best long-term fix?

A. Keep the architect permanently on the on-call rotation so they can respond personally each time
B. Build a runbook mapping common symptoms to likely architectural causes (e.g., retrieval failure, prompt version, model change, tool errors), paired with dashboards and an eval command the on-call team can run themselves to diagnose and act
C. Automatically disable the assistant the moment any quality metric drops, with no further process
D. Move to a more capable model so the issue stops recurring

**Answer:** B
**Explanation:** A structured runbook that maps symptoms to causes and equips on-call staff with the diagnostic tools (traces, dashboards, an eval they can run) lets the team resolve incidents independently, which is the actual goal of operational documentation. Keeping the architect permanently on call (A) does not scale and defeats the purpose of a handover, blind model swaps (D) treat a symptom without diagnosis, and automatic shutdowns with no process (C) just replace one incident with another.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
