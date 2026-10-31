# Objective 20: Define Evaluation Metrics

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Define evaluation metrics covering accuracy, task completion rate, latency, cost per request, token consumption, reliability, safety, security, and user satisfaction.

---

### Q1.
A regional bank's architect is standing up an evaluation suite for a Claude-based loan-document summarization service. Compliance wants assurance the system reliably extracts the correct APR from documents. Which metric most directly captures whether the model's answer matches the ground-truth APR?

A. Latency percentile (p95)
B. Accuracy against a labeled ground-truth dataset
C. Token consumption per request
D. User satisfaction score from a post-call survey

**Answer:** B
**Explanation:** Accuracy against labeled ground truth directly measures correctness of extracted values like APR. Latency and token consumption measure efficiency, not correctness, and satisfaction surveys are subjective proxies that don't verify factual correctness.

### Q2.
A healthcare SaaS company deploys a Claude agent that must both retrieve patient scheduling data via a tool call AND produce a correctly formatted appointment confirmation. Leadership asks for a single metric reflecting whether the *entire* multi-step workflow succeeded end-to-end, not just individual steps.

A. Token consumption
B. Task completion rate
C. Safety violation rate
D. Average latency per tool call

**Answer:** B
**Explanation:** Task completion rate measures whether the full workflow achieved its intended outcome end-to-end, which is what leadership is asking about. The other metrics each measure a narrower dimension (cost, safety, speed) rather than overall workflow success.

### Q3.
An insurance claims platform processes bursts of 10,000 claims during catastrophe events. The architecture team is concerned that under load, response times could degrade enough to violate SLA commitments with adjusters. Which metric should be tracked specifically to catch this risk?

A. Cost per request
B. p95/p99 latency under load
C. Token consumption per claim
D. Reliability (uptime) over a 30-day window

**Answer:** B
**Explanation:** Tail latency percentiles (p95/p99) measured under realistic burst load directly reveal SLA-threatening slowdowns that average latency can mask. Cost and token metrics don't capture responsiveness, and 30-day uptime is too coarse-grained to detect burst-driven degradation.

### Q4.
A telecom company's customer support agent is billed per Claude API call based on input and output tokens. Finance wants to understand the unit economics of the deployment to forecast budget as call volume scales 5x.

A. Reliability
B. Cost per request (including token consumption)
C. Safety violation rate
D. Task completion rate

**Answer:** B
**Explanation:** Cost per request, derived from token consumption and pricing, is the metric that enables accurate unit-economics forecasting as volume scales. The other metrics address quality, safety, or success rate but not financial forecasting.

### Q5.
A legal tech firm's contract-review assistant occasionally fabricates case citations that do not exist. Which category of metric is most appropriate for detecting and quantifying this specific failure mode?

A. Latency
B. Safety metric (harmful content rate)
C. Accuracy/factuality metric (hallucination rate)
D. Cost per request

**Answer:** C
**Explanation:** Fabricated citations are a factuality/hallucination problem, best tracked via an accuracy-oriented metric such as a hallucination or citation-verification rate. Safety metrics target harmful/toxic content, not factual correctness, and the remaining options are unrelated to truthfulness.

### Q6.
An e-commerce retailer's Claude-powered product-description generator must never leak internal supplier pricing data embedded in its context window into customer-facing output. Which metric category should the evaluation framework prioritize to catch this?

A. Task completion rate
B. Security/data-leakage metric
C. User satisfaction score
D. Token consumption

**Answer:** B
**Explanation:** Preventing exposure of sensitive internal data in model output is a security concern, so a dedicated data-leakage/security metric is required to detect and quantify this risk. Completion rate, satisfaction, and token usage do not test for information disclosure.

### Q7.
A manufacturing company's internal engineering copilot has high accuracy scores in offline evaluation, but engineers report in interviews that they find its answers "unhelpfully verbose and hard to act on." Which metric would best capture this complaint quantitatively over time?

A. Reliability (error rate)
B. User satisfaction (e.g., CSAT/NPS or thumbs-up rate)
C. Cost per request
D. Token consumption only

**Answer:** B
**Explanation:** Perceived helpfulness and usability are subjective qualities best captured through user satisfaction instruments like CSAT, NPS, or in-product feedback signals, which accuracy and cost metrics cannot surface. Token consumption only measures volume, not perceived quality.

### Q8.
A government agency's public-facing chatbot must be evaluated for its tendency to produce outputs that could be considered politically biased or offensive, independent of whether the facts stated are correct. Which metric category targets this concern?

A. Accuracy
B. Safety metric
C. Latency
D. Task completion rate

**Answer:** B
**Explanation:** Bias and offensiveness in generated content fall under safety evaluation, which assesses harm potential separately from factual correctness. Accuracy measures correctness of facts, not tone or social harm, and latency/completion rate are unrelated dimensions.

