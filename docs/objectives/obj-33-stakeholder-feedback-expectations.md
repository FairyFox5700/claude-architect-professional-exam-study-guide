# Objective 33: Manage Stakeholder Feedback and Expectations

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Manage stakeholder feedback and expectations by establishing feedback loops, defining SLAs, agreeing on measurable performance targets, communicating system limitations, managing expectations around probabilistic outputs, communicating model upgrades/changes, and translating feedback into improvements.

---

### Q1.
A business stakeholder at a retail company insists that a new Claude-based customer support assistant must achieve "100% customer satisfaction" to be considered successful. How should the architect respond?

A. Agree to the 100% target to keep the stakeholder happy
B. Explain that 100% is not a realistic or measurable target, and propose a specific, achievable metric (e.g., CSAT ≥ 85%, with a defined baseline and measurement window)
C. Refuse to define any success metric
D. Tell the stakeholder that customer satisfaction cannot be measured for AI systems

**Answer:** B
**Explanation:** Managing expectations means replacing unrealistic absolute targets with specific, measurable, and achievable goals tied to a baseline. Silently agreeing (A) sets the project up to "fail" against an impossible bar, while refusing to engage (C, D) abdicates the architect's responsibility.

### Q2.
A hospital's IT director wants an SLA for the clinical note-summarization assistant. Which SLA term is MOST appropriate for an AI system with inherently probabilistic outputs?

A. "100% accuracy guaranteed on all summaries"
B. "99.5% system availability, median response time under 3 seconds, and summary accuracy validated against a sampled audit with a target error rate below an agreed threshold"
C. "The system will never make a mistake"
D. "Accuracy will improve over time with no specific target"

**Answer:** B
**Explanation:** A sound SLA for an LLM-based system separates measurable infrastructure guarantees (availability, latency) from output-quality targets validated through sampling, since perfect accuracy cannot be guaranteed. Absolute guarantees (A, C) misrepresent how generative models work, and vague promises (D) are not an SLA.

### Q3.
A finance firm's compliance team is uneasy that the AI research assistant occasionally gives different answers to the same question on different runs. What is the best way to manage this expectation?

A. Tell them the behavior is a bug that will be fixed immediately
B. Explain that LLM outputs are probabilistic and some variance is expected, describe steps taken to reduce unwanted variance (e.g., lower temperature, grounding in retrieved sources), and define what consistency level is acceptable
C. Avoid discussing the behavior
D. Claim the system is deterministic and the team is mistaken

**Answer:** B
**Explanation:** Managing expectations around probabilistic outputs means honestly explaining the underlying behavior, what mitigations exist, and agreeing on an acceptable consistency bar — not denying it (D) or mischaracterizing it as a simple bug (A).

### Q4.
A logistics company's operations manager is frustrated that the AI exception-routing assistant sometimes misroutes a shipment. What is the best structured mechanism to address this ongoing concern?

A. A one-time apology email
B. An established feedback loop (e.g., regular review sessions, a logged issue tracker, and periodic model/prompt tuning cycles) that captures and prioritizes real-world misroutes for improvement
C. Telling the manager to stop reporting issues since they are expected
D. Disabling the assistant until further notice without discussion

**Answer:** B
**Explanation:** A structured, recurring feedback loop is the correct mechanism to continuously capture, triage, and act on real-world issues. An apology (A) or shutdown without discussion (D) does not address the underlying process gap, and dismissing complaints (C) damages trust.

### Q5.
Anthropic releases a new Claude model version. A SaaS client's product team is anxious about potential behavior changes in their production copilot. What is the BEST communication practice?

A. Silently switch to the new model without notifying the client
B. Proactively communicate the upgrade timeline, run a regression evaluation against the client's test suite, and share results and any behavior differences before switching in production
C. Wait for the client to notice the change and ask questions
D. Tell the client upgrades are entirely risk-free

**Answer:** B
**Explanation:** Responsible model-upgrade communication is proactive, evidence-based (regression testing), and transparent about any behavior differences before the change reaches production. Silent changes (A) or reactive communication (C) erode trust, and claiming zero risk (D) is misleading.

