# Objective 25: Monitor Performance

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Monitor performance in production through production evaluation, logging and metrics, distributed tracing, quality monitoring, regression detection, alerting, performance drift detection, and continuous improvement.

---

### Q1.
A bank deploys a Claude-based loan-advisory agent and runs evaluation only once, before launch, with no ongoing measurement in production. Six months later, accuracy has silently degraded due to upstream data changes. What architectural gap does this illustrate?

A. The pre-launch evaluation was unnecessary
B. The lack of continuous production evaluation to detect drift after launch
C. The model should never be evaluated more than once
D. This indicates a tool execution failure, not a monitoring gap

**Answer:** B
**Explanation:** Pre-launch evaluation alone cannot catch degradation that emerges after deployment due to data or environment drift; continuous production evaluation is needed to detect such issues over time. The pre-launch evaluation was valuable but insufficient alone, and this scenario is specifically about missing ongoing monitoring, not a one-off tool failure.

### Q2.
A healthcare SaaS company's Claude agent calls multiple internal microservices and an external lab-results API as part of answering clinical questions. When a response is slow, the team currently has no way to tell which specific step in the pipeline caused the delay. What capability should be added?

A. Prompt caching
B. Distributed tracing across the full request pipeline
C. A/B testing framework
D. Regression dataset expansion

**Answer:** B
**Explanation:** Distributed tracing instruments each step of a multi-service pipeline with timing and correlation data, allowing engineers to pinpoint exactly which component (microservice, API call, model inference) contributed to latency. Caching, A/B testing, and regression datasets address different concerns (cost, comparison, correctness) rather than pipeline-level latency visibility.

### Q3.
A retail company's support chatbot's quality score (measured via a model-based grader sampling live traffic) drops from 0.91 to 0.82 over two weeks, but no alert was triggered because no threshold was configured. What should the architect implement?

A. Remove the quality score tracking since it clearly doesn't work
B. Configure alerting thresholds on key quality metrics so that significant drops trigger automatic notification
C. Only check the quality score manually once per quarter
D. Replace quality monitoring with cost monitoring entirely

**Answer:** B
**Explanation:** Automated alerting on meaningful metric thresholds ensures that significant quality regressions are surfaced promptly rather than relying on someone to notice them manually, which is the actual gap in this scenario. Removing tracking or reverting to infrequent manual checks would make the problem worse, and substituting cost monitoring doesn't address quality degradation.

### Q4.
A logistics company's route-planning agent experiences a gradual, slow decline in recommendation quality over several months as real-world traffic patterns shift away from those represented in its original evaluation dataset. What is this phenomenon called, and what practice addresses it?

A. Agent looping; addressed by prompt engineering
B. Performance/data drift; addressed by periodically refreshing evaluation datasets and monitoring for drift
C. Context overflow; addressed by reducing prompt length
D. Tool execution failure; addressed by retrying failed API calls

**Answer:** B
**Explanation:** A slow, systemic decline as the real-world distribution diverges from what the system was evaluated/trained against is a classic case of performance drift, addressed by refreshing evaluation data and actively monitoring for drift signals over time. The other options describe unrelated failure modes with different causes and fixes.

### Q5.
A telecom provider's architect wants production logs for its customer-service agent to be useful for root-cause analysis after an incident, not just for counting request volume. What should the logging strategy include?

A. Only aggregate counts of total requests per day
B. Structured logs capturing inputs, outputs, tool calls, intermediate reasoning steps, and relevant metadata (e.g., model version, prompt version) per request
C. No logging at all, relying solely on user complaints to detect issues
D. Logs limited strictly to HTTP status codes

**Answer:** B
**Explanation:** Rich, structured per-request logging — including inputs/outputs, tool calls, and version metadata — is what enables effective post-incident root-cause analysis, unlike coarse aggregate counts or minimal status-code-only logs. Relying solely on user complaints provides no systematic visibility at all.

### Q6.
A government agency's chatbot deployment includes a nightly job that re-runs a fixed evaluation dataset against the production system and compares results to the previous day's baseline. What capability does this provide?

A. Real-time user authentication
B. Automated regression detection between deployments or over time
C. Cost per request optimization
D. Prompt caching

**Answer:** B
**Explanation:** Repeatedly running a fixed evaluation set and comparing results over time is the core mechanism for automated regression detection, catching unintended quality degradation introduced by any change (code, model, data). This has no connection to authentication, cost optimization, or caching.

### Q7.
A manufacturing company's architect notices that automated evaluation metrics look stable, but production support tickets related to the equipment-diagnostics assistant have tripled. What additional monitoring practice would most likely explain this discrepancy?

