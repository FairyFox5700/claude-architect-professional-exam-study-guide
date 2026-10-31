# Domain 1: Solution Design & Architecture

[← Back to index](../README.md)

## Exam objectives covered

1. Translate a stated business problem into a Claude-based solution by identifying the actual underlying problem, defining the users, inputs, outputs and expected outcomes, distinguishing which subtasks genuinely require an LLM versus deterministic software, establishing measurable success criteria and business KPIs, and assessing feasibility, risk and organizational constraints before committing to an architecture.
2. Design complete end-to-end architectures that trace the full lifecycle from input through processing to output and feedback, clearly identifying where Claude, backend services and human reviewers each participate, incorporating validation and error-handling paths at every stage, and closing the loop with feedback mechanisms that improve future system performance.
3. Select the most appropriate architectural pattern for a given problem among augmented LLM, prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer and autonomous agent architectures, and correctly judge when a fixed workflow is sufficient versus when an autonomous agent is warranted.
4. Design multi-agent systems using coordinator and subagent architectures, including task delegation and decomposition, choices between parallel and sequential execution, context passing between agents, clearly scoped agent responsibilities and tool access, management of token consumption, concurrency and execution limits, and handling of failed or incomplete subagent runs.
5. Apply task decomposition techniques by breaking complex tasks into independent subtasks, identifying dependencies between them, defining clear contracts between components, ensuring each step is independently testable, and deciding which subtasks should run in parallel versus sequentially.
6. Align Claude-based architecture decisions with measurable business value, including efficiency gains, productivity improvements, broader business transformation, cost reduction, performance against service-level agreements, and demonstrable return on investment tied to business impact.

---

### Q1.
A financial services company asks for "an AI system to process 10,000 invoices daily." Discovery reveals that invoice data extraction needs language understanding, numerical validation must be exact, payment-status checks query an external API, and high-value payments need human sign-off. Which architecture decomposition is MOST appropriate?

A. One Claude call performs extraction, validation, status checks and approval together for maximum simplicity
B. Claude extracts invoice data, deterministic code validates the numbers, a backend API checks payment status, and a human approves high-value payments, with independent invoices processed in parallel
C. An autonomous agent handles the entire pipeline so it can adapt the process however it sees fit
D. A human performs all four steps manually since invoices are sensitive financial documents

**Answer:** B
**Explanation:** Each subtask is matched to the tool best suited for it — language understanding to Claude, exact calculation to deterministic code, live data to an API, and risk-bearing decisions to a human — while independent invoices are parallelized for throughput, reflecting sound decomposition and pattern selection. A collapses distinct responsibilities into one ungoverned call, C introduces unneeded and risky autonomy over a well-understood process, and D discards legitimate automation value.

### Q2.
A SaaS company's leadership says, "just build an agent, agents are the future." The architect discovers the actual task — generating weekly usage reports — follows an identical five-step process every time with no variation. What is the architect's BEST response?

A. Comply immediately since leadership has already decided on the architecture
B. Explain that a fixed prompt chain or simple workflow is more appropriate here because the task has no genuine need for dynamic planning, and reserve agents for problems with real uncertainty in scope or sequence
C. Refuse to engage with leadership on architecture questions
D. Build an agent but silently constrain it to the five fixed steps internally

**Answer:** B
**Explanation:** Part of sound architectural judgment is pushing back, with clear technical reasoning, against a default toward unnecessary complexity when a simpler, more predictable and cheaper pattern suffices for a fixed, well-understood task. A abdicates professional judgment, C fails to engage constructively, and D builds unneeded complexity while pretending otherwise, which adds cost and risk without transparency.

### Q3.
A healthcare provider's end-to-end design has Claude draft a care summary, after which a nurse reviews it before it enters the patient record. The nurse reports that 80% of her edits are the same two types of correction every time. What should the architect do to close the feedback loop?

A. Ignore the pattern since manual review is already in place
B. Analyze the recurring correction types and use them to refine the prompt, extraction instructions or few-shot examples so the draft quality improves and review burden decreases over time
C. Remove the nurse review step since Claude is already "good enough"
D. Increase the summary length to cover more detail regardless of the correction pattern

**Answer:** B
**Explanation:** A recurring, specific correction pattern is exactly the kind of structured signal a feedback loop should capture and use to systematically improve the upstream generation step, reducing review burden while preserving the safety net. A wastes a valuable improvement signal, C removes a necessary clinical safety check, and D does not address the actual identified problem.

