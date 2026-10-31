# Objective 28: Apply Human-in-the-Loop Validation

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Apply human-in-the-loop validation, including mandatory approval before high-risk actions, human review after execution for reversible actions, confidence-based escalation, exception handling, human review queues, risk-based review strategies, and audit trails and approval records.

---

### Q1.
A bank's Claude-powered agent can recommend account closures, but leadership insists no account is ever actually closed without a human clicking "confirm" in an operations console. Which implementation correctly enforces this requirement?

A. The system prompt instructs Claude to "always ask for confirmation first"
B. The account-closure API endpoint requires a valid approval record created by a human in the operations console before it will execute, and the agent can only submit a proposal, not a direct closure
C. Claude is told to summarize the risks of closing an account before proceeding
D. A nightly report lists all accounts closed that day for review

**Answer:** B
**Explanation:** Mandatory pre-execution human approval for high-risk actions must be enforced at the API/execution layer, independent of the model's own behavior, so that no prompt manipulation or model error can bypass the gate. A and C are advisory only, and D is after-the-fact (post-hoc) review, not prevention.

### Q2.
An e-commerce company allows its Claude agent to autonomously issue refunds under $50 without human review, since the action is low-value and reversible in practice (it can be clawed back via a chargeback dispute process). What human-in-the-loop pattern does this represent?

A. Mandatory pre-approval for all actions
B. Risk-based review strategy, where low-risk, reversible, low-value actions are allowed to proceed autonomously while higher-risk actions are not
C. No human oversight at all
D. Confidence-based escalation only

**Answer:** B
**Explanation:** Tiering the level of human involvement based on the risk, value, and reversibility of the action is a risk-based review strategy — a core human-in-the-loop design pattern that balances efficiency with safety. A is too strict for this case, C mischaracterizes the design (there is still a fallback process), and D describes a different pattern (based on model confidence, not transaction value).

### Q3.
A healthcare provider's clinical-notes agent is designed so that every note it drafts is saved immediately to the patient record, but a physician must review and sign off within 24 hours or the note is flagged and escalated. What human-in-the-loop pattern is this?

A. Mandatory approval before execution
B. Human review after execution for reversible/correctable actions, with an escalation mechanism if review doesn't happen in time
C. Fully autonomous operation with no human involvement
D. Confidence-based escalation only

**Answer:** B
**Explanation:** Because the note is saved first (execution) and reviewed afterward, with a time-bound escalation safety net, this is post-execution human review appropriate for an action that is correctable/reversible (the note can be amended), not a strict pre-approval gate. A would require sign-off before saving, and C and D don't fit the described workflow.

### Q4.
A legal-tech company's contract-analysis agent flags clauses it is uncertain about (below a defined confidence threshold) and routes only those clauses to a paralegal for manual review, while high-confidence clause classifications proceed automatically. What pattern does this illustrate?

A. Mandatory approval for all actions regardless of confidence
B. Confidence-based escalation, where the system routes uncertain outputs to a human reviewer based on a measurable confidence or uncertainty signal
C. Audit trail logging only
D. Fail-open behaviour

**Answer:** B
**Explanation:** Using a confidence score (or similar uncertainty signal) to decide whether a human must review a specific output is the definition of confidence-based escalation, an efficient alternative to reviewing everything or nothing. A is more conservative than described, and C and D are unrelated concepts.

### Q5.
An insurance claims system built on Claude routes claims into three queues: auto-approve (low value, high confidence), human-review queue (medium value or medium confidence), and mandatory-senior-review queue (high value or flagged for potential fraud indicators). What is the primary architectural benefit of this design?

A. It eliminates the need for any audit trail
B. It balances operational efficiency and risk management by applying proportionally more human scrutiny where the potential harm or uncertainty is greatest
C. It guarantees zero fraud will ever occur
D. It removes the need for deterministic fraud-detection rules

**Answer:** B
**Explanation:** Tiered review queues matched to risk level are the core benefit of a risk-based human-in-the-loop strategy — proportional scrutiny without blocking every transaction. A is false (audit trails are still needed), and C and D overstate what queuing alone accomplishes.

### Q6.
A government procurement system uses Claude to draft vendor-evaluation summaries that influence contract award decisions. Which practice is most important for maintaining accountability and enabling later audits of these AI-assisted decisions?

A. Deleting draft summaries once a final decision is made, to save storage
B. Maintaining an audit trail that records the AI-generated draft, any human edits, the identity of the approving official, and the timestamp of approval
C. Allowing the AI summary to be the final record with no human sign-off captured
D. Keeping only the final approved text with no record of the AI's original output

**Answer:** B
**Explanation:** A defensible audit trail must capture the full lineage — AI output, human modifications, approver identity, and timing — so decisions can be reconstructed and justified later, which is essential in public-sector and regulated contexts. A, C, and D all result in incomplete or missing accountability records.

