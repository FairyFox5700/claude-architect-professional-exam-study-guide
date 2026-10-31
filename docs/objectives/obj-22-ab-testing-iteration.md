# Objective 22: Conduct A/B Testing and Iterative Improvement

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Conduct A/B testing and iterative improvement, including establishing a baseline, comparing model configurations, prompts, retrieval strategies, and alternative architectures, running experiments on controlled traffic, measuring statistical and practical improvements, and rolling back unsuccessful changes.

---

### Q1.
A retail company wants to test a new prompt for its product-recommendation agent. Before launching any experiment, what is the essential first step an architect must take?

A. Deploy the new prompt to 100% of traffic immediately
B. Establish a measured baseline of current performance on key metrics
C. Skip measurement and rely on team intuition about which prompt is better
D. Only test the new prompt in isolation without comparing it to anything

**Answer:** B
**Explanation:** Without a measured baseline, there is no reference point to determine whether the new prompt actually improves outcomes, making comparison meaningless. Full rollout, relying on intuition, or testing in isolation all skip the comparative measurement that A/B testing requires.

### Q2.
A financial-services firm is comparing two Claude model configurations — one using extended thinking/high effort and one using standard effort — for a loan-underwriting assistant. What is the most rigorous way to compare them?

A. Run each configuration sequentially in separate months and compare informally
B. Run both configurations concurrently on randomly split, controlled traffic and compare metrics statistically
C. Ask engineers to manually judge which felt better
D. Deploy the high-effort configuration to all traffic without comparison, since more effort is always better

**Answer:** B
**Explanation:** Concurrent testing on randomly split traffic controls for time-based confounders (seasonality, data drift) and enables statistically valid comparison, which is the core principle of rigorous A/B testing. Sequential testing introduces confounds, subjective judgment lacks rigor, and assuming higher effort is always better skips verification entirely.

### Q3.
A healthcare SaaS company runs an A/B test comparing two retrieval strategies for its clinical-reference assistant. The new strategy shows a 0.4 percentage-point improvement in accuracy with a large sample size, which is statistically significant (p < 0.05). The product owner wants to roll it out immediately. What should the architect consider first?

A. Statistical significance alone is sufficient to justify rollout regardless of magnitude
B. Whether the 0.4 point improvement is also practically meaningful given rollout costs and risks
C. Significance testing is irrelevant for medical applications
D. The sample size should be reduced to make the result easier to interpret

**Answer:** B
**Explanation:** A statistically significant but practically tiny improvement may not justify the engineering cost, risk, and disruption of a rollout, so practical significance must be weighed alongside statistical significance. Significance alone, ignoring significance, or shrinking sample size are all flawed responses.

### Q4.
A telecom provider tests a new system prompt for its billing-dispute agent on 10% of production traffic. After one week, the new prompt shows a higher resolution rate but also a higher rate of safety-flagged responses. What is the appropriate next action?

A. Roll out to 100% of traffic immediately since resolution rate improved
B. Weigh both metrics together, and if safety risk is unacceptable, iterate on the prompt or roll back before further rollout
C. Ignore the safety metric since resolution rate is the primary KPI
D. Permanently keep the test at 10% traffic without ever deciding

**Answer:** B
**Explanation:** A holistic trade-off evaluation is required when one metric improves while another regresses; an increase in safety-flagged responses is a red flag that must be addressed via iteration or rollback before wider exposure, regardless of resolution-rate gains. Ignoring safety or indefinitely stalling the decision are not responsible courses of action.

### Q5.
An e-commerce company launches a redesigned retrieval-augmented architecture for its support agent as a controlled experiment on 20% of traffic. After two days, latency has spiked and a subset of users are receiving malformed responses. What is the best immediate action?

A. Continue the experiment for the full planned duration regardless of the issue
B. Roll back the change immediately to mitigate user impact, then diagnose offline
C. Expand the experiment to 100% of traffic to gather more data faster
D. Switch metrics to only measure cost, ignoring the malformed responses

