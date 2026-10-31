# Domain 4: Evaluation, Testing & Optimization

[← Back to index](../README.md)

## Exam objectives covered

1. Define evaluation metrics covering accuracy, task completion rate, latency, cost per request, token consumption, reliability, safety, security, and user satisfaction.
2. Design evaluation datasets and frameworks, including building representative datasets, using real-world examples, edge cases, and adversarial test cases, creating regression datasets, using code-based and model-based graders, incorporating human evaluation, evaluating multi-turn conversations, and calibrating model graders against human judgment.
3. Conduct A/B testing and iterative improvement, including establishing a baseline, comparing model configurations, prompts, retrieval strategies, and alternative architectures, running experiments on controlled traffic, measuring statistical and practical improvements, and rolling back unsuccessful changes.
4. Diagnose system issues including prompt failures, hallucinations, incorrect retrieval, model mismatch, tool execution failures, context overflow, incorrect structured outputs, agent loops, and evaluation failures, and distinguish root causes from symptoms.
5. Optimize token usage, latency, and cost-performance using prompt caching, context reduction, model routing, batch processing, parallel execution, retrieval optimization, output token limits, model and effort selection, and cost per successful task.
6. Monitor performance in production through production evaluation, logging and metrics, distributed tracing, quality monitoring, regression detection, alerting, performance drift detection, and continuous improvement.

---

### Q1.
A regional bank's fraud-review agent's accuracy drops from 94% to 78% two days after a deployment that bundled a model version upgrade, a prompt revision, and a retrieval index refresh. What is the architect's best first step to find the root cause?

A. Immediately roll back everything permanently and never investigate further
B. Revert each change independently (model, then prompt, then retrieval index) against the evaluation dataset to isolate which one caused the regression
C. Assume it's a hallucination issue and add a disclaimer to all outputs
D. Wait a few weeks to see if the metric recovers naturally

**Answer:** B
**Explanation:** When multiple changes ship simultaneously, isolating each variable against a fixed evaluation set is the only reliable way to pinpoint the true cause rather than guessing or waiting passively. Permanent rollback without investigation prevents learning the cause, and assuming a specific failure mode without evidence is unfounded.

### Q2.
A healthcare SaaS company is building its first evaluation dataset for a clinical-notes summarizer. The current dataset consists entirely of clean, well-formatted notes written by the engineering team. What should be added before considering the dataset production-ready?

A. More synthetic clean notes from the same team
B. Real de-identified production notes, edge cases (malformed/ambiguous notes), and adversarial cases probing PHI leakage
C. Nothing; clean synthetic data is the gold standard
D. Only latency benchmark cases

**Answer:** B
**Explanation:** A representative, production-ready evaluation dataset needs real-world examples, edge cases, and adversarial cases (especially for a domain with sensitive data like PHI) — synthetic clean data alone cannot surface the messier failure modes seen in production. Latency cases measure a different dimension entirely.

### Q3.
A telecom company wants to compare a new retrieval strategy against its current one for a billing-dispute assistant. What is the most statistically sound experimental design?

A. Deploy the new strategy to all users for a month, then compare to last month's numbers
B. Randomly split live traffic concurrently between old and new strategies and compare metrics statistically over the same time period
C. Have two engineers manually judge which strategy "feels" better
D. Test only in a staging environment with synthetic traffic, never in production

**Answer:** B
**Explanation:** Concurrent random traffic splitting controls for time-based confounds (seasonality, data drift) and enables valid statistical comparison, the core principle of sound A/B testing. Sequential before/after comparison introduces confounds, subjective judgment lacks rigor, and staging-only testing may not reflect real production traffic patterns.

### Q4.
A retail company's support chatbot begins producing JSON responses with missing required fields immediately following a model version upgrade, breaking the downstream order-processing integration. What is the most precise diagnosis?

A. Hallucination unrelated to the upgrade
B. Incorrect structured output likely caused by a model mismatch introduced by the upgrade
C. A context overflow issue unrelated to the model change
D. An agent loop

**Answer:** B
**Explanation:** Malformed JSON output appearing right after a model upgrade strongly indicates the new model needs updated formatting instructions or schema enforcement — a structured-output failure tied to model mismatch. The timing correlation rules out unrelated causes like overflow or looping, which have different symptoms.

### Q5.
A logistics company sends the same lengthy system prompt and tool schema on every single dispatch-routing API call, driving up cost unnecessarily. Which optimization most directly addresses this without affecting the model's capability?

A. Prompt caching of the static system prompt and tool definitions
B. Switching to a smaller model for all requests regardless of complexity
C. Reducing the number of available tools
D. Increasing the output token limit

**Answer:** A
**Explanation:** Prompt caching allows the static, repeated portions of the prompt to be reused at reduced cost across calls, directly cutting spend without reducing capability. Switching models or removing tools risks quality degradation, and raising output limits would increase cost rather than reduce it.

