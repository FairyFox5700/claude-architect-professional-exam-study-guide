# Objective 3: Select Architectural Patterns

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Select the most appropriate architectural pattern for a given problem among augmented LLM, prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer and autonomous agent architectures, and correctly judge when a fixed workflow is sufficient versus when an autonomous agent is warranted.

---

### Q1.
A customer support team wants Claude to answer billing questions using up-to-date account data and the ability to issue refunds through an API. Which pattern BEST fits this requirement?

A. Prompt chaining
B. Augmented LLM (LLM with retrieval and tool use)
C. Evaluator-optimizer
D. Orchestrator-workers

**Answer:** B
**Explanation:** The requirement is a single model call enhanced with retrieval (account data) and tool use (refund API), which is the definition of the augmented LLM pattern. The other patterns involve multiple coordinated steps or agents that are not needed for this single-turn, tool-augmented task.

### Q2.
A legal document pipeline must first classify a document type, then route it to one of three distinct specialized prompts (NDA, employment contract, lease) for review. Which pattern is MOST appropriate?

A. Routing
B. Parallelization
C. Autonomous agent
D. Augmented LLM only, with no routing logic

**Answer:** A
**Explanation:** Routing is the correct pattern when an initial classification step determines which of several specialized downstream prompts or workflows should handle the input, exactly as described. Parallelization would run multiple paths simultaneously regardless of type, an autonomous agent adds unneeded open-ended planning, and skipping routing logic would force one prompt to handle all three distinct document types poorly.

### Q3.
A financial services firm needs to translate the same disclosure document into 12 languages simultaneously, each translation being independent of the others. Which pattern BEST fits?

A. Orchestrator-workers with a dynamic, unknown number of subtasks decided at runtime
B. Parallelization, since the 12 translation tasks are fixed, independent and can run concurrently
C. Evaluator-optimizer, to iteratively refine a single translation
D. Autonomous agent, to decide which languages are necessary

**Answer:** B
**Explanation:** When subtasks are known in advance, independent of each other and fixed in number, parallelization (sectioning) is the simplest and most efficient pattern. Orchestrator-workers suits unpredictable, dynamically determined subtask sets, evaluator-optimizer targets iterative refinement rather than independent fan-out, and an autonomous agent is unnecessary overhead for a fixed, well-defined task list.

### Q4.
An engineering team is building a system where Claude must write a function, then a second pass critiques the function against a style guide and test coverage requirements, feeding corrections back until the code passes. Which pattern is this?

A. Routing
B. Evaluator-optimizer
C. Parallelization
D. Prompt chaining with no feedback step

**Answer:** B
**Explanation:** Iteratively generating an output and having a separate evaluation step provide structured feedback that drives refinement is the defining characteristic of the evaluator-optimizer pattern. Routing and parallelization do not involve iterative critique, and plain prompt chaining without a feedback loop would not re-evaluate and correct the output.

### Q5.
A research assistant tool must plan an unknown number of research sub-questions based on the user's query, which varies in scope every time, and then synthesize results from each. Which pattern BEST matches?

A. A fixed prompt chain with exactly three predetermined steps
B. Orchestrator-workers, where a central LLM call dynamically breaks down the task and delegates to worker calls, then synthesizes their outputs
C. Routing to one of two fixed prompts
D. A single augmented LLM call with no decomposition

**Answer:** B
**Explanation:** When the number and nature of subtasks cannot be known in advance and must be determined dynamically by the system itself, orchestrator-workers is the correct pattern, as the central orchestrator plans delegation at runtime. A fixed-step chain or two-way router cannot adapt to variable scope, and a single call would struggle to handle open-ended decomposition.

### Q6.
A manufacturing company wants a strict, repeatable sequence: extract measurements from a PDF, convert units, validate against tolerance ranges, then generate a compliance report. Each step's output feeds the next with no branching or dynamic decision-making. Which pattern fits BEST?

A. Autonomous agent, since it can decide the sequence itself
B. Prompt chaining, since the sequence is fixed and each step depends on the prior step's output
C. Parallelization, since each step is independent
D. Evaluator-optimizer, since the report needs refinement

