# Objective 35: Support the Complete Solution Lifecycle

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Support the complete solution lifecycle, spanning discovery, architecture and design, implementation, testing and validation, deployment, monitoring, handover, continuous improvement, model migration, and decommissioning.

---

### Q1.
A logistics company's AI exception-routing assistant has been live for 18 months. Monitoring shows accuracy has quietly dropped 10% over the last quarter. What lifecycle phase does addressing this fall under?

A. Discovery
B. Continuous improvement (including investigating drift and retraining/re-tuning as needed)
C. Decommissioning
D. Initial deployment

**Answer:** B
**Explanation:** Ongoing performance monitoring and the response to detected degradation is the continuous improvement phase of the lifecycle, which includes root-causing drift and applying fixes. Discovery and initial deployment are earlier phases, and decommissioning is unrelated unless the system is being retired.

### Q2.
A bank wants to migrate its fraud-detection assistant from an older Claude model version to a newer one. What should happen BEFORE the migration is rolled out to production?

A. Switch immediately since newer models are always better
B. Run a structured regression evaluation comparing old vs. new model outputs on a representative test set, and define rollback criteria if results regress
C. Announce the migration only after it has already happened
D. Skip testing since the vendor guarantees compatibility

**Answer:** B
**Explanation:** Model migration should be validated with regression testing against defined criteria before production rollout, with an explicit rollback plan if issues are found. Assuming automatic improvement or vendor guarantees (A, D) is risky, and after-the-fact announcements (C) violate good change-management practice.

### Q3.
A government agency's citizen-services chatbot is being retired after being replaced by a new in-house platform. What should the decommissioning plan address?

A. Simply shutting down servers with no further action
B. Data retention/deletion obligations, migration or archival of historical conversation logs as required by policy, stakeholder notification, and a defined cutover date with fallback support
C. Letting citizens discover the system is gone on their own
D. Deleting all documentation immediately to save storage

**Answer:** B
**Explanation:** Responsible decommissioning addresses compliance (data retention/deletion), continuity (notification and fallback), and records management — not just technical shutdown. Deleting documentation (D) or leaving users to discover removal unannounced (C) are poor practice and risk compliance or trust issues.

### Q4.
A manufacturing company's new Claude-based quality assistant has just passed user acceptance testing. What is the NEXT appropriate lifecycle phase?

A. Decommissioning
B. Deployment, following an agreed rollout plan (e.g., phased or pilot rollout) with defined success gates
C. Discovery
D. Architecture and design

**Answer:** B
**Explanation:** After successful testing and validation, the natural next phase is a controlled deployment with defined rollout and success criteria. Discovery and design are earlier phases already completed, and decommissioning is the end-of-life phase, not relevant here.

### Q5.
Six weeks after go-live, a healthcare client's clinicians report the AI summarization assistant works well but ask for a new feature: auto-flagging medication conflicts. How should the architect categorize and handle this request within the lifecycle?

A. As a decommissioning trigger
B. As input to the continuous improvement phase, to be scoped, prioritized, and potentially designed as a new increment
C. As a sign the original discovery was a failure
D. As something to ignore since the original scope is "done"

**Answer:** B
**Explanation:** Post-launch feature requests are a normal and expected part of the continuous improvement phase of the lifecycle and should be scoped and prioritized like any new requirement. Dismissing them (D) or treating a reasonable enhancement request as project failure (C) misreads the lifecycle's iterative nature.

### Q6.
An insurance company's claims-triage assistant is about to go live. What should the monitoring plan established before go-live include?

A. Nothing — monitoring can be set up after problems occur
B. Defined dashboards/alerts for key metrics (accuracy, latency, error rate, escalation rate) with thresholds that trigger investigation or rollback
C. A plan to check in only once per year
D. Reliance on end users to report all problems verbally

**Answer:** B
**Explanation:** A proactive monitoring plan with concrete metrics, dashboards, and alert thresholds should be established before go-live so issues are caught early, rather than relying on infrequent manual checks or user reports alone (C, D). Waiting until problems occur to build monitoring (A) is reactive and risky.