### Q4.
A government agency wants Claude to independently investigate an unknown number of possible causes behind an unexplained drop in benefit-application completion rates, deciding its own next steps based on what it finds. Which pattern is MOST appropriate, and why?

A. Prompt chaining, because the investigation should follow a fixed five-step process
B. Autonomous agent, because the number and nature of investigative steps cannot be predetermined and must adapt to evolving findings
C. Parallelization, because all possible causes should be checked simultaneously regardless of relevance
D. Routing, because there are only two possible causes to choose between

**Answer:** B
**Explanation:** Genuinely open-ended investigation where the next step depends on what was just discovered, and where the scope cannot be fixed in advance, is the scenario that justifies an autonomous agent's dynamic planning capability. The other patterns all assume a predictability (fixed steps, a fixed exhaustive list, or a small fixed choice set) that contradicts the described uncertainty.

### Q5.
A retail company's multi-agent product-research system has a coordinator delegating to five subagents, one per product category. Each subagent is given access to the pricing-update API even though only the pricing-analysis subagent needs it. What risk does this illustrate, and what is the fix?

A. No risk exists; broad tool access simplifies configuration
B. This violates least-privilege, risking unintended price changes by subagents with no legitimate need; the fix is to scope tool access per subagent to only what each one's task requires
C. The risk is that the coordinator will run out of tokens
D. The fix is to remove the coordinator entirely

**Answer:** B
**Explanation:** Granting a high-impact, potentially irreversible tool (price updates) to subagents whose tasks do not require it creates real operational risk; access should be scoped per subagent according to the principle of least privilege. A dismisses a legitimate risk, and C and D misdiagnose or fail to address the actual problem.

### Q6.
An insurance company is decomposing a subrogation-claim workflow and identifies two subtasks: "determine fault percentage from accident report" and "calculate recoverable amount based on fault percentage and policy limits." Which statement about their relationship is correct?

A. They are independent and should run in parallel
B. The second subtask has a hard dependency on the first subtask's output and must run after it completes
C. They should be merged into a single undifferentiated subtask for efficiency
D. Neither subtask requires a defined contract since both are "simple" calculations

**Answer:** B
**Explanation:** The recoverable amount calculation explicitly requires the fault percentage as an input, creating a genuine sequential dependency that must be respected; running them in parallel would produce incorrect or incomplete results. C loses the benefits of separate testability and clear ownership, and D is incorrect since even simple-looking steps benefit from an explicit input/output contract.

### Q7.
A manufacturing executive wants to know whether a newly deployed Claude-based quality-inspection assistant delivered "efficiency" or "transformation." The tool performs the same inspections 30% faster with the same pass/fail criteria. How should the architect characterize this result?

A. As business transformation, since any AI deployment is transformative by definition
B. As an efficiency gain, since the same work is being completed with the same scope and criteria but using fewer resources or less time
C. As a cost increase, since AI projects always increase operating expense
D. As irrelevant, since efficiency gains do not matter to leadership

**Answer:** B
**Explanation:** Delivering the same inspection scope and outcome criteria in less time is the definition of an efficiency gain rather than a transformation, which would require a fundamentally new capability or business model; accurate characterization matters for setting stakeholder expectations. A overstates the result, and C and D are incorrect or dismissive mischaracterizations.

### Q8.
A telecom company's architect must decide where to place human review in an automated SIM-swap fraud-prevention workflow, given that SIM swaps are a known vector for account takeover fraud. What is the BEST placement?

A. No human review anywhere, to maximize processing speed
B. Human review only for requests flagged as high-risk by a deterministic risk-scoring step that follows Claude's extraction of request details, so low-risk routine requests process quickly while risky ones get scrutiny
C. Human review of every single SIM-swap request regardless of risk level
D. Human review only of the system's server logs, not the actual requests

**Answer:** B
**Explanation:** Targeting human review at the genuinely high-risk subset, identified through a deterministic scoring step, balances fraud risk mitigation with operational efficiency, which is the correct placement principle. A ignores a known high-stakes fraud vector, C wastes human capacity on low-risk cases and slows the whole system, and D misapplies review to the wrong artifact.

### Q9.
A logistics company's architect is weighing a $200,000/year multi-agent routing system against the current $140,000/year single-call augmented LLM system. The multi-agent system is projected to reduce fuel costs by $35,000/year with no other measurable benefit. What should the architect recommend?