### Q6.
A government agency's citizen-services team reports repeatedly that the AI chatbot misunderstands questions phrased in regional dialects. How should this feedback be handled?

A. Log it but take no action since dialects are too complex to address
B. Translate the feedback into a specific improvement initiative — e.g., expanding the prompt/examples or retrieval corpus to cover dialect variations — and set a target for measurable improvement
C. Tell the team to instruct citizens to phrase questions differently
D. Escalate to Anthropic and consider the matter closed

**Answer:** B
**Explanation:** Managing feedback well means converting a pattern of complaints into a concrete, measurable improvement plan owned by the project team. Shifting the burden to end users (C) or treating it as unsolvable (A) or someone else's problem (D) fails the stakeholder.

### Q7.
A manufacturing client wants to know what the AI quality-inspection assistant CANNOT do. What is the best way to communicate system limitations?

A. Avoid discussing limitations to maintain stakeholder confidence
B. Clearly document known failure modes (e.g., poor performance on low-light images, inability to detect defect types outside training examples) and provide guidance on when human inspection is required
C. State that the system has no limitations
D. Only mention limitations if directly asked, and keep answers vague

**Answer:** B
**Explanation:** Transparent, specific documentation of limitations and fallback guidance builds durable trust and prevents misuse in scenarios the system isn't suited for. Hiding or downplaying limitations (A, C, D) sets up future failures and loss of credibility.

### Q8.
An insurance company's business sponsor asks for a monthly performance review meeting for the claims-triage assistant. What should this feedback loop primarily track?

A. Only the number of support tickets filed against engineers
B. Agreed-upon performance metrics (accuracy, latency, escalation rate), trend over time, and a running list of stakeholder-reported issues with resolution status
C. General anecdotes with no data
D. The architect's personal opinion of how the project is going

**Answer:** B
**Explanation:** Effective ongoing feedback reviews are grounded in the previously agreed measurable targets and a transparent issue log, enabling informed decisions. Anecdotes (C) or personal opinion (D) without data undermine accountability.

### Q9.
A telecom's call-center director worries that promising "80% automated resolution" sets unrealistic expectations with frontline staff. What should the architect recommend?

A. Promise 80% regardless of evidence to satisfy leadership
B. Establish a phased rollout with a measured baseline, define what "resolution" means precisely, and set an initial conservative target (e.g., 40-50%) to be revised upward based on real performance data
C. Avoid giving leadership any numeric target
D. Tell leadership the target is impossible and the project should be cancelled

**Answer:** B
**Explanation:** Responsible expectation management replaces an unvalidated aspirational number with a phased, evidence-based target that can be adjusted as real data comes in. Refusing to give any number (C) or declaring the project dead (D) are overcorrections, and blindly promising the original figure (A) sets up failure.

### Q10.
A legal firm's partners ask the architect to guarantee the AI contract-review tool will "never miss a risky clause." How should the architect respond?

A. Provide the guarantee to close the deal
B. Explain that no AI system can guarantee zero misses, present the tool's measured recall rate on a benchmark set, and recommend it as an assistive second-check layer alongside attorney review, not a replacement
C. Suggest the partners stop using human review entirely once the tool is deployed
D. Refuse to provide any accuracy data

**Answer:** B
**Explanation:** Setting honest expectations about probabilistic system limitations — backed by actual measured performance — while clarifying the tool's role as an assistive layer is the professionally responsible response. A false guarantee (A) or removing human oversight (C) creates serious liability risk.

### Q11.
A SaaS company wants to understand how negative feedback from beta users will be incorporated into the next release of their AI writing assistant. What should the architect establish?

A. An informal process where feedback is remembered but not tracked
B. A defined feedback intake and triage process (e.g., categorize by severity/frequency, map to backlog items, communicate back to reporters when addressed) feeding into a regular release cycle
C. A policy of ignoring beta feedback until general availability
D. A rule that only feedback from paying customers is considered

**Answer:** B
**Explanation:** Translating feedback into improvement requires a repeatable, visible process connecting reports to prioritized action and closing the loop with the reporter. Informal, undocumented handling (A) or ignoring early feedback (C) wastes valuable signal, and excluding beta users (D) overlooks a key source of pre-launch insight.

