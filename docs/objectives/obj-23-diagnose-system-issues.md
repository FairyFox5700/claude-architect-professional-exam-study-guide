# Objective 23: Diagnose System Issues

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Diagnose system issues including prompt failures, hallucinations, incorrect retrieval, model mismatch, tool execution failures, context overflow, incorrect structured outputs, agent loops, and evaluation failures, and distinguish root causes from symptoms.

---

### Q1.
A bank's loan-advisory agent's accuracy drops from 94% to 78% immediately after a routine deployment that changed both the system prompt and the underlying model version in the same release. What is the architect's best first diagnostic step?

A. Assume it's a hallucination problem and add more grounding instructions
B. Roll back changes incrementally (model, then prompt) to isolate which change caused the regression
C. Immediately retrain the model from scratch
D. Ignore the drop since aggregate accuracy will likely recover on its own

**Answer:** B
**Explanation:** When multiple changes ship together, isolating variables by reverting them one at a time is the only reliable way to identify the true root cause rather than guessing. Assuming a specific cause without evidence, retraining unnecessarily, or ignoring a significant regression are all unjustified leaps.

### Q2.
A legal-research assistant confidently cites a case name and docket number that do not exist in any legal database. What is this failure mode called, and what diagnostic step confirms it?

A. Context overflow; confirmed by checking token counts
B. Hallucination; confirmed by verifying the cited facts against an authoritative source
C. Tool execution failure; confirmed by checking API error logs
D. Agent loop; confirmed by checking for repeated identical tool calls

**Answer:** B
**Explanation:** Fabricating plausible-sounding but nonexistent facts is a hallucination, verified by cross-checking the specific claim against ground-truth sources. The other diagnostic methods target unrelated failure modes (token limits, API errors, repetitive loops).

### Q3.
A retail company's RAG-based product-support assistant answers a question about a specific product's return policy with information that is accurate but belongs to a *different, similar* product. What is the most likely root cause?

A. Model mismatch
B. Incorrect retrieval (wrong or insufficiently specific document retrieved)
C. Context overflow
D. Agent loop

**Answer:** B
**Explanation:** The model correctly reasoned over what it was given, but what it was given was the wrong document — a retrieval precision/specificity problem, not a model or context-length issue. Model mismatch refers to using an inappropriate model version, overflow refers to context exceeding limits, and agent loops involve repetitive unproductive actions.

### Q4.
A telecom customer-service agent is observed calling the same "check account status" tool repeatedly with identical parameters, never progressing to resolve the customer's issue, until it times out. What is this failure pattern called?

A. Hallucination
B. Context overflow
C. Agent loop
D. Incorrect structured output

**Answer:** C
**Explanation:** Repeatedly invoking the same action without making progress toward task completion is the defining symptom of an agent loop, often caused by flawed control logic or misinterpreted tool results. The other options describe fabricated facts, exceeding context limits, or malformed output format, none of which match this repetitive-action pattern.

### Q5.
A manufacturing company's maintenance-scheduling agent begins producing JSON outputs that are missing required fields and occasionally contain trailing commas that break the downstream parser, starting right after a model version upgrade. What is the most likely category of issue?

A. Context overflow
B. Incorrect structured output, potentially due to model mismatch after the upgrade
C. Evaluation failure
D. Tool execution failure

**Answer:** B
**Explanation:** Malformed JSON output (missing fields, syntax errors) is an incorrect-structured-output failure, and its correlation with a model upgrade strongly suggests a model mismatch — the new model may need updated output-formatting instructions or schema enforcement. Context overflow and tool execution failures describe different symptoms, and evaluation failure refers to flaws in the test harness itself, not the production output.

### Q6.
An insurance claims agent's evaluation dashboard shows no regression in automated metrics, yet claims adjusters report a sharp rise in incorrect payout recommendations. Investigation reveals the evaluation dataset was never updated to include a new claim type introduced three months ago. What does this best illustrate?

A. A model mismatch
B. An evaluation failure (the evaluation framework itself has a blind spot)
C. A tool execution failure
D. An agent loop