### Q7.
A telecom's architecture team completed the design phase for a new Claude-based billing-inquiry assistant. What activity marks the transition into the implementation phase?

A. Writing the original business case
B. Building the actual system components (prompts, integrations, guardrails, infrastructure) according to the approved design and ADRs
C. Conducting user interviews for the first time
D. Shutting down the legacy billing system

**Answer:** B
**Explanation:** Implementation is where the approved design is actually built. Business case writing and user interviews belong to earlier discovery/design phases, and shutting down a legacy system is a decommissioning activity tied to migration, not implementation itself.

### Q8.
A SaaS company's product team wants to know what distinguishes the "testing and validation" phase from "monitoring" in the lifecycle. What is the key difference?

A. There is no meaningful difference between the two
B. Testing and validation verify the system meets requirements before go-live using controlled test cases, while monitoring continuously tracks real production behavior after go-live
C. Testing only happens after deployment
D. Monitoring is only needed if testing is skipped

**Answer:** B
**Explanation:** Testing/validation is a pre-deployment, controlled verification activity, while monitoring is an ongoing, production-data-driven activity after go-live — both are necessary and distinct, not substitutes for each other (C, D) nor the same activity (A).

### Q9.
A law firm's AI contract-review tool has been in production for a year. The firm now wants to retire the tool in favor of a competitor's product. What should the architect prioritize when planning the transition?

A. Deleting all historical review data immediately without client sign-off
B. A transition plan covering data export/migration to the new tool, a parallel-run or cutover period, retraining staff on the new tool, and formal decommissioning of the old system once the firm confirms successful migration
C. Ending support the moment the decision is made, with no transition period
D. Ignoring the request since the original tool still "works fine"

**Answer:** B
**Explanation:** A responsible decommissioning/transition plan protects data continuity, ensures a verified cutover, and supports staff through the change rather than abrupt termination (C) or unilateral data deletion (A), and the architect should honor the client's informed decision (D) rather than override it.

### Q10.
A government agency wants Claude-based benefits-eligibility guidance piloted with a small group of caseworkers before agency-wide rollout. What lifecycle practice does this represent?

A. Decommissioning
B. A phased/pilot deployment approach to validate real-world performance and gather feedback before full-scale rollout
C. Model migration
D. Discovery

**Answer:** B
**Explanation:** Rolling out to a limited group first to validate real-world results before a full launch is a standard phased/pilot deployment practice. It is not discovery (which precedes design), decommissioning, or model migration (which involves switching underlying models).

### Q11.
A retail company's AI personalization assistant has been running for two years on an older Claude model that Anthropic is deprecating. What should the architect do to manage this lifecycle event?

A. Wait until the model is fully shut off before taking any action
B. Proactively plan a migration project: evaluate the replacement model, regression test against current behavior, update any model-specific prompts, and schedule a cutover well before the deprecation deadline
C. Assume no changes are needed since "a model is a model"
D. Cancel the project entirely rather than migrate

**Answer:** B
**Explanation:** Model deprecation requires proactive migration planning with evaluation and testing well ahead of the deadline to avoid service disruption. Waiting until shutoff (A) risks an outage, assuming no behavior changes are needed (C) ignores real model differences, and cancelling the project (D) is an overreaction when migration is viable.

### Q12.
A finance firm's internal audit team asks when "handover" should occur in the lifecycle of a newly built AI research assistant. What is the best answer?

A. Handover should only happen informally, whenever convenient
B. Handover should be a planned phase after successful deployment and stabilization, including documentation delivery, operational training, and a defined support transition period
C. Handover should happen before the system is even tested
D. Handover is unnecessary if the original team remains available indefinitely

**Answer:** B
**Explanation:** Handover is a deliberate phase that should follow deployment and a stabilization period, packaged with documentation and training so the receiving team can operate independently. Doing it informally (A), before testing (C), or assuming the original team stays forever (D) are not sound practices.

