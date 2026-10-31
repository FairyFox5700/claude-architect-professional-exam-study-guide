# Objective 1: Translate Business Problems into Claude-Based Solutions

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Translate a stated business problem into a Claude-based solution by identifying the actual underlying problem, defining the users, inputs, outputs and expected outcomes, distinguishing which subtasks genuinely require an LLM versus deterministic software, establishing measurable success criteria and business KPIs, and assessing feasibility, risk and organizational constraints before committing to an architecture.

---

### Q1.
A regional hospital network asks an architect to "add an AI chatbot to our patient portal." Initial interviews reveal that the real driver is a 40% call-center abandonment rate caused by patients unable to find appointment and billing information. What is the architect's BEST first step?

A. Begin prototyping a conversational Claude agent immediately since the client explicitly requested a chatbot
B. Reframe the engagement around reducing call-center abandonment and validate which parts of that journey actually require natural-language understanding
C. Propose a multi-agent system so the chatbot can simultaneously handle appointments, billing and clinical triage
D. Recommend deferring any AI work until the call center adds more staff

**Answer:** B
**Explanation:** The stated request ("a chatbot") is a solution, not the problem; the real business problem is abandonment driven by discoverability friction. Reframing around the measurable business outcome ensures the eventual architecture is evaluated against the right target. A and C jump to solutioning before the problem is validated, and D ignores that the business explicitly wants a technology-assisted fix.

### Q2.
An insurance carrier wants Claude to "decide" whether a claim should be paid. During discovery, the architect learns that claim payout thresholds are governed by fixed regulatory tables and policy limits with no interpretive ambiguity. What should the architecture recommendation be?

A. Use Claude as the sole decision-maker because it can reason over claim documents holistically
B. Use Claude to extract and summarize unstructured claim details, and apply the payout threshold logic in deterministic code
C. Use an autonomous agent with tool access to the payout system so it can self-correct mistakes
D. Avoid Claude entirely since the task is well-defined

**Answer:** B
**Explanation:** Extracting information from unstructured claim narratives (forms, adjuster notes, photos) is a natural fit for an LLM, but applying fixed regulatory thresholds is deterministic and should never be delegated to a probabilistic model. Options A and C introduce unnecessary non-determinism into a compliance-sensitive calculation, and D discards the genuine LLM-suited extraction work.

### Q3.
A logistics company wants to reduce the average time to resolve customer shipment inquiries. Which artifact should the architect produce FIRST when translating this into a solution design?

A. A detailed prompt library for the support agent
B. A problem statement that defines current baseline resolution time, target resolution time, the user population and the inputs/outputs of the desired workflow
C. A cost estimate for Claude API usage at current ticket volume
D. A list of all tools the agent will need access to

**Answer:** B
**Explanation:** Before any prompt, tool, or cost work, the architect needs a crisp problem statement with baseline and target metrics, users, and input/output definitions — this anchors every downstream design decision and prevents scope drift. The other artifacts are useful but premature without this foundation.

### Q4.
A manufacturing firm's quality team wants an LLM-based system to "catch all production defects before shipment." What is the PRIMARY feasibility risk the architect must surface before proceeding?

A. Claude cannot process images of defective parts
B. The desired outcome implies a near-zero false-negative guarantee that a probabilistic language model cannot responsibly promise, especially without grounding in deterministic sensor data
C. The project will take longer than six months
D. Defect detection does not require a success metric

**Answer:** B
**Explanation:** Framing "catch all defects" as an absolute guarantee sets an unachievable bar for any probabilistic system; the architect must negotiate realistic precision/recall targets and combine the LLM with deterministic sensor thresholds or human review for edge cases. The other options either misstate a technical limitation or dismiss the need for rigor.

### Q5.
A legal services firm asks for a solution to "review contracts faster." Which pair of questions is MOST important for the architect to ask before any design begins?

A. Which cloud provider does the firm currently use, and what is their support contract tier
B. Who are the end users of the review output, and what does "faster" mean in measurable terms (e.g., turnaround hours, reviewer hours saved)
C. How many attorneys are employed by the firm
D. What color scheme should the review dashboard use

**Answer:** B
**Explanation:** Defining the actual users and a measurable definition of "faster" converts a vague request into a scoped, testable objective, which is essential before selecting any architecture. The remaining options are implementation or cosmetic details irrelevant at this stage.

### Q6.
A telecom provider wants to automate tier-1 support ticket triage. The architect determines that ticket categorization needs judgment about ambiguous customer language, but ticket routing to the correct queue is a simple lookup once a category is known. How should responsibilities be split?