### Q6.
A government agency's citizen-services chatbot runs a one-time pre-launch evaluation but has no ongoing production monitoring. Months later, a slow decline in answer quality goes undetected until citizen complaints accumulate. What should have been implemented from the start?

A. A single annual evaluation cycle
B. Continuous production evaluation with regression detection and alerting to catch drift as it happens
C. No monitoring at all, since pre-launch evaluation is considered sufficient
D. Monitoring only cost metrics, since quality was already validated pre-launch

**Answer:** B
**Explanation:** Pre-launch evaluation cannot detect degradation that emerges after deployment due to drift in data or usage patterns; continuous production evaluation paired with regression detection and alerting is required to catch such issues promptly. Infrequent, one-time, or cost-only monitoring all leave quality drift undetected for too long.

### Q7.
An insurance company's architect wants to quantify whether its claims-triage agent reliably completes the full workflow (classify claim, retrieve policy data, generate recommendation) rather than just producing fluent individual responses. Which metric best fits this need?

A. Token consumption per request
B. Task completion rate across the full multi-step workflow
C. Average latency per step
D. Cost per API call

**Answer:** B
**Explanation:** Task completion rate specifically measures whether the entire end-to-end workflow achieves its intended outcome, which is exactly what's being asked, unlike token, latency, or per-call cost metrics that measure narrower efficiency dimensions rather than overall success.

### Q8.
A manufacturing company's architect deploys an LLM-based grader to score the helpfulness of its equipment-diagnostics assistant at scale. Before using its output to gate releases, what must be done?

A. Trust the grader immediately since LLMs are inherently reliable evaluators
B. Calibrate the grader's scores against a human-labeled sample to confirm alignment with actual human judgment
C. Replace it permanently with a simple keyword-matching grader
D. Use it only on adversarial test cases, never on normal traffic

**Answer:** B
**Explanation:** Model-based graders must be validated against human judgment on a representative sample before being trusted for high-stakes decisions like release gating, since LLM judges can have systematic biases. Blind trust, reverting to keyword matching, or restricting use to only adversarial cases all fail to establish the needed calibration.

### Q9.
A SaaS company's architect runs an A/B test comparing two prompts and finds a statistically significant 0.3 percentage-point improvement in accuracy, but rolling out the change requires substantial engineering effort and introduces migration risk. What should the architect weigh before deciding to roll out?

A. Statistical significance alone is sufficient justification regardless of magnitude or cost
B. Whether the improvement is practically meaningful relative to the rollout cost and risk
C. The p-value should be ignored entirely once any positive trend is observed
D. The decision should be based solely on which engineer proposed the change

**Answer:** B
**Explanation:** A statistically significant but very small improvement may not justify substantial engineering cost and migration risk, so practical significance must be weighed alongside statistical significance before committing to rollout. Relying purely on statistical significance, ignoring p-values, or basing the decision on who proposed it are not sound engineering judgments.

### Q10.
A pharmaceutical company's regulatory assistant occasionally calls the same document-lookup tool repeatedly with identical parameters without making progress, eventually timing out. What is this failure pattern, and what should the architect investigate?

A. Hallucination; investigate the grounding documents
B. Agent loop; investigate the control logic and how the agent interprets tool results to break the repetitive cycle
C. Context overflow; investigate the input document length
D. Model mismatch; investigate which model version is deployed

**Answer:** B
**Explanation:** Repeated identical tool calls without progress is the defining symptom of an agent loop, typically caused by flawed control logic or misinterpreted tool outputs, requiring investigation into that control flow. The other diagnoses (hallucination, overflow, model mismatch) have different, distinct symptom profiles that don't match repetitive non-progressing tool calls.

### Q11.
A legal firm's contract-review tool processes the full 300-page master services agreement in context for every question, even when most questions pertain to a single clause. Which combination of techniques best reduces cost and latency here?

A. Keep full-document inclusion but increase the output token limit
B. Apply context reduction via targeted retrieval so only relevant clauses/sections are included per query
C. Switch to batch processing for all real-time user-facing queries
D. Increase the model's reasoning effort to compensate for the large context

**Answer:** B
**Explanation:** Retrieval-based context reduction — including only the relevant clauses instead of the entire document — directly cuts both input token cost and processing latency while preserving answer quality. Increasing output limits or effort would raise cost further, and batch processing is inappropriate for real-time user-facing queries.

### Q12.
A retail company's architect wants a single north-star metric to judge whether a proposed cost-cutting change (cheaper model, more aggressive caching) is actually beneficial overall, not just cheaper in isolation. Which metric best serves this purpose?

A. Raw cost per API call only
B. Cost per successful task, which accounts for both spend and the rate of actual task success
C. Total number of tokens processed per day
D. Average response length

**Answer:** B
**Explanation:** Cost per successful task combines economic efficiency with outcome quality, preventing an optimization that lowers per-call cost while increasing failures/retries from appearing falsely beneficial. The other metrics measure only raw usage or cost without connecting it to whether tasks were actually completed successfully.