A. Relying exclusively on the existing automated metrics, since they show no change
B. Incorporating broader quality monitoring signals (e.g., support ticket correlation, user feedback, sampled human review) alongside automated metrics to catch gaps the automated suite misses
C. Reducing the frequency of automated evaluation runs
D. Switching entirely to cost-based monitoring instead of quality monitoring

**Answer:** B
**Explanation:** When automated metrics and real-world outcomes diverge, it signals a blind spot in the automated evaluation; correlating other signals like support tickets and incorporating human review helps uncover what the automated suite is missing. Trusting only the existing metrics, running them less often, or switching to cost monitoring would not resolve this visibility gap.

### Q8.
An insurance company's monitoring dashboard shows average latency within SLA, but the architect wants to also catch cases where a small percentage of requests experience severe slowdowns that could frustrate specific customers. What should be added to the monitoring setup?

A. Nothing; average latency is a sufficient indicator
B. Percentile-based latency monitoring (e.g., p95, p99) in addition to average, with alerting on tail degradation
C. Remove average latency tracking in favor of total request count
D. Only track latency once per month in a summary report

**Answer:** B
**Explanation:** Averages can mask tail-latency problems affecting a subset of users; tracking and alerting on percentiles like p95/p99 specifically surfaces these outlier slowdowns that averages hide. Relying solely on averages, removing latency tracking, or reducing monitoring frequency to monthly would all fail to catch this issue in a timely way.

### Q9.
A SaaS company's architect wants to ensure that after any new deployment, the team is systematically prompted to review quality metrics, cost metrics, and any new error patterns, rather than relying on ad hoc attention. What organizational/technical practice supports this?

A. A one-time evaluation before the very first launch only
B. A continuous improvement process with regular post-deployment review cadences tied to monitoring dashboards and alerts
C. Disabling all alerts to reduce noise
D. Delegating all monitoring responsibility to end users via complaint channels

**Answer:** B
**Explanation:** Establishing a continuous improvement process — a regular, structured cadence of reviewing dashboards, metrics, and alerts after each deployment — institutionalizes monitoring rather than leaving it to chance or memory. A one-time pre-launch check, disabling alerts, or relying on user complaints all abdicate the active monitoring responsibility.

### Q10.
A legal firm's contract-review assistant uses a model-based grader sampling 5% of production traffic daily to estimate ongoing quality. The architect wants to validate this production-evaluation approach periodically. What should be done?

A. Never revisit the grader once it's deployed
B. Periodically recalibrate the model-based grader's scores against a human-reviewed sample to ensure its judgments remain aligned with actual quality
C. Increase the sampling rate to 100% permanently to avoid the need for calibration
D. Discontinue production evaluation since pre-launch evaluation is sufficient

**Answer:** B
**Explanation:** Model-based graders used in production monitoring can drift or exhibit systematic bias over time, so periodic recalibration against human judgment ensures the ongoing monitoring signal remains trustworthy. Never revisiting it, sampling 100% without addressing calibration, or abandoning production evaluation entirely all leave the validity question unresolved.

### Q11.
A retail company's architect sets up monitoring that tracks model accuracy but nothing about cost or latency. During a high-traffic sales event, the system remains "accurate" by this dashboard, but costs spike dramatically and customers experience significant delays, discovered only afterward via the finance team's monthly invoice. What does this scenario demonstrate?

A. Monitoring a single dimension (accuracy) is sufficient for production health
B. Production monitoring should cover multiple dimensions (quality, cost, latency, reliability) holistically, not just one metric in isolation
C. Finance teams should own all technical monitoring going forward
D. Cost spikes are always acceptable during high-traffic events and require no monitoring

**Answer:** B
**Explanation:** Comprehensive production monitoring must track multiple dimensions simultaneously — quality, cost, latency, and reliability — because strength in one dimension can mask serious problems in another, as shown by the cost/latency blind spot here. Single-metric monitoring, outsourcing all monitoring to finance, or assuming cost spikes are always fine are all flawed responses.

### Q12.
A government agency's architect wants to detect, within hours rather than weeks, if a newly deployed Claude model version begins producing systematically different (and potentially worse) outputs than the previous version for the same inputs. What monitoring technique best supports this?

A. Waiting for citizen complaints to accumulate over several weeks
B. Shadow/canary evaluation comparing new-version outputs against the previous version's outputs or known-good baselines on a continuous sample of live or replayed traffic
C. Running the evaluation dataset once before launch and never again
D. Disabling monitoring during the rollout window to avoid noisy signals

**Answer:** B
**Explanation:** Shadow or canary evaluation — continuously comparing the new version's behavior against a trusted baseline on live or replayed traffic — enables fast (hours-scale) detection of systematic regressions, far quicker than waiting for complaints. Pre-launch-only evaluation or disabling monitoring during rollout both remove the very visibility needed to catch issues early.