**Answer:** B
**Explanation:** When a controlled experiment shows active user harm (malformed responses, latency spikes), the responsible action is immediate rollback to limit blast radius, with root-cause diagnosis conducted afterward outside of live traffic. Continuing or expanding the experiment increases harm, and ignoring the issue by changing metrics is irresponsible.

### Q6.
A manufacturing firm wants to compare an agentic architecture (multiple tool calls and sub-agents) against a simpler single-prompt architecture for a maintenance-scheduling task. Which experimental design best isolates the effect of the architectural change itself?

A. Change the architecture and the underlying model simultaneously in one test
B. Hold the model and prompt constant where possible, varying only the architecture, then compare on identical traffic splits
C. Run the simpler architecture in production and the complex one only in a demo environment
D. Skip controlled testing and choose the architecture preferred by the engineering team

**Answer:** B
**Explanation:** Isolating a single variable (architecture) while holding others constant is the fundamental principle of valid experimental design, allowing the observed performance difference to be attributed to the architectural change itself. Changing multiple variables at once, comparing across different environments, or skipping testing all undermine causal attribution.

### Q7.
A logistics company's architect wants to compare three candidate prompts for a dispatch-routing assistant simultaneously. What is a key statistical consideration when running more than two variants at once?

A. No adjustment is needed; standard two-variant significance thresholds apply unchanged
B. The risk of false positives increases with multiple comparisons, so correction methods or appropriate multi-variant test design should be used
C. Multi-variant tests cannot be run on controlled traffic
D. Only the variant with the fastest latency should be considered regardless of other metrics

**Answer:** B
**Explanation:** Testing multiple variants simultaneously increases the chance of spurious "significant" results by chance (the multiple-comparisons problem), so architects should apply appropriate statistical corrections or multi-armed test designs. The other options either ignore this risk or substitute an unrelated single-metric heuristic.

### Q8.
An insurance company rolled out a new Claude model version for its claims-triage agent after a successful two-week A/B test. Three weeks post-rollout, accuracy on a new, previously rare claim type has quietly degraded. What should have been included in the original test design to catch this earlier?

A. A longer baseline measurement period only
B. Monitoring and evaluation segments for emerging or underrepresented input categories, not just aggregate metrics
C. A higher traffic allocation percentage during the test
D. Disabling the regression dataset during the test

**Answer:** B
**Explanation:** Aggregate metrics can mask degradation in specific underrepresented segments; segment-level monitoring (including for rare/emerging categories) is needed to catch localized regressions that overall averages hide. Longer baselines, higher traffic allocation, or disabling regression testing do not address the segment-level blind spot.

### Q9.
A government agency is piloting a new prompt template for its citizen-inquiry chatbot. The architect proposes measuring success using only "average user session length" as the key metric. What is the main risk of this metric choice?

A. Session length is always the best proxy for quality in every context
B. Longer sessions could indicate either higher engagement or user confusion/repeated failed attempts, making it an ambiguous success signal
C. Session length is impossible to measure in production
D. Session length is a safety metric, not a performance metric

**Answer:** B
**Explanation:** Metrics like session length are ambiguous because they can increase due to either genuine engagement or user frustration from repeated failures, so they should be combined with resolution/completion metrics rather than used alone. The other options misstate the nature or measurability of the metric.

### Q10.
A SaaS company's architect runs an A/B test comparing two prompt caching strategies to reduce cost. Variant B shows a 30% cost reduction but a measurable increase in stale/outdated context being used in responses. What is the correct interpretation?

A. Deploy Variant B immediately since cost reduction is the only metric that matters
B. The cost savings must be weighed against the correctness risk introduced by stale context; iterate on cache invalidation before rollout
C. Ignore the staleness issue since caching only affects performance, not correctness
D. Cost and correctness are unrelated and cannot be evaluated together

**Answer:** B
**Explanation:** Prompt caching decisions must balance cost savings against potential correctness trade-offs like serving stale context; the right response is to refine cache invalidation logic before a full rollout, not to ignore the regression. Treating cost as the sole criterion or claiming no relationship between the two both lead to a flawed decision.

