# Objective 7: Select Claude Models Based on Trade-Offs

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Select Claude models based on capability, latency, and cost trade-offs, including reasoning/effort settings, migration strategy, and model assignment across stages of an agentic workflow.

---

### Q1.
A logistics company is building a route-optimization agent that must plan multi-leg shipments across dozens of constraints (fuel cost, driver hours, customs rules, weather) and revise its plan repeatedly before committing. Which model is the BEST fit for the core planning step?

A. Haiku, because the agent must respond within milliseconds
B. Opus, because the task requires deep multi-step reasoning across many interacting constraints
C. Sonnet, because it is the default model and requires no justification
D. Any model, since routing problems are purely deterministic and model choice does not matter

**Answer:** B
**Explanation:** Complex, constraint-heavy planning with many interacting variables benefits from Opus's stronger reasoning depth. Haiku optimizes for speed over depth, Sonnet is a reasonable balanced choice but not the strongest reasoner, and routing with many soft constraints is not purely deterministic.

### Q2.
A telecom provider runs a chatbot that classifies millions of inbound SMS messages per day into one of 10 intent categories before routing them. Cost and latency are the dominant concerns, and accuracy requirements are modest. Which model is MOST appropriate?

A. Opus, to guarantee maximum classification accuracy
B. Haiku, because high-volume, low-latency classification tasks favor the fastest, cheapest model
C. Sonnet, because it is always a safe middle-ground choice regardless of workload shape
D. Whichever model has the largest context window, since message volume is high

**Answer:** B
**Explanation:** High-volume, low-complexity classification is the canonical Haiku use case: it is fast and cheap while still being accurate enough for simple categorization. Opus would be unnecessarily expensive and slower; Sonnet is overkill for the task's complexity; context window size is irrelevant to short SMS classification.

### Q3.
An insurance company's claims-processing pipeline has three stages: (1) extract structured fields from scanned documents, (2) reason about coverage eligibility against policy language, and (3) draft a plain-language explanation letter to the customer. An architect is deciding whether to use one model for all three stages or different models per stage. What is the BEST approach?

A. Use Opus for all three stages to maximize quality everywhere
B. Use Haiku for all three stages to minimize cost
C. Match each stage to its complexity: Haiku or Sonnet for extraction, Opus (or Sonnet) for eligibility reasoning, and Sonnet/Haiku for drafting
D. Use a single random model per request to average out cost and quality

**Answer:** C
**Explanation:** Agentic workflows benefit from assigning the strongest model only where reasoning complexity demands it (eligibility judgment) while using faster/cheaper models for mechanical extraction and formulaic drafting. Using Opus everywhere wastes cost and latency budget; using Haiku everywhere risks poor eligibility judgments; random assignment is not a defensible architectural decision.

### Q4.
A hospital system is evaluating whether to upgrade a clinical-notes summarization agent from an older Claude model to a newer generation model. What is the PRIMARY risk the architect should validate before switching in production?

A. The newer model will definitely be slower in all cases
B. Behavioral drift: the new model may summarize or phrase clinical content differently, which could affect downstream consumers or compliance reviews
C. Newer models cannot be used with system prompts
D. Model upgrades always require rewriting every tool definition from scratch

**Answer:** B
**Explanation:** Model upgrades can shift output style, verbosity, or judgment calls even when overall quality improves, which matters enormously in regulated domains like healthcare. Speed is not guaranteed to regress, system prompts remain supported, and tool definitions typically do not need a full rewrite for a model swap.

### Q5.
A legal tech vendor wants to reduce cost on a contract-clause-tagging feature that currently uses Opus for every request. Internal review shows the task is well-specified, has clear labeling rules, and rarely requires multi-step reasoning. What should the architect do?

