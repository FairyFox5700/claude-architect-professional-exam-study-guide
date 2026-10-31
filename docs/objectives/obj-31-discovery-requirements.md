# Objective 31: Conduct Structured Discovery and Requirement Gathering

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Conduct structured discovery and requirement gathering, including identifying business objectives, stakeholders, user workflows, functional and non-functional requirements, data sources, technical constraints, security and compliance requirements, business risks, and measurable success criteria.

---

### Q1.
A regional bank's operations VP asks for an AI assistant that "handles all loan inquiry calls automatically." Before scoping the project, what should the architect do first?

A. Immediately begin prototyping a voice-enabled Claude agent to demonstrate feasibility
B. Run a structured discovery session to clarify what "handles automatically" means, which inquiry types qualify, and what success looks like
C. Tell the VP the request is not feasible and recommend a simpler FAQ chatbot instead
D. Ask the engineering team to estimate infrastructure costs based on current call volume

**Answer:** B
**Explanation:** Vague executive requests must be translated into concrete, measurable requirements before any design or costing work begins. Prototyping (A) or costing (D) too early risks building the wrong thing, and rejecting the idea outright (C) skips discovery entirely.

### Q2.
A hospital system wants Claude integrated into clinician workflows to summarize patient visit notes. During discovery, which question is MOST important to surface non-functional requirements?

A. "Which EHR vendor do you currently use?"
B. "What is the acceptable latency and availability for summaries during active patient visits, and what happens if the system is unavailable?"
C. "Do clinicians prefer bullet points or paragraphs?"
D. "How many clinicians will use the tool in year one?"

**Answer:** B
**Explanation:** Latency, availability, and failure-mode expectations are classic non-functional requirements that directly affect architecture choices (e.g., fallback workflows). Vendor identity (A), formatting preference (C), and user counts (D) are relevant but secondary to safety-critical performance constraints.

### Q3.
During discovery for a retail client's product-recommendation assistant, the architect discovers that marketing, merchandising, and customer-support teams each expect different outcomes from the same project. What is the best next step?

A. Proceed with marketing's requirements since they sponsored the budget
B. Document each stakeholder group's objectives separately, then reconcile conflicts into a single prioritized requirements set
C. Build three separate systems to satisfy each team
D. Escalate to the CTO to pick a single owner and ignore the rest

**Answer:** B
**Explanation:** Proper stakeholder identification requires capturing and reconciling divergent objectives rather than silently favoring the loudest or best-funded group. Options A, C, and D each skip the structured reconciliation step that discovery is meant to produce.

### Q4.
A manufacturing company wants Claude to generate maintenance work orders from sensor logs. Discovery reveals the sensor data arrives in three incompatible formats from different plants. How should this be classified?

A. A non-functional requirement
B. A data source and technical constraint that must be documented before design
C. An out-of-scope detail to be solved during deployment
D. A security and compliance requirement

**Answer:** B
**Explanation:** Heterogeneous data formats are a concrete technical constraint tied to data sourcing and must shape the ingestion architecture; deferring it (C) risks costly rework. It is not primarily about non-functional performance (A) or compliance (D).

### Q5.
A law firm wants an AI tool to draft contract clauses. Which discovery question best addresses business risk?

A. "What is the expected response time for clause generation?"
B. "What happens if the model generates a clause that is legally incorrect and a partner signs off without noticing?"
C. "Which word processor do attorneys currently use?"
D. "How many templates exist today?"

**Answer:** B
**Explanation:** Identifying the risk of unnoticed erroneous output in a high-stakes legal context is central to business risk analysis and will shape review workflows and liability controls. The other options are useful but are workflow/tooling details, not risk framing.

### Q6.
An insurance company's claims department requests a Claude-based fraud-flagging assistant. During discovery, the architect should prioritize identifying measurable success criteria. Which is the BEST example of such a criterion?

A. "The system should be smart about fraud"
B. "Reduce false-positive fraud flags by at least 20% within six months while maintaining current detection recall"
C. "Use the latest Claude model available"
D. "Make claims adjusters happy with the tool"

**Answer:** B
**Explanation:** A measurable success criterion specifies a quantifiable target, baseline, and timeframe. The other options are vague aspirations that cannot be objectively evaluated post-launch.

### Q7.
A telecom provider wants to deploy Claude to triage customer complaints submitted via chat. Which discovery step most directly uncovers security and compliance requirements?

A. Mapping how customer PII flows through the system and which regulations (e.g., telecom privacy rules) apply to that data
B. Interviewing the UX team about chat window design
C. Benchmarking Claude's response time against a competitor's chatbot
D. Reviewing the company's brand style guide

**Answer:** A
**Explanation:** Compliance requirements emerge from understanding data flows, data classification, and applicable regulations — a core discovery activity. The other choices address usability or performance, not compliance.