### Q11.
A legal firm's architect wants to validate that a new structured-output prompt format genuinely improves downstream parsing success, not just that it looks better to reviewers. What experimental practice best supports this validation?

A. Rely solely on reviewer impressions of the new format
B. Measure objective downstream parsing success rate on controlled traffic comparing old vs. new format
C. Change the output format and the parsing code at the same time
D. Deploy to all traffic and assume success without measurement

**Answer:** B
**Explanation:** An objective, automatically measurable success criterion (parsing success rate) compared across controlled variants provides concrete evidence of improvement, superior to subjective impressions. Changing the format and parser simultaneously confounds the experiment, and deploying without measurement provides no evidence at all.

### Q12.
A retail company's experiment shows that a new model routing strategy (routing simple queries to a smaller/cheaper model) reduces cost by 25% with no statistically significant change in accuracy. What should the architect recommend?

A. Reject the change because any architectural complexity is undesirable
B. Adopt the routing strategy, since it achieves meaningful cost savings without sacrificing measured quality
C. Require another six months of testing before any decision, regardless of evidence
D. Adopt the change only if latency also decreases, otherwise reject regardless of cost

**Answer:** B
**Explanation:** A meaningful cost reduction with no measurable quality regression is a clear net positive and a textbook case for adoption following proper experimentation. Rejecting it on principle, demanding indefinite delay, or imposing an unrelated latency requirement are not justified by the evidence presented.

### Q13.
A pharmaceutical company's architect is debating whether to roll back a recently deployed prompt change after receiving two user complaints, despite the A/B test showing a statistically significant overall improvement. What is the most defensible approach?

A. Roll back immediately based solely on two anecdotal complaints, discarding the statistical evidence
B. Investigate whether the complaints represent a systematic segment-level issue not captured by aggregate test metrics, then decide based on that analysis
C. Ignore the complaints entirely since the test showed significance
D. Permanently disable all future A/B testing for this feature

**Answer:** B
**Explanation:** Anecdotal complaints should prompt targeted investigation into whether they reflect a real, possibly segment-specific regression masked by aggregate results, rather than either dismissing the data or reflexively rolling back on small anecdotal signals. Overreacting or ignoring the signal entirely are both poor responses; abandoning testing altogether is an extreme overcorrection.

### Q14.
A manufacturing company compares two prompt variants for an equipment-diagnostics assistant. Variant A has higher average accuracy; Variant B has lower average accuracy but far more consistent (lower variance) performance across different equipment types. In a high-stakes, safety-sensitive deployment, what additional consideration matters most?

A. Only average accuracy should ever be considered, variance is irrelevant
B. Consistency (lower variance across segments) may be critical in safety-sensitive contexts even if average accuracy is slightly lower
C. Variance cannot be measured in production experiments
D. The variant with more tokens consumed should always be preferred

**Answer:** B
**Explanation:** In safety-sensitive domains, consistent, predictable performance across all conditions can be more valuable than a higher average that masks poor performance on certain equipment types, so variance/consistency should be weighed alongside average accuracy. Ignoring variance or using token consumption as a selection criterion misses the actual risk trade-off.

### Q15.
An architect at an insurance company wants to test a new conversational prompt against the existing one but is worried that running the experiment during a known seasonal claims surge (e.g., storm season) could bias results. What is the best mitigation?

A. Run the test anyway and apply no adjustment, since seasonality doesn't affect language model behavior
B. Either time the experiment outside the surge period or ensure both variants are exposed concurrently to the same seasonal conditions
C. Cancel all future testing until next year
D. Use only historical data from a different company's deployment instead

**Answer:** B
**Explanation:** Concurrent exposure of both variants to the same conditions (including seasonal effects) neutralizes the confound, or alternatively the test can be scheduled outside the anomalous period; both preserve valid comparison. Ignoring seasonality, cancelling testing indefinitely, or substituting unrelated external data all fail to produce a valid controlled comparison.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