A. Adopt the multi-agent system regardless of the numbers since more sophisticated architecture is inherently better
B. Recommend against the multi-agent system, since its $60,000 higher annual cost exceeds its $35,000 projected benefit, and suggest investigating whether a lower-cost architecture could capture a similar fuel-cost benefit
C. Adopt the multi-agent system and ignore the cost difference in reporting to leadership
D. Cancel all further investment in route optimization

**Answer:** B
**Explanation:** A sound recommendation nets cost against quantified benefit; here the proposed system costs more than it saves, so the architect should recommend against it while still pursuing the underlying fuel-cost opportunity through a more cost-effective design. A ignores the numbers, C is dishonest, and D abandons a legitimate opportunity rather than right-sizing the approach.

### Q10.
A legal firm's contract-review pipeline decomposes into "extract clauses," "classify clause risk," and "draft negotiation suggestions." Testing shows clause extraction occasionally misses clauses buried in unusual formatting, causing downstream risk classification to be incomplete. Where should the architect add validation?

A. Only at the very final step, checking the negotiation suggestions' tone
B. Immediately after the extraction step, validating extraction completeness (e.g., against expected clause-count heuristics or a secondary pass) before passing results downstream
C. Nowhere, since the error rate is probably acceptable
D. Before the document even reaches the pipeline, by asking the client to reformat every contract

**Answer:** B
**Explanation:** Validation should be placed as close as possible to where the error originates — immediately after extraction — to catch incompleteness before it silently propagates into downstream risk classification and negotiation drafting. A catches the problem far too late, C accepts a known failure mode without justification, and D is impractical and shifts an engineering problem onto clients.

### Q11.
An architect is designing a customer-feedback-analysis system for a consumer electronics brand. The task requires summarizing themes from 500,000 reviews, each independent of the others, with no need for the reviews to inform one another's summary. Which combination of pattern and execution strategy is BEST?

A. Prompt chaining with sequential processing of all 500,000 reviews one at a time
B. Parallelization (or orchestrator-workers for batching), processing independent batches of reviews concurrently, then synthesizing theme summaries across batches
C. A single Claude call containing all 500,000 reviews in one prompt
D. An autonomous agent that decides which reviews to read based on its own preferences

**Answer:** B
**Explanation:** Since the reviews are independent and the volume is large, batching them into concurrent parallel subtasks (a parallelization or orchestrator-workers pattern) with a final synthesis step is both correct and efficient. A wastes available parallelism, C would exceed practical context limits and mix unrelated content, and D introduces unwarranted and unpredictable autonomy for a task with no genuine need for independent planning.

### Q12.
A government benefits agency's multi-agent eligibility-review system has a coordinator delegating three subagents: income verification, residency verification, and dependent verification. During a production incident, the residency-verification subagent fails due to an external registry outage, while the other two succeed. What is the BEST coordinator behavior?

A. Discard all three subagents' results and restart from scratch
B. Retain the successful income and dependent verification results, flag the residency verification as incomplete due to the external outage, and either retry or escalate that specific piece to a human reviewer
C. Fabricate a plausible residency verification result to keep the process moving
D. Permanently mark the applicant as ineligible due to the failure

**Answer:** B
**Explanation:** Isolating the failure to the specific failed subagent, preserving valid completed work, and retrying or escalating only the failed piece reflects resilient multi-agent failure handling. A wastes valid results unnecessarily, C introduces dangerous fabricated data into an eligibility determination, and D makes an unjustified adverse decision based on an infrastructure failure rather than the facts of the case.

### Q13.
A manufacturing company wants its supplier-contract-risk-assessment tool to improve over time as more contracts are reviewed. Which design choice BEST reflects a genuine feedback loop, as opposed to superficial logging?

A. Storing every input and output in a database with no further use
B. Using analyst corrections and overrides of Claude's risk flags as a labeled dataset to periodically refine the flagging prompts or criteria, measurably reducing false positives and false negatives over subsequent quarters
C. Deleting old assessment records every month to save storage
D. Re-running the identical prompt on the same test contracts repeatedly with no new data

**Answer:** B
**Explanation:** A genuine feedback loop uses structured outcome data, specifically analyst corrections, to drive measurable improvement in future performance, closing the lifecycle rather than merely recording history. A is passive logging without action, C destroys the data needed for improvement, and D produces no new information to learn from.

### Q14.
An architect at an airline is deciding between a workflow and a multi-agent system for a tool that checks flight status, baggage status, and rebooking options for a single passenger's single inquiry, where all three checks are independent lookups against known APIs. What is the MOST architecturally sound choice?