### Q9.
A logistics company runs a Claude agent that calls three downstream APIs per request (routing, inventory, carrier rates). Occasionally a downstream API times out, causing the agent to silently return a degraded answer. Which metric best captures the frequency of such operational failures across a fleet of production requests?

A. Reliability (error/failure rate including tool/API failures)
B. Token consumption
C. User satisfaction
D. Cost per request

**Answer:** A
**Explanation:** Reliability metrics track the rate of operational failures, including downstream dependency failures, which is exactly the issue described. Token consumption and cost are economic metrics, and satisfaction is a lagging, subjective signal unlikely to isolate this specific cause.

### Q10.
A financial-services firm wants to compare two Claude model configurations (one with extended reasoning/high effort, one standard) for a fraud-review assistant. Which pairing of metrics is most appropriate to make a balanced decision, rather than optimizing a single dimension?

A. Only token consumption
B. Only latency
C. Accuracy/task completion rate together with latency and cost per request
D. Only user satisfaction

**Answer:** C
**Explanation:** A sound architectural decision requires a multi-metric view that balances quality (accuracy/completion) against efficiency (latency) and economics (cost), since optimizing any single metric alone can hide unacceptable trade-offs elsewhere. The single-metric options each ignore critical trade-off dimensions.

### Q11.
A retail chain's inventory-forecasting agent has a 99.95% uptime over the quarter, yet the business reports that forecasts are frequently wrong. What does this scenario best illustrate about evaluation metric selection?

A. Reliability (uptime) alone is a sufficient proxy for output quality
B. Reliability and accuracy are independent dimensions and both must be tracked
C. Latency is the more important metric here
D. Cost per request should replace accuracy tracking

**Answer:** B
**Explanation:** The system is highly available (reliable) yet still produces incorrect outputs, demonstrating that reliability and accuracy measure different failure modes and neither substitutes for the other. The other answers incorrectly conflate or substitute unrelated metrics.

### Q12.
An architect designing metrics for a multi-turn customer-service agent at a telecom wants a metric specifically sensitive to whether the agent resolves the customer's issue within the conversation, as opposed to simply responding coherently turn-by-turn. Which metric fits best?

A. Per-turn latency
B. Conversation-level task completion / resolution rate
C. Per-turn token consumption
D. Model-level uptime

**Answer:** B
**Explanation:** A resolution-rate metric evaluated at the conversation level captures whether the overall customer issue was solved, which per-turn latency or token metrics cannot assess since they measure individual exchanges rather than end-to-end outcomes. Uptime is unrelated to conversational outcome quality.

### Q13.
A pharmaceutical company's regulatory-submission assistant must flag any output containing protected health information (PHI) it should not expose. Which pair of metric categories is most directly relevant to evaluating this risk?

A. Latency and cost per request
B. Security (data exposure) and safety (compliance/harm) metrics
C. Token consumption and reliability
D. User satisfaction and task completion rate

**Answer:** B
**Explanation:** PHI exposure is simultaneously a security concern (sensitive data leakage) and a safety/compliance concern (regulatory harm), making both categories directly relevant, while the other pairs measure performance, cost, or satisfaction dimensions unrelated to data protection risk.

### Q14.
During evaluation design for a cost-sensitive SaaS chatbot, an architect proposes tracking "cost per successful task" instead of "cost per request" as the primary cost efficiency metric. What is the main advantage of this choice?

A. It eliminates the need to track accuracy
B. It normalizes cost by actual useful outcomes, penalizing cheap-but-failing requests
C. It is easier to compute than cost per request
D. It removes the need for latency monitoring

**Answer:** B
**Explanation:** Cost per successful task divides spend by successful outcomes, so a model that is cheap per call but frequently fails looks worse than one that costs more but reliably succeeds — a more meaningful efficiency signal. It does not replace accuracy, latency tracking, or simplify computation.

### Q15.
A manufacturing firm's predictive-maintenance assistant evaluation shows excellent accuracy and low latency in staging, but the architect insists on also tracking token consumption trends before go-live. Why is this justified even when quality metrics already look strong?

A. Token consumption is a proxy for accuracy
B. Token consumption drives direct cost and can reveal inefficient prompting or context bloat that quality metrics won't show
C. Token consumption replaces the need for safety evaluation
D. Token consumption is required by Anthropic's API and has no architectural purpose

**Answer:** B
**Explanation:** Token consumption is an independent operational signal tied to cost and efficiency; a model can be accurate yet consume excessive tokens due to bloated prompts or context, which only token-level tracking will surface. It is not a proxy for accuracy nor a substitute for safety evaluation.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