### Q13.
A pharmaceutical company's monitoring system flags that the proportion of "I don't know" or refusal responses from its regulatory-assistant has increased from 2% to 15% over a month, with no deployment changes. What should the architect investigate as a likely explanation?

A. This metric is irrelevant and should be ignored
B. A possible shift in the input distribution (e.g., new query types, upstream data changes) or an issue with retrieval/context supply that increasingly prevents the model from finding sufficient grounding
C. This always indicates a prompt injection attack and nothing else
D. This is purely a latency issue requiring infrastructure scaling

**Answer:** B
**Explanation:** A rising refusal/"I don't know" rate without a deployment change typically points to a shift in what's being asked or a degradation in the retrieval/context pipeline feeding the model sufficient grounding; this is a quality/drift signal worth investigating thoroughly. Dismissing it, assuming a single specific attack cause, or misattributing it to infrastructure scaling all skip proper investigation.

### Q14.
A manufacturing company wants its monitoring system to not only detect a quality regression but also help the team understand whether it is isolated to a specific equipment type, region, or customer segment. What monitoring capability enables this kind of analysis?

A. Only tracking a single aggregate metric across all traffic
B. Segmented/dimensional monitoring that breaks down metrics by relevant categories (e.g., equipment type, region, customer tier)
C. Removing all logging to reduce storage costs
D. Running evaluation only once per year across the entire dataset

**Answer:** B
**Explanation:** Breaking down metrics along meaningful dimensions (equipment type, region, segment) allows the team to localize where a regression is occurring rather than seeing only an undifferentiated aggregate trend. Tracking only an aggregate metric, removing logging, or evaluating annually would all obscure this kind of granular insight.

### Q15.
A SaaS company's architect is designing the overall production monitoring strategy for a newly launched Claude-based agent and wants to balance thoroughness with practical maintainability. Which combination best reflects mature monitoring practice?

A. Logging and metrics only, with no alerting or tracing
B. A combination of structured logging, distributed tracing, sampled production evaluation, regression detection against a baseline, and threshold-based alerting, reviewed in a continuous improvement cadence
C. A single manual spreadsheet updated monthly by one engineer
D. Relying entirely on the model provider to handle all monitoring responsibilities

**Answer:** B
**Explanation:** Mature production monitoring combines multiple complementary capabilities — logging, tracing, ongoing evaluation, regression detection, and alerting — tied into a regular improvement process, giving both depth and actionability. Logging without alerting/tracing, manual ad hoc tracking, or outsourcing monitoring entirely to the provider all leave significant gaps in visibility and responsiveness.

### Q16.
A telecom provider's operations dashboard shows normal request rate, normal error rate, stable p95/p99 latency, and 99.98% uptime throughout a period during which customer complaints about wrong answers from its billing assistant have surged. Why do the standard operational dashboards fail to show any problem?

A. The dashboards are misconfigured and should be replaced entirely
B. Operational counters (throughput, error rate, latency, uptime) measure whether the system is running, not whether its answers are correct; detecting a quality regression requires content-level signals such as sampled response review, grader scores, or complaint correlation
C. Uptime and error rate are the most reliable proxies for answer correctness and should be trusted here
D. This pattern only happens when the monitoring system itself has crashed

**Answer:** B
**Explanation:** Standard operational/observability metrics describe the health of the serving pipeline (is it up, is it fast, is it erroring) and are structurally incapable of detecting that the content of successful, fast, non-erroring responses is wrong; catching a quality regression requires monitoring that actually inspects output content, such as sampled model-/human-graded review or correlation with complaint volume. The dashboards are not inherently misconfigured or crashed — they are simply answering a different question than "are the answers correct."

### Q17.
A government agency reruns the exact same fixed 500-example evaluation set against its citizen-services chatbot every week, and the score has stayed flat at 93% for six months. Meanwhile, real user satisfaction has been quietly declining as the agency rolled out new services and citizen query patterns shifted. What does this scenario reveal about the evaluation set itself?

A. A flat score over time always means the system is healthy and no further action is needed
B. A frozen, never-refreshed evaluation set can no longer detect regressions caused by a shift in the real input distribution, since it keeps measuring performance only on the same unchanging slice of traffic; the set should be periodically refreshed and its distribution compared against current production traffic
C. The evaluation set should be deleted since it is clearly broken
D. This proves the model-based grader is miscalibrated and must be replaced with a code-based grader

**Answer:** B
**Explanation:** A fixed evaluation set that is never refreshed will keep producing the same score indefinitely because it only ever tests the same unchanging slice of inputs, even as the live traffic distribution shifts due to new features or changing user behavior — the flat score reflects the dataset's staleness, not system health. The fix is to periodically refresh the set and compare its category distribution to current production traffic, not to delete the dataset outright or assume the grader (rather than the dataset's staleness) is the problem.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