A. Keep Opus because legal content always requires the most capable model regardless of task shape
B. Evaluate downgrading to Sonnet or Haiku with representative test cases, since task complexity—not domain sensitivity alone—should drive model selection
C. Switch immediately to Haiku without testing, since cost reduction is the only goal
D. Increase the reasoning/effort setting instead of considering a smaller model, since effort tuning is always cheaper than switching models

**Answer:** B
**Explanation:** Model selection should be driven by task complexity, validated empirically, rather than assuming domain sensitivity alone requires the largest model. Blind assumptions in either direction (never downgrade, or downgrade untested) are risky, and raising effort on an oversized model does not address the root cost issue.

### Q6.
An architect is designing an agentic coding assistant with three internal phases: planning the change, writing the code, and running/interpreting test output. Which staged model assignment best balances cost and quality?

A. Use Opus only for the planning phase where architectural reasoning matters most, and Sonnet for code generation and test-output interpretation
B. Use Haiku for planning since it is the first and simplest-looking step
C. Use the same model for every phase to simplify observability, regardless of cost
D. Use Opus for test-output interpretation only, since logs are the largest input

**Answer:** A
**Explanation:** Planning often requires the deepest reasoning about trade-offs and architecture, making it a good candidate for the strongest model, while code generation and log interpretation can often be handled well by a balanced production model. Treating planning as "simple," forcing uniformity for its own sake, or over-indexing on input size rather than reasoning demand are weaker heuristics.

### Q7.
A retail company's product-description generator must produce thousands of SEO-friendly blurbs per hour from structured catalog data. Occasionally a human reviewer flags subtly wrong tone. What is the MOST cost-effective way to improve quality without major cost increase?

A. Switch the entire pipeline to Opus permanently
B. Keep a fast/cheap model for the bulk of generation and selectively escalate only flagged or high-value SKUs to a stronger model
C. Stop using Claude and rely on static templates
D. Increase the context window size, since more tokens improve output tone

**Answer:** B
**Explanation:** Selective escalation is a standard cost/quality trade-off pattern: use the cheaper model at volume and reserve the stronger model for edge cases or high-value items. Full migration to the strongest model is costly at this scale, abandoning Claude discards the value of the system, and context window size does not inherently fix tone issues.

### Q8.
A government agency's document-redaction agent must flag sensitive PII with very high recall, and errors carry legal consequences. Latency is a secondary concern (batch processing overnight). Which trade-off prioritization is MOST appropriate?

A. Optimize purely for latency since overnight batch jobs should finish quickly
B. Optimize primarily for accuracy/capability, accepting higher latency and cost given the batch context and legal stakes
C. Optimize purely for cost regardless of accuracy
D. Use the fastest model, since any model can be made "high recall" through prompting alone

**Answer:** B
**Explanation:** When latency is not a binding constraint (overnight batch) and the cost of errors is high (legal consequences), it is appropriate to weight model selection toward the strongest available reasoning/capability, typically Opus. Prioritizing cost or latency here undervalues the stakes, and prompting alone cannot fully substitute for underlying model capability on hard recall tasks.

### Q9.
A manufacturing company uses Claude for real-time anomaly explanation on a factory floor dashboard; operators need an explanation within roughly one second of an alert firing. Which factor should dominate the model choice?

A. Context window size, since factory logs can be long
B. Latency, since the use case has a hard near-real-time response requirement
C. Training data recency, since anomalies are novel
D. Price per million output tokens only, ignoring response time entirely

**Answer:** B
**Explanation:** A hard real-time constraint makes latency the dominant selection factor, pointing toward Haiku-class models even if some reasoning depth is traded off. Context window and training recency are secondary here, and ignoring latency entirely would violate the core requirement of the use case.

### Q10.
An architect is asked to justify, in an internal design review, why a customer-support summarization feature uses Sonnet rather than Opus or Haiku. Which justification best reflects sound model-selection reasoning?