**Answer:** B
**Explanation:** A fixed, linear sequence of dependent steps where each stage's output becomes the next stage's input is the textbook definition of prompt chaining. An autonomous agent is unwarranted overhead for a known fixed sequence, the steps here are explicitly dependent rather than independent (ruling out parallelization), and there is no iterative critique loop described (ruling out evaluator-optimizer).

### Q7.
Which scenario MOST justifies an autonomous agent architecture over a fixed workflow?

A. A monthly report that follows the exact same five steps every time with no variation
B. An open-ended IT troubleshooting assistant that must investigate an unknown number of possible root causes, choosing its own next action based on evolving evidence, until the issue is resolved
C. A form that converts structured fields into a PDF
D. A translation task with a known, fixed target language list

**Answer:** B
**Explanation:** Autonomous agents are justified when the task requires open-ended, dynamic decision-making about what to do next based on evolving context, which is exactly the nature of unpredictable troubleshooting. The other scenarios have fixed, predictable steps better served by a simpler workflow.

### Q8.
A SaaS company is deciding between a workflow and an agent for automated customer onboarding emails triggered by signup events. The sequence of emails and their timing are entirely fixed by business rules. What should the architect recommend, and why?

A. An autonomous agent, because agents are more modern
B. A fixed workflow (prompt chaining or simple augmented LLM calls), because the task has no genuine need for dynamic planning or tool selection
C. An orchestrator-workers pattern, to parallelize each email
D. An evaluator-optimizer, to iteratively rewrite each email indefinitely

**Answer:** B
**Explanation:** The core engineering principle is to use the simplest pattern that satisfies the requirements; since the email sequence and timing are fixed by business rules with no dynamic decision-making needed, a workflow is sufficient and more predictable, cheaper and easier to debug than an agent. The other options introduce unnecessary complexity or indefinite loops.

### Q9.
A healthcare system wants to summarize a patient chart, then separately and concurrently check for drug interaction warnings and insurance pre-authorization requirements, before combining all three outputs into a single care summary. Which pattern BEST matches this?

A. Sequential prompt chaining with one step after another
B. Parallelization (or an orchestrator-workers pattern if the three checks vary per case), since the three checks are independent and can run concurrently before being merged
C. Routing to only one of the three checks
D. A single evaluator-optimizer loop

**Answer:** B
**Explanation:** Because the three sub-analyses are independent of each other and all contribute to a combined final output, running them concurrently (parallelization, or orchestrator-workers if the exact checks vary by case) reduces latency compared to running them one after another. Sequential chaining would be slower without providing any benefit, routing would drop necessary checks, and an evaluator-optimizer loop does not match this fan-out/fan-in structure.

### Q10.
An architect is evaluating whether an autonomous agent is appropriate for a retail price-matching tool that checks three fixed competitor websites and applies a known discount formula. What is the BEST assessment?

A. An agent is appropriate because web scraping always requires autonomy
B. A workflow is sufficient because the competitor list and discount formula are fixed and known in advance, leaving no genuine need for the system to independently plan or decide its own steps
C. An agent is required because any tool use implies autonomy
D. Neither a workflow nor an agent is appropriate; this must be fully manual

**Answer:** B
**Explanation:** Fixed, known inputs and a deterministic formula mean the task does not require independent planning, so a simpler workflow pattern (augmented LLM calls plus deterministic logic) is more appropriate and controllable. A and C conflate tool use with the need for autonomy, which is a common architectural mistake, and D discards legitimate automation value.

### Q11.
A telecom company's network incident response system must dynamically decide, based on evolving diagnostic signals, which of dozens of possible remediation playbooks to investigate, potentially branching into sub-investigations whose number cannot be predicted. Which pattern BEST fits?

A. A fixed prompt chain of five steps
B. An autonomous agent architecture, since the number and nature of needed actions cannot be determined in advance and depend on evolving evidence
C. Simple routing between two playbooks
D. Parallelization across a fixed list of playbooks

**Answer:** B
**Explanation:** When the scope and sequence of actions genuinely cannot be predetermined and must adapt based on changing evidence, an autonomous agent's dynamic planning capability is warranted. The fixed chain, two-way router, and fixed parallel list all assume a predictability that this scenario explicitly lacks.

### Q12.
A government tax-filing assistant drafts a response to a citizen inquiry, then a second Claude call checks the draft against current tax code citations and flags any unsupported claims, triggering a revision if issues are found. What pattern is this an example of?