### Q7.
A telecom company's network-operations agent can propose configuration changes to routers but immediately applies "rollback-safe" changes (fully reversible within seconds via automated revert) while queuing non-reversible changes for engineer approval. What determines the review tier each proposed change receives?

A. The time of day the change is proposed
B. The reversibility and potential blast radius of the action, which determines whether pre-approval is required or post-execution monitoring with fast rollback is sufficient
C. Which user initiated the request
D. The length of the agent's response

**Answer:** B
**Explanation:** Reversibility and potential impact are the key factors in deciding whether an action can proceed with lightweight post-hoc safeguards (fast automated rollback) versus requiring mandatory pre-approval — a textbook risk-based review strategy. A, C, and D are not meaningful risk criteria here.

### Q8.
A manufacturing company's Claude-based quality-control agent occasionally encounters sensor readings or scenarios it was not designed to classify (an "unknown defect type"). What is the best exception-handling design?

A. Force the agent to guess a classification and proceed with automated action regardless
B. Route unrecognized or out-of-scope scenarios to a dedicated human-review queue rather than allowing the agent to take automated action on unfamiliar inputs
C. Silently discard the sensor reading
D. Shut down the entire production line automatically every time

**Answer:** B
**Explanation:** Proper exception handling means recognizing when an input falls outside the agent's reliable operating envelope and escalating to a human reviewer rather than guessing or taking unchecked automated action. A risks unsafe automated decisions, C loses important data, and D is an overreaction that harms availability unnecessarily.

### Q9.
A retail company wants to ensure that human reviewers approving AI-flagged suspicious transactions don't simply "rubber-stamp" the agent's recommendation without real scrutiny. Which design choice helps mitigate this automation-bias risk?

A. Show the reviewer only the agent's final recommendation (approve/deny) with no supporting detail, to speed up review
B. Present the reviewer with the underlying evidence, confidence signals, and the agent's reasoning, and track review time/override rates to detect rubber-stamping patterns
C. Remove human review entirely since it's unreliable
D. Require the reviewer to agree with the agent 100% of the time

**Answer:** B
**Explanation:** Surfacing evidence and reasoning (rather than just a recommendation) combined with monitoring override rates helps detect and reduce automation bias, where humans default to agreeing with AI suggestions without genuine scrutiny. A worsens the risk, and C and D are not viable solutions.

### Q10.
A financial services firm is designing its loan-underwriting workflow. Which action in this workflow should most clearly require mandatory human approval before execution, rather than post-hoc review?

A. Logging the applicant's session duration on the website
B. Final denial of a loan application that has significant, often irreversible consequences for the applicant's credit access and may carry regulatory fair-lending scrutiny
C. Auto-saving a draft application form
D. Displaying a generic FAQ answer about interest rates

**Answer:** B
**Explanation:** High-impact, difficult-to-reverse decisions with regulatory implications (like loan denials under fair-lending laws) are classic candidates for mandatory pre-execution human sign-off. A, C, and D are low-risk, reversible, or informational actions well-suited to full automation.

### Q11.
A logistics company implements a human review queue for AI-flagged shipment anomalies, but engineers notice the queue has grown to 10,000 unreviewed items over two months, with items sitting for weeks before any human looks at them. What is the primary risk with this situation?

A. None — a large queue just means the system is thorough
B. A human-review queue that isn't resourced or monitored for throughput becomes a theoretical control only, since unreviewed high-risk items may be auto-escalated, ignored, or expire in ways that negate the intended safety check
C. The agent should be given full autonomy to resolve the backlog itself
D. The queue should be deleted to improve dashboard metrics

**Answer:** B
**Explanation:** A review queue is only an effective control if it is adequately staffed and monitored for SLA/throughput; an unbounded backlog means the "human-in-the-loop" control is failing in practice even though it exists on paper. A, C, and D either ignore or worsen the underlying problem.

### Q12.
A government agency's benefits-fraud detection system uses Claude to flag potentially fraudulent claims. Policy requires that any flagged case resulting in benefit suspension must have documented reasoning and reviewer sign-off retained for at least seven years. What architectural requirement does this impose?

A. The system only needs to retain the final suspension decision, not supporting reasoning
B. The system must persist structured audit records (AI flag rationale, evidence, reviewer identity, decision, and timestamp) in durable storage meeting the required retention period
C. Records can be stored only in the chat UI's session history, which is acceptable since it is rarely cleared
D. No special storage is needed since Claude itself retains conversation history indefinitely

**Answer:** B
**Explanation:** Regulatory retention requirements demand durable, structured, long-term storage of the full decision record (not just the outcome), independent of any ephemeral chat interface, which is a deliberate architectural/audit-trail design decision. A, C, and D would all fail to meet a 7-year retention and defensibility requirement.