### Q13.
A manufacturing client's production system shows a sudden spike in AI-generated false defect flags after a routine software update to an unrelated upstream system. Which lifecycle activity should catch this quickly?

A. Discovery
B. Monitoring, through alerting on anomalous shifts in flag rates that prompt investigation into the root cause
C. Decommissioning
D. The original testing phase, since it already covered all future scenarios

**Answer:** B
**Explanation:** Ongoing production monitoring with anomaly alerting is specifically designed to catch unexpected behavior shifts like this quickly, regardless of root cause location. Pre-launch testing (D) cannot anticipate every future change in connected systems, making monitoring essential post-launch.

### Q14.
A telecom's leadership asks the architect to define "continuous improvement" for their AI network-anomaly assistant in concrete terms. What is the best description?

A. An unstructured, ad hoc process with no cadence
B. A recurring cycle of reviewing performance data and stakeholder feedback, prioritizing enhancements, implementing and testing changes, and redeploying — repeated on a regular cadence
C. A one-time effort performed right after go-live and never repeated
D. Reserved only for fixing critical bugs

**Answer:** B
**Explanation:** Continuous improvement is a recurring, structured cycle, not a one-off effort (C) or limited strictly to bug fixes (D); it should have cadence and process, not be ad hoc (A).

### Q15.
A hospital system is evaluating whether to decommission a legacy rules-based triage tool in favor of a Claude-based assistant. What should the lifecycle transition plan include to minimize patient-safety risk?

A. An immediate full cutover with no parallel operation
B. A defined parallel-run or shadow period where both systems operate simultaneously, with clinical staff validating the new system's outputs against the legacy tool before full cutover and legacy decommissioning
C. Decommissioning the legacy tool before the new system has completed testing
D. No formal plan, relying on staff to adapt informally

**Answer:** B
**Explanation:** In safety-critical environments, a parallel-run/shadow period with validation before full cutover is the standard risk-mitigation practice when retiring a legacy system in favor of a new one. Immediate cutover (A), premature decommissioning (C), or having no plan (D) all introduce unacceptable patient-safety risk.

### Q16.
A retail company's AI product-description assistant begins producing noticeably worse output immediately after Anthropic releases a new default model version the team adopted. The eval score drops by six points in one specific content category. What should the architect do first?

A. Immediately redesign the entire multi-step architecture, assuming the pattern itself is now wrong
B. Treat this as a local failure tied to the model change: re-tune the affected prompts and retrieval settings against the eval suite on the new model before considering any larger redesign
C. Revert to the deprecated model permanently and refuse to migrate again
D. Ignore the drop since eval scores naturally fluctuate between model versions

**Answer:** B
**Explanation:** A failure that appears right after a model change and is localized to one category is best treated as a local, iterable problem — tune the prompt/retrieval against the eval suite — rather than assumed to be a structural flaw requiring re-architecture (A). Permanently reverting (C) avoids the inevitable migration, and dismissing a measured six-point drop (D) ignores a real regression that the eval suite was built to catch.

### Q17.
A manufacturing client wants to move its AI-assisted inspection pilot, which has performed well with one plant, into company-wide production. What should the architect ensure is agreed upon BEFORE scaling the pilot?

A. Nothing further is needed — a successful pilot should scale immediately to maximize value
B. Defined graduation criteria agreed up front — performance thresholds, operational readiness (monitoring, runbooks, support model), and risk/compliance infrastructure — so the decision to scale is evidence-based rather than ad hoc
C. A commitment to scale regardless of outcome, to maintain stakeholder enthusiasm
D. A plan to select the next use case based on whichever team asks the loudest

**Answer:** B
**Explanation:** Moving from pilot to production should be gated by pre-agreed graduation criteria covering performance, operational readiness, and risk infrastructure, preventing a successful but narrow pilot from being scaled before the organization is actually ready to support it. Scaling automatically on pilot success alone (A, C) or choosing the next use case by loudest demand (D) skips the structured evaluation this transition requires.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