A. Claude performs both categorization and routing since it already read the ticket
B. Claude performs categorization only; a deterministic routing table maps category to queue
C. A human performs categorization; Claude performs routing
D. Neither task needs Claude since ticket triage is a solved problem

**Answer:** B
**Explanation:** Categorizing ambiguous natural language is squarely an LLM strength, while mapping a known category to a queue is a simple deterministic lookup that should not involve a model call, preserving latency, cost and predictability. C inverts the natural strengths, and D ignores the genuine need for language understanding in triage.

### Q7.
During discovery with a government benefits agency, the architect learns that any automated eligibility determination must be fully explainable and auditable under statute. What is the BEST architectural implication?

A. Use Claude to generate a final eligibility decision with a natural-language justification only
B. Use Claude strictly for extracting and normalizing applicant data, and compute eligibility with transparent deterministic rules whose logic can be audited line by line
C. Avoid any automation and keep the process fully manual
D. Use an autonomous multi-agent system so multiple models can cross-check each other's decisions

**Answer:** B
**Explanation:** Regulatory auditability requires a decision path that can be inspected and reproduced exactly, which deterministic rules provide and LLM-generated justifications do not; Claude still adds value by handling unstructured intake. A risks ungrounded or inconsistent decisions, C discards automation value unnecessarily, and D adds complexity without solving the auditability requirement.

### Q8.
A retail chain's stated goal is "use AI to improve customer experience." Which action BEST demonstrates proper business-problem translation?

A. Immediately proposing a conversational shopping assistant because it is a popular use case
B. Running structured stakeholder interviews to identify a specific friction point (e.g., return-policy confusion) and a corresponding measurable KPI
C. Benchmarking Claude against competitor models before any requirements are gathered
D. Building a proof of concept for every retail use case Claude could theoretically support

**Answer:** B
**Explanation:** Vague aspirational goals must be decomposed into a specific, measurable problem before any solution is chosen; stakeholder interviews surface the real friction point and a KPI to validate against. A and D are premature solutioning, and C is a model-selection activity that comes later.

### Q9.
A SaaS company's engineering lead insists every customer support ticket should be handled by an autonomous Claude agent because "agents are more powerful." The architect disagrees. What is the strongest justification for pushing back?

A. Agents are always slower than workflows regardless of task
B. Many support tickets follow a small number of predictable resolution paths better served by a deterministic or lightly-augmented workflow, and defaulting to full autonomy adds cost, latency and unpredictability without added benefit
C. Claude cannot be used for customer support under its usage policies
D. Autonomous agents cannot call external tools

**Answer:** B
**Explanation:** Matching the simplest architecture to the task's actual variability is a core principle; most support tickets do not require open-ended autonomous planning, so an agent is architectural overkill that increases cost and reduces predictability. A, C and D are factually incorrect generalizations.

### Q10.
An architect is asked to define success criteria for a Claude-based document summarization tool used by financial analysts. Which metric set BEST reflects proper KPI definition?

A. Number of API calls made per day
B. Analyst time saved per report, factual accuracy against source documents, and analyst satisfaction score
C. The number of lines of code in the integration
D. The model's context window size

**Answer:** B
**Explanation:** Good KPIs tie directly to business outcomes (time saved, accuracy, satisfaction) rather than technical or implementation metrics that say nothing about value delivered. A, C and D are infrastructure details, not business success measures.

### Q11.
A procurement team at a manufacturing company wants Claude to automatically approve purchase orders under $500. Legal flags this as a compliance concern because approval authority is regulated. What should the architect do?

A. Proceed as requested since the dollar threshold is low risk
B. Treat this as a constraint discovered during feasibility assessment, and redesign so Claude drafts a recommendation that a human approver confirms, preserving the required approval authority
C. Cancel the project entirely
D. Replace the human approver with a second Claude call for redundancy

**Answer:** B
**Explanation:** Surfacing and respecting regulatory/organizational constraints during the feasibility phase is a core part of problem translation; a human-in-the-loop approval step satisfies the legal constraint while still delivering automation value via drafting. A ignores the compliance flag, C over-reacts by abandoning value entirely, and D does not address the authority requirement at all.

### Q12.
A customer wants "Claude to write all our marketing copy end to end with zero human review" for a regulated pharmaceutical brand. What risk should the architect prioritize in the feasibility assessment?