**Answer:** B
**Explanation:** When the monitoring/evaluation system itself fails to detect a real problem because its test coverage is stale or incomplete, that is an evaluation failure — the measurement system, not the underlying model, is the broken component. The other options describe model- or execution-level failures, not failures of the evaluation apparatus.

### Q7.
A SaaS company's document-analysis assistant begins truncating its reasoning and giving incomplete answers only on very long input documents (>80 pages), while performing normally on shorter documents. What is the most likely root cause?

A. Hallucination
B. Context overflow (exceeding the effective context window or attention degradation at length)
C. Tool execution failure
D. Incorrect structured output

**Answer:** B
**Explanation:** Degraded performance correlated specifically with longer inputs is the classic signature of context overflow or long-context attention degradation, distinct from fabrication, tool errors, or formatting issues which would not correlate with document length in this way.

### Q8.
A logistics company's route-planning agent calls an external mapping API, which returns an HTTP 500 error, but the agent proceeds to present a fabricated route to the user without indicating any problem. What are the two distinct issues present, and which is the root cause versus the symptom?

A. The root cause is hallucination; the tool failure is a minor symptom
B. The root cause is the unhandled tool execution failure; the fabricated route is a downstream symptom (hallucination triggered by missing data)
C. Both issues are unrelated and should be fixed independently without prioritization
D. The root cause is context overflow; the tool failure is irrelevant

**Answer:** B
**Explanation:** The true root cause is that the system did not handle the tool's failure gracefully; the model's fabrication of a route is a downstream symptom caused by the agent proceeding with missing/invalid data. Treating the hallucination as the root cause misses the actual defect in error handling, and claiming the issues are unrelated ignores their causal link.

### Q9.
A government benefits-eligibility chatbot gives inconsistent answers to the same question asked in slightly different phrasings on different days, even though no code, model, or prompt changes were deployed. What should the architect investigate first?

A. Assume this is expected and acceptable model variance requiring no action
B. Check for non-deterministic factors (e.g., temperature settings, retrieval index changes, or underlying data source updates) that could explain the inconsistency
C. Immediately conclude it is a context overflow issue
D. Immediately conclude it is an agent loop

**Answer:** B
**Explanation:** Unexplained inconsistency without a deployment change warrants investigating non-deterministic or environmental factors such as sampling temperature, updated retrieval indices, or changed source data, before settling on a specific diagnosis. Dismissing it as acceptable, or jumping to an unrelated diagnosis without evidence, skips proper root-cause investigation.

### Q10.
A pharmaceutical company's regulatory-assistant architecture uses a smaller, faster Claude model for an internal tool-selection step but routes final answer drafting to a larger model. After a change, the tool-selection step begins choosing inappropriate tools for the task at hand, while the drafting model's output quality is unaffected when given correct tool results. What is the most precise diagnosis?

A. Model mismatch in the tool-selection step (the smaller model may be insufficiently capable or misconfigured for its assigned task)
B. Hallucination in the drafting model
C. Context overflow in the drafting model
D. Evaluation failure in the test harness

**Answer:** A
**Explanation:** The symptom is isolated specifically to the tool-selection step performed by the smaller model, pointing to a model-task mismatch — that model may be undersized or misconfigured for the selection task's complexity — while the drafting model performs correctly given good inputs. The other diagnoses misattribute the problem to the wrong component.

### Q11.
A financial-services chatbot's architect observes that accuracy degraded only for queries submitted via the mobile app, not the web app, after a shared backend prompt update. What does this pattern suggest about root cause versus symptom?

A. The prompt update itself is unlikely to be the root cause since both clients share it; investigate client-specific request formatting or context assembly differences
B. The prompt update is definitely the root cause and must be rolled back immediately without further investigation
C. Mobile users are simply less skilled at phrasing queries
D. This is unrelated to any system issue and requires no investigation

**Answer:** A
**Explanation:** Since the prompt is shared across both clients but only one client shows regression, the root cause more likely lies in something client-specific — such as how each client formats requests or assembles context — not the shared prompt itself. Blaming the prompt outright ignores the differential symptom, and blaming user skill or ignoring the issue are unsupported non-diagnoses.