### Q8.
During discovery with a logistics company, the architect learns that warehouse staff currently route exceptions through a complex approval chain involving three managers. What discovery activity does this best represent?

A. Gathering functional requirements
B. Understanding existing user workflows
C. Identifying technical constraints
D. Establishing success criteria

**Answer:** B
**Explanation:** Mapping how work currently flows through people and approvals is workflow analysis, which reveals where automation can realistically fit. It is distinct from functional requirements (specific system behaviors) or technical constraints (infrastructure limits).

### Q9.
A government agency wants an AI system to answer citizen inquiries about benefits eligibility. A key non-functional requirement surfaces: the system must be usable by citizens with low digital literacy and must meet accessibility standards. How should the architect treat this finding?

A. Ignore it since it is a UX concern, not architecture
B. Capture it as a formal non-functional requirement influencing interface design and testing criteria
C. Defer it to the deployment phase
D. Assume Claude's default behavior already satisfies accessibility needs

**Answer:** B
**Explanation:** Accessibility and usability for a defined population are legitimate non-functional requirements that must be documented early, since they affect interface design, testing, and acceptance criteria. Assuming default compliance (D) or deferring it (C) risks late, costly rework.

### Q10.
A SaaS company's product team asks for "an AI copilot that increases user engagement." What is the first discovery task the architect should perform?

A. Select the model size and context window
B. Translate the vague goal into specific business objectives and measurable engagement metrics (e.g., session length, feature adoption)
C. Draft the API contract
D. Propose a pricing model for the copilot feature

**Answer:** B
**Explanation:** Discovery begins with converting ambiguous business goals into concrete, measurable objectives before any technical or commercial decisions are made. The other options are downstream of having clear objectives.

### Q11.
While gathering requirements for a finance firm's research-summarization tool, the architect finds that analysts need summaries cross-referenced with real-time market data from an external feed. What discovery category does this finding belong to?

A. Identifying data sources
B. Defining success criteria
C. Identifying business risks
D. Stakeholder identification

**Answer:** A
**Explanation:** Recognizing the need for an external real-time data feed is squarely a data-source discovery finding that will shape integration architecture. It does not itself define success metrics, risks, or stakeholders.

### Q12.
A healthcare SaaS vendor's compliance officer insists during discovery that any AI-generated clinical note summary must be reviewed by a licensed clinician before entering the medical record. How should the architect classify and act on this input?

A. Treat it as a nice-to-have UX suggestion
B. Treat it as a mandatory compliance/security requirement and incorporate a human-in-the-loop review step into the architecture
C. Overrule it since it slows down the workflow
D. Note it but exclude it from requirements since it's a policy matter, not technical

**Answer:** B
**Explanation:** Regulatory/compliance mandates from an authorized stakeholder must be captured as hard requirements shaping the system design, including mandatory review gates. Dismissing or deprioritizing compliance input (A, C, D) creates legal and patient-safety exposure.

### Q13.
An architect conducting discovery for a logistics firm identifies two conflicting goals: "minimize human review time" and "ensure zero misrouted shipments." What should the architect do?

A. Pick the goal that is easiest to implement
B. Surface the tension explicitly to stakeholders and define acceptable trade-off thresholds (e.g., acceptable review rate per risk tier)
C. Tell stakeholders both goals can be fully achieved simultaneously
D. Drop the zero-misroute goal since it's unrealistic

**Answer:** B
**Explanation:** Good discovery makes trade-offs visible and negotiated rather than silently resolved or falsely promised as fully compatible. Claiming both goals are fully achievable (C) sets up future stakeholder distrust.

### Q14.
A manufacturing client wants discovery to also capture technical constraints. Which of the following is the clearest example of a technical constraint?

A. "Executives want faster decision-making"
B. "The on-premises plant network cannot support outbound internet calls to external APIs for security reasons"
C. "Users want a friendlier chatbot tone"
D. "The project must be under budget"

**Answer:** B
**Explanation:** A network restriction preventing outbound API calls is a concrete technical/infrastructure constraint that directly limits architecture options (e.g., requiring on-prem or private-link deployment). The other options are business goals, UX preferences, or budget concerns, not technical constraints.

### Q15.
During discovery for a government benefits chatbot, the architect must identify all relevant stakeholders. Which group is MOST often overlooked but critical to include?

A. The procurement team signing the contract
B. Front-line caseworkers who will handle escalations the AI cannot resolve
C. The marketing team announcing the launch
D. The vendor's sales representative

**Answer:** B
**Explanation:** Front-line staff who absorb escalations are directly affected by system design (handoff quality, context transfer) and are frequently omitted from discovery despite being essential to workflow success. The other groups are involved but are not the ones whose daily workflow is most reshaped by the system.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