A. A multi-agent system with a coordinator and three separate subagents, each requiring its own context window and token budget
B. A single augmented LLM call with three parallel tool calls within one turn, since the task is well-defined, bounded and does not require independent planning or separate agent context
C. A fully autonomous agent empowered to rebook the passenger without review
D. Three entirely separate conversations with no shared context at all

**Answer:** B
**Explanation:** When subtasks are simple, bounded, well-defined tool calls within a single user turn, the augmented LLM pattern with parallel tool calls is simpler, cheaper and equally effective compared to spinning up a full multi-agent architecture, which would add unnecessary coordination overhead. A over-engineers a simple bounded task, C introduces unreviewed autonomous action on a customer-impacting change, and D needlessly fragments a single coherent inquiry.

### Q15.
A retail bank reports to its board that a new Claude-based fraud-alert-drafting tool "generated 50,000 alerts last quarter." The board asks for the business case to justify renewal. What additional information is MOST critical to include?

A. The exact wording of the system prompt used
B. The dollar value of fraud losses prevented or reduced, analyst time saved per alert reviewed, and the tool's total operating cost, compared against the prior process
C. The number of distinct Claude model versions tested during development
D. The size of the engineering team that built the tool

**Answer:** B
**Explanation:** A credible business case requires translating raw activity volume into financial and operational impact — fraud losses prevented, labor saved, and cost — so the board can evaluate ROI, rather than citing technical or team-size details that do not speak to business value. A, C and D are implementation details irrelevant to a renewal business case.

### Q16.
A hospital's discharge-summary assistant was scoped so that Claude drafts the summary, a deterministic terminology-coding step adds standardized diagnosis codes, and a physician signs off before the record is finalized. A new team member suggests removing the physician sign-off "to save time." What is the BEST response?

A. Agree immediately since the physician step is the slowest part of the pipeline
B. Explain that physician sign-off is a required validation and accountability gate for clinical correctness and liability, and that removing it would eliminate necessary error-handling for a high-stakes output, undermining the end-to-end design's safety
C. Agree, but only for patients under a certain age
D. Replace the physician with a second Claude call for speed

**Answer:** B
**Explanation:** The physician sign-off is a deliberate validation gate placed at the highest-stakes point in the lifecycle, and removing it for speed would eliminate necessary error-handling and accountability for clinical content, which is an unacceptable trade-off. A and C treat a safety-critical control as negotiable for arbitrary reasons, and D substitutes a non-equivalent, non-licensed check for a required human clinical judgment.

### Q17.
A logistics company's task-decomposition review identifies that "generate shipping label" and "calculate shipping cost" are currently bundled into a single subtask. An architect recommends splitting them. What is the STRONGEST justification?

A. Splitting always improves performance regardless of content
B. The two concerns have different inputs, different failure modes, and different rates of change (carrier rate tables change frequently, label templates rarely), so separating them into independently testable units with clear contracts reduces the risk and cost of future changes
C. Splitting makes the system diagram have more boxes, which auditors prefer
D. The two tasks cannot both be performed by Claude

**Answer:** B
**Explanation:** Good decomposition separates concerns that change at different rates or have distinct failure modes into independently testable units with explicit contracts, directly reducing the blast radius and cost of future changes such as a carrier rate update. A is an unsupported generalization, and C and D are not legitimate technical justifications.

### Q18.
A manufacturing company's architect must recommend whether to pursue an evaluator-optimizer pattern for a technical-specification-writing assistant used by engineers, where early drafts frequently fail an internal completeness checklist and require rework. What is the BEST justification for this pattern here?

A. Evaluator-optimizer is justified because the task benefits from an explicit, repeatable critique step (the completeness checklist) that can drive automatic iterative revision before a draft reaches an engineer, reducing manual rework cycles
B. Evaluator-optimizer should be avoided because iteration always increases cost with no benefit
C. A single-shot augmented LLM call is sufficient because checklists are not relevant to pattern selection
D. Routing is the correct pattern because the checklist determines which of several unrelated prompts to use

**Answer:** A
**Explanation:** When there is a well-defined, repeatable evaluation criterion (the completeness checklist) and documented evidence that first drafts frequently fail it, structuring the system as generate-then-critique-then-revise directly targets the observed rework problem and is the textbook justification for evaluator-optimizer. B dismisses a real, measurable benefit, C ignores the explicit evaluation signal, and D misapplies routing, which selects between distinct paths rather than iteratively refining a single draft.