A. Token cost per generated article
B. The risk of generating non-compliant medical claims that violate advertising regulations without a review gate
C. Claude's inability to use British versus American English spelling
D. The marketing team's current satisfaction with their CMS tool

**Answer:** B
**Explanation:** In a regulated industry, ungated generative output creates material compliance and brand risk, which must be weighed above stylistic or tooling concerns during feasibility assessment. The other options are minor compared to regulatory exposure.

### Q13.
Which scenario represents a task that should NOT be delegated to Claude, based on sound business-problem translation?

A. Summarizing lengthy customer feedback transcripts into themes
B. Drafting a first version of a customer response email
C. Calculating exact tax withholding amounts for payroll according to a fixed statutory formula
D. Classifying inbound emails by topic

**Answer:** C
**Explanation:** Exact statutory tax calculations are deterministic, must be reproducible precisely, and have zero tolerance for probabilistic variance, making them unsuitable for an LLM; they belong in deterministic code. The other tasks involve language understanding or generation, which are appropriate LLM uses.

### Q14.
An architect is scoping a project for an airline's baggage-claim support team. Which output of the discovery phase would be considered incomplete?

A. A defined list of input types (claim forms, photos, flight data) and expected outputs (resolution emails, compensation decisions)
B. A list of the users who will interact with the system and their respective permission levels
C. A high-level architecture diagram with no problem statement or success metric attached
D. A documented list of constraints including data residency requirements for passenger data

**Answer:** C
**Explanation:** An architecture diagram without a grounding problem statement or measurable success criteria cannot be validated or justified, making the discovery output incomplete regardless of its technical polish. A, B and D are each legitimate, necessary discovery artifacts.

### Q15.
A nonprofit asks Claude architecture consultants to "automate grant writing." After analysis, the architect finds that grant requirements vary widely per funder, writers currently spend 70% of their time on research rather than drafting, and leadership measures success by number of grants submitted per quarter. What is the BEST translated problem statement?

A. Build an autonomous agent that submits grants on the organization's behalf without review
B. Reduce writer research time by using Claude with retrieval over funder requirement documents, keeping drafting and submission under human control, to increase grants submitted per quarter
C. Replace the grant-writing team with a single Claude prompt template
D. Focus only on improving the visual formatting of submitted grant documents

**Answer:** B
**Explanation:** This statement directly targets the real bottleneck (research time), ties to the leadership-defined KPI (grants per quarter), and appropriately scopes Claude's role while keeping human judgment over submission — a faithful translation of the discovery findings. A removes necessary oversight, C ignores the nuance of varying funder requirements, and D addresses a non-issue.

### Q16.
During a feasibility assessment for a retailer's returns-automation proposal, an architect concludes the system cannot be built within the current data-access constraints, but notes that if the warehouse system exposed a real-time inventory API, the proposal would become buildable. How should this verdict be recorded?

A. As a flat "no," since the system cannot be built today under any circumstances
B. As a "yes, if" verdict that explicitly names the missing real-time inventory API as the condition, with an owner assigned to pursue making that API available
C. As a "yes," since the architect is confident the API will eventually exist
D. As an informal note in a meeting, since feasibility verdicts do not need to be written down

**Answer:** B
**Explanation:** A feasibility verdict has three legitimate outcomes — yes, yes-if, and no — and a "yes, if" is only useful when the specific condition that would change the answer is written down with an accountable owner, otherwise it quietly decays into an unconditional "yes." A incorrectly treats a conditional blocker as a permanent one, C skips past a real unmet constraint, and D fails to treat the verdict as the documented deliverable it must be.

### Q17.
An architect scoping a contract-analysis tool for a law firm wants to know, before writing any code, whether the firm's longest contracts (some exceeding 400 pages) will fit within a single model request alongside the firm's required system instructions and extraction tool definitions. What is the BEST way to establish this?

A. Estimate token count by eye based on page count and proceed with the design
B. Use the token-counting capability to measure the actual input size (including system prompt, tools and documents) against the target model's context window before committing to a single-call design, and treat the result as a structural constraint rather than a tuning problem if it does not fit
C. Assume it will fit because Claude has a large context window in general
D. Wait until the system is in production to discover whether any contracts are too large

**Answer:** B
**Explanation:** Sizing is arithmetic that can and should be done before any design is committed to: measuring actual token counts for real documents against the model's context window turns a guess into a verified constraint, and if a unit of work does not fit, that is a structural finding requiring retrieval or decomposition, not a prompt-tuning fix. A and C substitute assumption for measurement, and D defers a discoverable risk into costly production failure.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