### Q12.
A retail company's agent occasionally produces an output that passes all automated code-based graders but is flagged by human reviewers as subtly misleading. What does this reveal about the evaluation framework, and how should the architect respond?

A. The code-based graders are sufficient and the human reviewers are mistaken
B. The code-based graders have a coverage gap for subtle correctness issues; the architect should add model-based or human-reviewed test cases targeting this failure mode
C. This indicates a context overflow problem
D. This indicates a tool execution failure

**Answer:** B
**Explanation:** A gap between automated grader results and human judgment reveals that the current graders (likely structural/pattern-based) don't capture subtle semantic correctness issues, so the evaluation framework should be augmented with model-based or human review targeting that specific failure mode. Dismissing the human reviewers, or misattributing the issue to overflow or tool failure, does not address the actual evaluation gap.

### Q13.
A manufacturing company's agent, when given a very long list of sensor readings to summarize, begins ignoring instructions provided early in the prompt (like the required output format) while still correctly processing the sensor data itself. What is the most likely explanation?

A. Tool execution failure
B. Context-window attention effects, where instructions early in a very long prompt receive less effective attention ("lost in the middle")
C. Hallucination
D. Model mismatch

**Answer:** B
**Explanation:** This is a recognized long-context phenomenon where instructions placed early in a very long prompt can be under-attended relative to more recent content — a context-length-related attention issue rather than fabrication, tool failure, or using the wrong model entirely. Restructuring the prompt (e.g., repeating instructions near the end) is a common mitigation.

### Q14.
A telecom agent's structured output occasionally includes a valid JSON object, but with a phone number field containing an obviously hallucinated value not present anywhere in the source data. What combination of issues does this represent?

A. Purely a structured-output formatting issue; the JSON is valid so there's no other problem
B. A hallucination occurring within an otherwise well-formed structured output — formatting correctness does not guarantee content correctness
C. A tool execution failure masquerading as valid JSON
D. An agent loop

**Answer:** B
**Explanation:** This scenario shows that structural validity (well-formed JSON) and content correctness (accurate values) are independent concerns — the output can be syntactically perfect while still containing hallucinated content, so both must be evaluated separately. The other options mischaracterize the nature of the failure.

### Q15.
A government agency's chatbot evaluation suite reports 96% pass rate, but a newly identified category of adversarial prompts (not previously in the dataset) causes a 40% failure rate when manually tested. What root cause should the architect identify, and what is the appropriate corrective action?

A. The model is fundamentally broken and must be replaced entirely
B. The evaluation dataset has a coverage gap for this adversarial category; it should be added to the dataset and used to drive targeted prompt/architecture improvements
C. The 96% pass rate is sufficient and no further action is needed
D. This is purely a latency issue requiring infrastructure scaling

**Answer:** B
**Explanation:** A high aggregate pass rate alongside a newly discovered high-failure category reveals an evaluation coverage gap rather than a wholesale model failure; the correct response is to incorporate the new adversarial category into the dataset and use it to guide targeted fixes. Declaring the model broken, ignoring the finding, or misdiagnosing it as an infrastructure issue all miss the actual root cause.

### Q16.
A bank's loan-advisory agent begins behaving noticeably differently overnight even though the architecture team confirms the pinned model identifier in their API calls has not changed and no prompt or code deployment occurred. What should the architect investigate as the most likely explanation?

A. The pinned model ID must have silently changed its underlying weights on its own
B. A change in surrounding serving infrastructure (e.g., request routing, safety classifiers, or sampling/decoding logic) rather than the model itself, since the model ID is pinned and did not change
C. This can only be a user-reported illusion with no real underlying cause
D. The evaluation dataset must be corrupted

**Answer:** B
**Explanation:** A pinned model identifier should represent a fixed snapshot, so unexpected behavior change without any application-level deployment points to something in the surrounding serving stack (routing layer, safety filters, decoding parameters) rather than a silent swap of the model weights themselves. Assuming the pinned model silently changed, dismissing the report as illusory, or jumping to blame the evaluation dataset all skip the more likely infrastructure-level explanation.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