### Q13.
A SaaS company's internal DevOps agent can propose infrastructure changes via Terraform. For changes classified as "low blast radius" (e.g., adding a log statement), the team allows auto-apply; for "high blast radius" changes (e.g., modifying production security groups), mandatory two-person human approval is required before apply. What principle guides this split?

A. Alphabetical ordering of resource names
B. Risk-based review calibrated to potential impact (blast radius), applying stricter human gates to higher-consequence actions
C. The agent's confidence score alone, regardless of impact
D. Random sampling of changes for review

**Answer:** B
**Explanation:** Calibrating the rigor of human review to the potential impact/blast radius of an action is the essence of a risk-based review strategy, distinct from purely confidence-based or random approaches. A and D are not meaningful risk criteria, and C ignores impact entirely.

### Q14.
An airline's Claude-based rebooking agent automatically rebooks passengers on cancelled flights without pre-approval, but every rebooking is logged with full reasoning and is reversible by a human agent within a 2-hour window if a passenger disputes it. Why might this be an appropriate design instead of mandatory pre-approval?

A. Because airlines are exempt from any human oversight requirements
B. Because the action is readily reversible, time-sensitive (passengers need rebooking quickly), and relatively low-risk, making post-execution review with a fast correction window a reasonable risk-based tradeoff
C. Because Claude never makes mistakes in rebooking
D. Because audit trails are unnecessary for travel bookings

**Answer:** B
**Explanation:** When speed matters and the action is reversible with a bounded correction window, post-execution review is a legitimate risk-based alternative to mandatory pre-approval, as long as logging and a reliable correction mechanism exist. A, C, and D are incorrect justifications.

### Q15.
A manufacturing safety officer asks the architecture team to justify why their new agent requires human approval before adjusting pressure-valve thresholds on an industrial system, even though the agent has performed well in simulation for six months. What is the best justification?

A. Simulation performance over six months definitively proves the action is safe to fully automate
B. Physical safety-critical, difficult-to-reverse actions with potential for serious harm warrant mandatory human approval regardless of simulated performance, since simulations may not capture all real-world edge cases and the cost of a rare failure is severe
C. Human approval is only a regulatory formality with no real safety value here
D. The agent should instead be given more autonomy to reduce latency in emergency situations

**Answer:** B
**Explanation:** For safety-critical, high-consequence, hard-to-reverse physical actions, mandatory human approval remains warranted because simulated success does not guarantee coverage of all real-world edge cases, and the asymmetric cost of a rare failure justifies the friction. A, C, and D understate the real risk involved.

### Q16.
A bank designs its human-review routing primarily around transaction dollar amount: anything under $1,000 is auto-approved, anything over is queued for a reviewer. Under this scheme, a $5 outbound email blast that mistakenly broadcasts a wrong promotional rate to 10,000 customers and cannot be unsent is auto-approved, while a $50,000 internal ledger reclassification that can be fully reversed before end-of-day batch close sits in the review queue. What is wrong with this design, and what should replace it?

A. Nothing is wrong; dollar amount is always the correct proxy for risk
B. Routing by transaction size is the wrong axis; review gates should instead be set according to whether the action's outcome can be undone and how far its effects spread, since a small irreversible external action can carry far more harm than a large reversible internal one
C. The thresholds are simply set too low and should be raised
D. The bank should remove human review entirely and rely on the model's own judgment

**Answer:** B
**Explanation:** Transaction size does not correlate with actual risk; the correct routing axis is reversibility and blast radius, since a small but irreversible, widely-propagating action (like an erroneous mass email) can cause far more harm than a large but easily reversible internal change. A and C preserve the flawed axis, and D removes oversight entirely rather than correcting its targeting.

### Q17.
A SaaS company's agent workflow requires a human manager's approval before an agent can apply a high-impact infrastructure change, but managers often take several hours to respond given time zone differences, and the team does not want to keep a compute process alive and billing the whole time waiting on a response. What approval-handling pattern addresses this without treating a slow reviewer as a systemic failure?

A. Automatically approve the change if the manager hasn't responded within 10 minutes
B. Design the approval step so it can return a deferred response: the process exits (or pauses cheaply) and resumes later from persisted session state once the approval arrives, paired with a notification (e.g., Slack, email, or push) so the pending request is not invisible while waiting
C. Require the agent to keep polling in a tight loop indefinitely until approval is granted
D. Remove the approval requirement for any change proposed outside business hours

**Answer:** B
**Explanation:** A robust human-in-the-loop design should support deferred/asynchronous approval — exiting or pausing the process and resuming from durable state once a decision is made — combined with proactive notifications so a slow human reviewer is a configuration detail, not an architectural failure. A and D silently bypass the control under time pressure, and C wastes resources without actually solving the latency problem.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