A. Routing
B. Evaluator-optimizer
C. Orchestrator-workers
D. Augmented LLM with no feedback

**Answer:** B
**Explanation:** A generation step paired with a dedicated evaluation step that triggers revision based on specific criteria is the evaluator-optimizer pattern. Routing directs to different paths rather than critiquing output, orchestrator-workers involves dynamic task decomposition rather than critique, and "no feedback" directly contradicts the described revision loop.

### Q13.
Which of the following is the STRONGEST argument against defaulting to an autonomous agent architecture for most enterprise workflows?

A. Agents cannot call external tools at all
B. Agents introduce additional cost, latency, and unpredictability from open-ended planning loops that are unnecessary when task steps and tools are already well understood
C. Agents are deprecated by Anthropic
D. Agents cannot be monitored or logged

**Answer:** B
**Explanation:** The core architectural trade-off is that autonomy brings flexibility at the cost of predictability, latency and spend, so it should be reserved for genuinely open-ended problems rather than applied by default. A, C and D are factually incorrect statements about agent capabilities.

### Q14.
A logistics company wants a system that generates route plans, where a separate step scores each candidate plan against fuel cost, delivery time and driver hours, iteratively refining the plan across several rounds until a scoring threshold is met. Which pattern fits BEST?

A. Routing
B. Evaluator-optimizer
C. Parallelization only, with no iteration
D. A single-shot augmented LLM call

**Answer:** B
**Explanation:** Iteratively generating candidate plans and refining them against explicit scoring criteria across multiple rounds is precisely the evaluator-optimizer pattern. Routing does not involve iterative refinement, parallelization without iteration does not match the described refinement loop, and a single-shot call cannot achieve the described iterative improvement.

### Q15.
A manufacturing client needs Claude to answer "what is our current inventory level for part X" by querying a live ERP system in real time within a single conversational turn. Which pattern is MOST appropriate?

A. Orchestrator-workers
B. Augmented LLM (tool use to query the ERP system)
C. Evaluator-optimizer
D. Prompt chaining across five fixed stages

**Answer:** B
**Explanation:** A single real-time lookup via a tool call within one turn is the archetypal augmented LLM use case, requiring no multi-step decomposition, critique loop, or dynamic delegation. The other patterns introduce structure and overhead that this straightforward single-call lookup does not need.

### Q16.
An architect is designing a compliance-review assistant where Claude must read a contract, extract clause-level risk flags, and then draft a summary memo that explicitly references earlier extracted flags and the reasoning behind each one established in the extraction step. A colleague proposes splitting extraction and drafting into two separate subagents to "keep each step focused." What is the BEST assessment of this proposal?

A. The split is correct because every multi-step task benefits from being handled by separate agents
B. The split is likely counterproductive here because the drafting step must carry forward the full reasoning context from extraction, and splitting into separate agents is what would lose that context; this work should stay within a single call or chain rather than being distributed across isolated agents
C. The split is correct because subagents always reduce token consumption
D. The split is irrelevant because Claude cannot perform extraction and drafting in the same session

**Answer:** B
**Explanation:** Work that must carry context from one step to the next is a reason to keep it together rather than split it, because distributing it into separately scoped subagents is precisely what strips away the shared context each step depends on; subagents are better suited to genuinely parallel or isolated workstreams. A and C are false generalizations about when splitting helps, and D misstates a technical limitation that does not exist.

### Q17.
A finance team's expense-approval workflow currently has Claude make a separate model call to check each of 200 employees' budget status against a shared ledger, one employee at a time, resulting in 200 slow, costly round trips for a single monthly report. What is the BEST architectural fix?

A. Switch to an autonomous agent so it can decide how to check each employee more intelligently
B. Have Claude generate and execute a single script that calls the budget-check tool across all 200 employees programmatically in one pass, replacing 200 separate model round trips with one
C. Increase the model's context window so all 200 employees fit in one prompt
D. Add a fifth parallel subagent dedicated to budget checks with no change to the per-employee calling pattern

**Answer:** B
**Explanation:** When the same tool is called repeatedly over a list, the structural fix is to move the loop into code the model writes and executes once, collapsing many round trips into a single script rather than making the agent "smarter" or adding more parallel agents. A and D do not address the repeated round-trip problem, and C conflates context size with the actual inefficiency of per-item tool invocation.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