### Q13.
A telecom company's monitoring shows stable average latency for its virtual assistant, but customers in a specific region report frequent severe slowdowns. What monitoring gap does this reveal, and what should be added?

A. No gap exists; average latency is sufficient
B. A lack of percentile-based (p95/p99) and segmented/regional latency monitoring, which should be added to catch tail and localized degradation
C. The fix is to stop tracking latency altogether
D. The fix is to only track latency once per quarter

**Answer:** B
**Explanation:** Averages can mask both tail-latency spikes and region-specific degradation; adding percentile tracking plus segmentation by region directly addresses the described blind spot. Abandoning latency tracking or reducing its frequency would make the visibility gap worse, not better.

### Q14.
An insurance company's architect notices automated quality metrics for its claims-review assistant look stable, yet adjuster complaints about incorrect payout suggestions have tripled. What should the architect do to reconcile this discrepancy?

A. Trust the automated metrics exclusively since they haven't changed
B. Investigate whether the evaluation dataset has a coverage gap (e.g., for a new claim type) and incorporate broader signals like human review and complaint correlation
C. Disable the automated evaluation suite entirely
D. Assume the adjusters are mistaken and take no action

**Answer:** B
**Explanation:** A divergence between stable automated metrics and rising real-world complaints typically indicates an evaluation coverage gap (e.g., missing a new scenario type); the fix is to investigate and expand coverage while correlating with human review and complaint signals. Blind trust in the existing metrics, disabling evaluation, or dismissing the complaints all ignore the evidence of a real problem.

### Q15.
A manufacturing company's architect is choosing between two model configurations for a root-cause-analysis assistant: one with standard effort, one with extended thinking (3x cost, 3x latency, 6% accuracy gain). What is the most defensible architectural approach?

A. Always choose the extended-thinking configuration for every request regardless of stakes
B. Selectively route only high-stakes or ambiguous cases to the extended-thinking configuration, using standard effort for routine cases
C. Always reject the extended-thinking configuration since it costs more
D. Ignore cost and latency entirely in the decision

**Answer:** B
**Explanation:** A trade-off-aware routing strategy — using the costlier, higher-accuracy configuration only where the stakes justify it — captures the quality benefit where it matters while controlling overall cost and latency. Blanket adoption, blanket rejection, or ignoring cost/latency altogether all fail to make a balanced, context-sensitive decision.

### Q16.
A government agency deploys a new Claude model version for its benefits-eligibility chatbot. The architect wants to detect within hours, not weeks, if the new version behaves meaningfully worse than the prior version on live traffic. What technique best supports this?

A. Waiting for citizen complaints to accumulate before taking action
B. Shadow/canary evaluation comparing new-version outputs against the prior version's outputs or known-good baselines on a continuous sample of traffic
C. Running the evaluation dataset once before rollout and never again afterward
D. Disabling monitoring during the rollout window to reduce noise

**Answer:** B
**Explanation:** Shadow or canary evaluation — continuously comparing new-version behavior against a trusted baseline on live or replayed traffic — enables fast, hours-scale detection of regressions, far quicker than waiting on user complaints. Evaluating only pre-rollout or disabling monitoring during the critical rollout window removes the very visibility needed to catch problems early.

### Q17.
A financial-services firm's architect wants to test three candidate prompts simultaneously for a loan-document assistant rather than just two. What statistical consideration becomes more important with this multi-variant design?

A. No special consideration is needed beyond standard two-variant thresholds
B. The increased risk of false positives from multiple comparisons, requiring correction methods or an appropriate multi-armed test design
C. Multi-variant experiments cannot be run on live, controlled traffic
D. Only the fastest variant should be considered, ignoring other metrics

**Answer:** B
**Explanation:** Testing more than two variants simultaneously increases the chance of spurious "significant" findings purely by chance (the multiple-comparisons problem), requiring statistical correction or proper multi-armed experimental design. The other options either ignore this real statistical risk or substitute an unrelated single-metric heuristic for sound experimental design.

### Q18.
A SaaS company's architect is finalizing the overall evaluation and monitoring strategy for a newly launched Claude-based agent, aiming to balance thoroughness with long-term maintainability. Which strategy best reflects mature practice across the domain?

A. Logging alone, with no tracing, alerting, or ongoing evaluation
B. A combination of representative and adversarial evaluation datasets, calibrated graders, controlled A/B testing before rollout, and continuous production monitoring (tracing, regression detection, alerting) in an ongoing improvement cycle
C. A single manual spreadsheet updated by one engineer each quarter
D. Full reliance on the model provider to handle all evaluation and monitoring

**Answer:** B
**Explanation:** Mature evaluation and optimization practice integrates dataset design, calibrated grading, rigorous experimentation, and continuous production monitoring into one ongoing cycle, giving both pre-launch rigor and post-launch visibility. Logging alone, ad hoc manual tracking, or fully outsourcing responsibility to the provider all leave significant gaps across the domain's lifecycle.