A. "Sonnet is the newest model, so it is always correct by default"
B. "Sonnet offers a balance of reasoning quality, latency, and cost appropriate for a production workload that needs good but not maximal reasoning depth"
C. "Sonnet was chosen because switching models requires no further testing"
D. "Sonnet was chosen at random to avoid vendor bias accusations"

**Answer:** B
**Explanation:** Sonnet is positioned as the balanced choice for production workloads needing solid reasoning without the cost/latency of Opus or the capability ceiling of Haiku. "Newest = correct," skipping validation, and random selection are not defensible architectural justifications.

### Q11.
A financial services firm wants to add a "deep analysis" reasoning/effort setting to its Claude-powered investment memo generator, available only to senior analysts for complex cases. What is the MOST appropriate guidance for when to enable this higher-effort mode?

A. Enable it for all requests to maximize quality uniformly
B. Enable it selectively for genuinely complex, high-stakes requests where added latency and cost are justified by the value of deeper reasoning
C. Never enable it, since effort settings have no measurable effect
D. Enable it only for short prompts, since effort settings do not apply to long prompts

**Answer:** B
**Explanation:** Reasoning/effort settings trade latency and cost for deeper reasoning, so they should be applied selectively where the task complexity and stakes justify the cost. Always-on usage wastes resources on simple cases, claiming no effect is false, and effort settings are not restricted to short prompts.

### Q12.
A SaaS company migrating from an older Claude model to a new generation model notices that a previously reliable prompt now produces inconsistent JSON formatting in a minority of responses. What is the BEST next step?

A. Roll back permanently and never attempt the migration again
B. Re-validate and likely tighten the output-format instructions or add structured output constraints for the new model, since prompts are not guaranteed to transfer perfectly across model generations
C. Ignore the issue since minor formatting inconsistencies never matter downstream
D. Switch to Haiku instead, assuming smaller models format JSON more reliably by default

**Answer:** B
**Explanation:** Model migrations should include prompt re-validation; even strong models can respond differently to legacy prompt phrasing, and tightening format instructions or constraints is the standard remediation. Permanently abandoning the migration is overly conservative, ignoring formatting errors risks downstream parsing failures, and model size does not guarantee formatting reliability.

### Q13.
An architect must choose between Sonnet and Opus for a multi-agent research system's "orchestrator" agent, which delegates subtasks to specialist subagents but does not perform heavy reasoning itself. Which choice is MOST defensible?

A. Opus, because orchestrators must always use the strongest available model
B. Sonnet, because the orchestrator's role is coordination and delegation rather than deep independent reasoning, making a balanced model sufficient
C. Haiku, because orchestrators never reason at all
D. It is irrelevant which model orchestrates, since subagents do all the work

**Answer:** B
**Explanation:** Model choice should match the actual reasoning burden of the role; a coordination-focused orchestrator typically does not need Opus-level depth, making Sonnet a cost-effective fit. Assuming orchestrators always need the top model, assuming zero reasoning occurs, or assuming model choice is irrelevant all misjudge the orchestrator's actual workload.

### Q14.
A customer-facing agent currently uses Opus for all turns, including simple FAQ-style replies within a broader support conversation. Cost has become a concern. What is the BEST architectural remediation?

A. Replace Opus entirely with Haiku for the whole conversation
B. Introduce intent classification to route simple FAQ turns to Haiku/Sonnet while reserving Opus for turns requiring complex troubleshooting or judgment
C. Keep Opus for everything, since mixing models in one conversation is not technically possible
D. Cache the Opus system prompt and assume that alone solves the cost problem

**Answer:** B
**Explanation:** Dynamic, per-turn model routing based on classified complexity is a standard pattern to control cost while preserving quality where it matters most. Full replacement with Haiku risks quality loss on hard turns, mixing models across turns is technically feasible, and prompt caching addresses token cost but not the deeper issue of using an oversized model for simple turns.

### Q15.
During a vendor evaluation, a procurement team asks an architect to explain why "always use the most capable model" is not a sound default policy for an enterprise Claude deployment spanning dozens of use cases. Which answer BEST captures the architectural reasoning?