### Q12.
A bank's risk officer asks what SLA metric is appropriate for the "helpfulness" of an AI assistant answering internal policy questions, given it's subjective. What should the architect propose?

A. No metric is possible for subjective qualities, so skip it
B. A proxy metric such as a periodic human-rated sample score (e.g., average rating ≥ 4/5 on a defined rubric) combined with escalation/override rate as a quantifiable stand-in for helpfulness
C. Use system uptime as the sole indicator of helpfulness
D. Rely solely on unstructured anecdotal praise or complaints

**Answer:** B
**Explanation:** Subjective qualities can still be operationalized into measurable proxies (rubric-based sampling, escalation rates) suitable for an SLA. Claiming it's unmeasurable (A) or substituting an unrelated metric like uptime (C) fails to address the actual stakeholder concern.

### Q13.
Six months into deployment, a manufacturing client's plant managers report the AI defect-detection assistant's accuracy seems to be degrading. What should the architect do first?

A. Dismiss the report as anecdotal
B. Investigate with data (e.g., compare recent accuracy metrics against the original baseline, check for data drift in sensor inputs or defect types), then communicate findings and a remediation plan
C. Immediately upgrade to the newest model without analysis
D. Tell the plant managers to retrain their own expectations

**Answer:** B
**Explanation:** Stakeholder-reported performance concerns should be validated against baseline data and investigated for root cause (e.g., drift) before any remediation action, and the findings should be communicated transparently. Dismissing (A) or deflecting (D) damages trust, and changing models without diagnosis (C) risks masking the real issue.

### Q14.
A government procurement office requires the architect to define what happens if the AI assistant's uptime falls below the agreed SLA threshold. What should be included in this conversation?

A. Nothing — SLA breaches are purely a legal matter outside the architect's scope
B. Clearly defined remediation steps (e.g., root-cause review, credits/penalties per contract, improvement plan) and escalation path, documented and agreed upon before go-live
C. A vague promise to "try harder" next time
D. An assumption that breaches will never happen, so no plan is needed

**Answer:** B
**Explanation:** Mature SLA management defines concrete remediation and escalation procedures in advance, which the architect should help shape even though commercial penalty terms may involve legal/contracts teams. Assuming breaches won't occur (D) or offering vague reassurance (C) leaves stakeholders unprotected.

### Q15.
A retail client's marketing team keeps requesting new AI assistant features mid-sprint based on informal hallway conversations with the architect. What should the architect do to better manage this?

A. Implement every request immediately to maintain goodwill
B. Redirect ad hoc requests into the established feedback/intake process so they are logged, prioritized against existing commitments, and communicated transparently
C. Refuse to speak with the marketing team at all
D. Implement only the requests from the most senior person who asked

**Answer:** B
**Explanation:** Protecting a structured feedback and roadmap process — rather than reacting to informal requests ad hoc — keeps expectations manageable and commitments honest. Blanket acceptance (A) or seniority-based prioritization (D) undermines the planning process, and refusing engagement (C) harms the stakeholder relationship.

### Q16.
Midway through building a SaaS company's AI writing assistant, the client requests a significant new capability (multi-language support) not in the original scope. What two practices should the architect follow to manage this scope change properly?

A. Quietly absorb the work to maintain goodwill, and leave the original project plan and timeline unchanged
B. Expose the cost and schedule impact of the request as soon as it is raised, and if accepted, formally reset the agreed plan (dates, scope, commitments) in writing
C. Accept the request immediately with no cost discussion, and silently extend the deadline without telling the client
D. Refuse to discuss the request until the current sprint ends

**Answer:** B
**Explanation:** Sound scope-change management surfaces the cost the moment a request is made, rather than absorbing it silently, and formally resets the plan once a change is accepted so everyone works from the same true picture. Silently absorbing the change (A) or accepting it while leaving a now-false plan in place (C) both conceal the real impact from stakeholders, and refusing to engage (D) isn't a substitute for a defined intake process.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