A. Because the most capable model is technically incapable of handling simple tasks
B. Because matching model capability to task complexity controls cost and latency without sacrificing the quality the task actually needs; over-provisioning capability is wasteful
C. Because enterprise contracts legally prohibit using advanced models for simple tasks
D. Because only one model can be used per organization at a time

**Answer:** B
**Explanation:** The core trade-off principle is proportionality: match model strength to task demands to avoid wasted cost and latency. The most capable model can handle simple tasks fine (just inefficiently), there is no such legal prohibition, and organizations are not limited to a single model.

### Q16.
A fintech company's agent uses Claude's effort parameter to control reasoning depth across different request types. An architect needs to explain the available effort levels and what happens if the parameter is left unset. Which statement is accurate?

A. Effort only has two levels, "on" and "off," and leaving it unset defaults to "off"
B. Effort ranges across levels such as low, medium, high, xhigh, and max; leaving the parameter unset is equivalent to using the default "high" level
C. Effort controls only the final answer's word count and has no relationship to reasoning depth
D. Effort must always be set explicitly on every request, since there is no documented default

**Answer:** B
**Explanation:** Claude's effort parameter spans multiple levels (low through max) trading response thoroughness against token efficiency, with "high" documented as the default, equivalent to omitting the parameter entirely. It is not a binary on/off switch, it governs reasoning depth rather than word count alone, and a documented default does exist.

### Q17.
An architect is designing cost controls for a multi-step agentic coding assistant that makes many sequential tool-use round trips per task. The team wants to cap total spend for the entire task, not just a single request, and also wants to understand how "thinking" tokens are billed. Which statement is correct?

A. Thinking tokens are free and unrelated to max_tokens, and setting max_tokens once at the start of the task automatically caps the whole multi-step loop
B. Thinking tokens are billed as output tokens (even when the thinking text itself is not returned) and count toward max_tokens; since max_tokens applies per request, capping spend for an entire multi-step loop requires a task-level budget mechanism rather than a single max_tokens value
C. Thinking tokens are billed separately as a flat per-task fee regardless of how much reasoning occurs
D. max_tokens automatically aggregates across every tool-use round trip in a task without any extra configuration

**Answer:** B
**Explanation:** Reasoning tokens are billed as output tokens and count against max_tokens, but max_tokens is scoped to a single request, so a ten-round-trip agentic loop has ten separate ceilings unless a task-level budget mechanism is used to bound the whole loop. Thinking is not free or a flat per-task fee, and max_tokens does not auto-aggregate across requests.

### Q18.
A team upgrades its customer-support agent from an older Claude model to a newer one. The system prompt contains forceful phrasing such as "CRITICAL: You MUST use the escalate_to_human tool whenever the customer expresses any frustration." After the upgrade, the tool fires far more often than intended, even for mild customer annoyance. What is the MOST likely explanation and fix?

A. The new model ignores system prompts, so the phrasing is irrelevant; add the same instruction to every user message instead
B. Newer model generations can respond more strongly to system prompt instructions than older ones; forceful, all-caps imperative phrasing calibrated to fix an older model's under-triggering can cause over-triggering after an upgrade, so the instruction should be dialed back to ordinary language and re-validated
C. The tool definition itself must be deleted and rewritten from scratch after every model upgrade
D. Over-triggering after a model upgrade is unrelated to prompt phrasing and can only be fixed by lowering the model's temperature

**Answer:** B
**Explanation:** Documented behavior shows some newer Claude generations respond more strongly to system prompt instructions, so prompt calibration—including forceful phrasing meant to fix under-triggering—does not transfer cleanly across model generations and can flip into over-triggering; dialing back to ordinary phrasing and re-validating is the correct remediation. System prompts are still respected, tool definitions don't need a full rewrite, and temperature is not the documented lever here.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
