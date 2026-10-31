# Domain 3: Integration

[← Back to index](../README.md)

## Exam objectives covered

1. Evaluate tool and agent configuration for capability bloat
2. Analyse authentication and authorisation
3. Evaluate accuracy-latency trade-offs
4. Analyse observability challenges
5. Design RAG pipelines
6. Apply retrieval strategies
7. Evaluate connection protocols
8. Evaluate progressive discovery versus monolithic context

---

### Q1.
A multinational bank is building an HR assistant that lets employees query payroll, benefits, and time-off balances across 12 regional HR systems. The architecture team proposes giving the agent 90 tools upfront (every operation across every system) and a single shared service-account credential for all backend calls. Which two concerns should the review flag as most urgent?

A. Only latency is a concern; credentials and tool count are secondary
B. Capability bloat from loading all 90 tools regardless of relevance, and an authorisation failure since a shared service credential cannot enforce that an employee only accesses their own records
C. Only the shared credential is a problem; 90 tools is a reasonable and safe design
D. Neither is a real concern as long as the vector database is well indexed

**Answer:** B
**Explanation:** This scenario combines two of the domain's core risks: tool/capability bloat (90 tools loaded regardless of task relevance, degrading selection accuracy and burning context) and an authorisation gap (a shared credential authenticates the app but cannot enforce per-employee data boundaries). Latency alone doesn't capture the access-control risk, dismissing the tool count ignores a real bloat problem, and vector database indexing is unrelated to either issue described.

### Q2.
A healthcare insurer's claims-processing agent retrieves clinical notes using semantic search over a flat vector index containing all patients across all regions, with no document-level permission filtering. What is the most severe architectural risk here?

A. Slightly suboptimal chunk sizing
B. Cross-patient and cross-region data exposure, since there is no metadata-based access filtering or document permission enforcement at the retrieval layer before results reach the model
C. Reduced reranking accuracy only
D. Excess token consumption during ingestion

**Answer:** B
**Explanation:** Without metadata filtering and document-level permission enforcement at retrieval time, any authenticated user's query could surface another patient's or region's clinical notes, which is a severe privacy and compliance failure, not a minor tuning issue. Chunk sizing, reranking accuracy, and ingestion token cost are real but much lower-severity concerns compared to an unenforced cross-tenant data exposure risk.

### Q3.
A SaaS company's support agent calls three independent diagnostic tools (check_subscription_status, check_payment_method, check_feature_flags) sequentially to answer "why can't I access this feature?", adding 1.8 seconds of avoidable latency. What should be changed?

A. Merge the three tools into one opaque tool with no parameters
B. Execute the three independent, non-dependent tool calls in parallel, since none of their inputs depend on another's output, then synthesize the combined result
C. Remove two of the three checks to save time, accepting incomplete diagnosis
D. Increase reasoning effort to compensate for the sequential latency

**Answer:** B
**Explanation:** Since the three checks are independent of each other's results, executing them in parallel directly reduces end-to-end latency without sacrificing the completeness of checking all three conditions, which is the standard parallel tool execution optimization. Merging into one opaque tool harms modularity and reuse, dropping checks reduces diagnostic accuracy, and higher reasoning effort does nothing to address sequential I/O-bound latency.

### Q4.
A government tax agency's citizen-facing chatbot shows healthy p50 latency and low average error rate on its dashboard, but citizens report the system frequently "times out" during a specific afternoon filing-deadline window. What should the observability strategy add?

A. Nothing; averages and p50 are sufficient indicators of system health
B. Time-segmented analysis and tail-latency (p95/p99) tracking, since aggregate averages can mask load-dependent degradation that only appears during specific high-traffic windows
C. Remove all latency metrics and rely only on citizen complaints
D. Switch entirely to tracking token consumption instead of latency

**Answer:** B
**Explanation:** Aggregate metrics like p50 and average error rate can hide tail-latency problems that only manifest under specific conditions (like a traffic spike during a filing deadline); segmenting by time window and tracking tail percentiles (p95/p99) is necessary to surface and diagnose this kind of load-dependent degradation. Relying solely on complaints is reactive and imprecise, and swapping to token-consumption tracking does not address a latency/timeout problem at all.

### Q5.
An architect designing a RAG pipeline for a legal firm's contract repository must choose a chunking strategy for lengthy, clause-structured contracts. Fixed 500-token chunks frequently split individual clauses mid-sentence, hurting retrieval precision. What is the best fix?

A. Use semantically aware chunking aligned to clause/section boundaries, with modest overlap to preserve continuity across chunk edges
B. Increase chunk size to the entire document length regardless of document size
C. Switch to one-word-per-chunk granularity
D. Disable chunking and store only document titles

**Answer:** A
**Explanation:** Semantically aware chunking that respects the document's natural structural boundaries (clauses, sections), combined with modest overlap, is the standard remediation for boundary-splitting problems that degrade retrieval precision. Whole-document chunks sacrifice retrieval granularity, word-level chunking destroys semantic coherence, and storing only titles discards the substantive content needed to answer contract-specific questions.

### Q6.
A retail company's product-support agent needs to answer both "find shoes under $80 in red" (a filterable, structured query) and "what shoe would feel best for a long training run" (a conceptual, descriptive query). Which retrieval design serves both needs?

A. Pure semantic search for both query types
B. Metadata/attribute filtering (price, color) for the structured query, combined with semantic search over descriptive content for the conceptual query, ideally within a unified hybrid pipeline
C. Pure keyword search for both query types
D. Full-context retrieval of the entire product catalog for every query

**Answer:** B
**Explanation:** Matching retrieval method to query structure is key: hard filterable attributes are best served by metadata filtering, while open-ended preference queries benefit from semantic search over descriptive text, and combining both in a hybrid pipeline serves the full range of customer queries. Semantic-only handles exact numeric thresholds poorly, keyword-only misses the conceptual query's nuance, and full-context retrieval of an entire catalog is infeasible and wasteful at scale.

### Q7.
An insurance company is deciding between MCP and direct API integration for a new claims-lookup tool that will initially be used by one internal claims-processing application, with no near-term plans for reuse by other teams. What is the most pragmatic recommendation?

A. Direct API integration is reasonable given the narrow, single-client scope; MCP can be adopted later if reuse needs emerge across multiple client applications
B. MCP must be used regardless of scope, since it is categorically superior in every situation
C. Agent-to-agent protocol is required since any tool call qualifies as agent-to-agent communication
D. CLI-based integration is mandatory for any claims-related data access

**Answer:** A
**Explanation:** Protocol choice should match actual integration topology and reuse requirements; a single-client, narrowly scoped integration does not need the added infrastructure and conceptual overhead of a general-purpose discovery protocol, and refactoring to MCP later remains a reasonable path if reuse needs materialize. Claiming MCP is categorically superior in every case ignores genuine trade-offs, labeling a simple tool call as A2A misapplies a term meant for autonomous agent-to-agent coordination, and CLI integration is not a requirement driven by the sensitivity of claims data (that's an authorisation/security design question, not a protocol mandate).

### Q8.
A manufacturing company's plant-operations agent has 80 tools loaded into every conversation, even though a typical session needs only 3-5. The architecture team wants to reduce context consumption without losing functionality. What should they implement?

A. Progressive tool discovery, where the agent first queries a lightweight tool catalog/search mechanism and loads only the relevant tool definitions for the current task
B. A larger context-window model to absorb all 80 tool definitions comfortably
C. Removal of 75 tools permanently regardless of whether they serve legitimate, if infrequent, use cases
D. Static system-prompt caching only, with no change to tool loading behavior

**Answer:** A
**Explanation:** Progressive discovery directly addresses this exact scenario — large catalog, narrow per-task need — by loading only the relevant subset of tools on demand rather than the entire catalog on every turn, cutting context consumption while preserving full functionality. A larger context window just absorbs the waste without eliminating it, permanently removing 75 tools risks discarding legitimately needed (if infrequent) capability, and prompt caching alone does not address the per-turn tool-definition loading problem.

### Q9.
A telecom provider's Claude agent orchestrates calls across a billing service, a network-diagnostics service, and a notification service. When a customer receives an incorrect bill explanation, engineers cannot determine which service contributed the faulty data. What should be implemented?

A. Distributed tracing with a correlation ID propagated across all services involved in handling the request, so engineers can reconstruct the full call path
B. A larger context window for the orchestrating model
C. Reranking of retrieved billing documents
D. Prompt caching of the system prompt

**Answer:** A
**Explanation:** Distributed tracing with a shared correlation ID is exactly the observability mechanism needed to reconstruct a multi-service request's path and pinpoint which component introduced an error. Context window size, reranking, and prompt caching are unrelated to the ability to trace and attribute behavior across multiple services in a single request.

### Q10.
A financial institution's Claude integration validates a JWT's signature and expiration but never checks the `aud` claim before accepting it to authorize a call to an internal trading API. What vulnerability does this create?

A. Slower token issuance times
B. Token replay/confusion risk, where a validly signed token issued for a different service could be accepted and misused against this API since the recipient (audience) was never verified
C. Increased latency in the retrieval pipeline
D. Reduced accuracy in reranking retrieved documents

**Answer:** B
**Explanation:** Audience validation ensures a token is only honored by the service(s) it was actually intended for; omitting this check allows a token legitimately issued for one service to be replayed against another that shares the same trusted issuer, a well-known class of token-confusion vulnerability. This is a security correctness issue unrelated to token issuance speed, retrieval latency, or reranking accuracy.

### Q11.
A logistics company's route-optimization agent is being evaluated: Config A uses a smaller model with deeper retrieval, Config B uses a larger model with shallower retrieval. What is the most rigorous way to choose between them for production deployment?

A. Choose based on which configuration the lead engineer personally prefers
B. Benchmark both configurations against a representative, labeled evaluation set measuring accuracy and latency/cost, then decide based on the organization's defined trade-off priorities for this specific use case
C. Always pick the larger model, since bigger models are categorically better in every scenario
D. Choose based solely on average token count per response, ignoring accuracy entirely

**Answer:** B
**Explanation:** Rigorous accuracy-latency trade-off evaluation requires representative benchmarking data and measurement across multiple relevant dimensions (accuracy and latency/cost), weighed against the specific business priorities of the use case, since no configuration wins on every axis universally. Personal preference lacks rigor, bigger models are not categorically superior for every latency budget or task, and token count alone ignores the accuracy dimension entirely.

### Q12.
A government benefits agency's eligibility-determination agent must ensure its generated answers are grounded strictly in retrieved policy text rather than the model's own training-data assumptions, which can be outdated. What combination of techniques best reduces this risk?

A. Increase the model's temperature to produce more varied, thorough-sounding answers
B. Require citation of retrieved sources in generated answers, combined with a post-generation verification step that checks claims against the actually retrieved context before the answer is returned
C. Remove retrieval entirely and rely purely on the model's parametric knowledge
D. Reduce the number of retrieved chunks so there is less material to misuse

**Answer:** B
**Explanation:** Combining explicit grounding/citation requirements with a verification step that checks generated claims against retrieved context is the standard way to reduce ungrounded additions, which is especially important for determinations based on policy that may have been updated after the model's training cutoff. Raising temperature increases variability and likely worsens grounding, removing retrieval eliminates the very mechanism meant to anchor answers in current policy, and reducing chunk count doesn't address the model's tendency to fill gaps with outdated assumptions.

### Q13.
A healthcare documentation agent logs full conversation transcripts, including patient names and diagnoses, in plaintext to a company-wide logging system accessible to all engineers. What principle is violated, and what is the recommended fix?

A. Tenant isolation is violated; the fix is to add more compute capacity
B. Privacy-aware logging is violated; sensitive fields should be redacted, masked, or access-restricted, with logging scoped to only what is needed for diagnosis and compliant retention
C. Prompt caching is violated; the fix is to disable caching entirely
D. Tool-selection accuracy is violated; the fix is to add more tools

**Answer:** B
**Explanation:** Privacy-aware logging requires minimizing, redacting, or restricting access to sensitive data captured for debugging/observability purposes; broad plaintext logging of identifiable health data to the entire engineering org is a serious compliance and privacy risk that needs scoped access and redaction, not just more infrastructure. This scenario has nothing to do with tenant isolation across customers, prompt caching mechanics, or tool-selection accuracy.

### Q14.
An e-commerce platform wants to retrieve both exact inventory counts ("how many units of SKU-4471 are in stock") and conceptual product recommendations ("what's a cozy sweater for cold weather") within the same assistant. Which retrieval design correctly handles both needs?

A. Route the exact-count query to a structured database lookup against the live inventory system, and route the conceptual query to semantic search over product descriptions, combining both approaches within the same assistant as appropriate per query
B. Use semantic search exclusively for both query types
C. Use a single structured SQL query to answer both, assuming the conceptual query can be reduced to a filter
D. Use full-context retrieval of the entire product catalog for every query regardless of type

**Answer:** A
**Explanation:** Matching retrieval strategy to data structure and query pattern is central here: exact, current numeric facts require a direct structured query against the system of record, while open-ended conceptual recommendations are well served by semantic search over descriptive content — and a well-designed assistant routes each query type appropriately. Semantic search alone risks imprecise or stale inventory counts, reducing a conceptual query to a structured filter loses its nuance, and full-context retrieval of the entire catalog for every query is both wasteful and imprecise.

### Q15.
A SaaS company's agent platform supports over 200 tools across many microservices, but any single customer conversation typically needs only 2-4 of them. The team debates whether loading all 200 tool schemas upfront is acceptable. What should guide the decision?

A. Always load all 200 schemas since context windows are effectively unlimited and this concern is overstated
B. Recognize that monolithic loading at this scale wastes context, increases latency/cost on every turn, and risks degraded tool-selection accuracy; progressive discovery (surfacing only the 2-4 relevant tools per task) is the appropriate mitigation given the large catalog and narrow per-task need
C. Require regulatory approval before ever using progressive discovery
D. Accept the current design permanently since no architectural alternative exists

**Answer:** B
**Explanation:** With a large catalog and narrow per-task tool needs, monolithic loading imposes real, avoidable costs in context, latency, cost, and selection accuracy, which progressive discovery directly mitigates by loading only what's relevant to the current task — this is the core trade-off this domain tests. Context windows, while large, are not unlimited and still carry real cost/latency implications; there is no regulatory requirement specific to progressive discovery; and viable architectural alternatives (namely progressive discovery) clearly exist.

### Q16.
A manufacturing conglomerate's maintenance agent is given OAuth tokens that are valid for 24 hours with refresh tokens that never expire or rotate. What change best aligns with secure token-handling practice?

A. Make the access tokens valid indefinitely to reduce refresh overhead for technicians
B. Shorten access token lifetimes appropriately for risk level and implement refresh token rotation with expiration, so a leaked refresh token has limited value over time
C. Eliminate refresh tokens and require technicians to log in again every 24 hours with no exceptions
D. Leave the configuration unchanged since 24-hour tokens are universally considered best practice

**Answer:** B
**Explanation:** Short-lived access tokens paired with rotating, expiring refresh tokens limit the damage window if credentials are compromised while still preserving usability, which is the standard secure token-handling pattern. Indefinite access tokens dramatically raise compromise risk, eliminating refresh tokens harms usability without proportional benefit, and a flat 24-hour rule ignores that appropriate lifetimes vary with the sensitivity of the operations involved.

### Q17.
A legal-tech company's RAG pipeline embeds isolated contract clauses without surrounding context, causing ambiguous clauses like "the rate increases by 2% after year one" to be embedded without knowing which contract or section they belong to. What technique addresses this?

A. Increase the embedding model's vector dimensionality
B. Apply contextual retrieval by prepending disambiguating context (document title, section heading, brief summary) to each chunk before embedding
C. Randomly reorder chunks before embedding
D. Delete all ambiguous chunks from the index

**Answer:** B
**Explanation:** Contextual retrieval — enriching each chunk with surrounding document context before embedding — directly resolves ambiguity that arises when a chunk's true meaning depends on context not captured within the chunk itself. Increasing embedding dimensionality doesn't address a missing-context problem, reordering chunks is irrelevant, and deleting ambiguous chunks discards potentially important contract content rather than fixing its retrievability.

### Q18.
A government agency's compliance team requires seven-year retention for all agent tool calls touching citizen records, but the current observability stack retains all logs (including verbose debug traces) for only 30 days, optimized for troubleshooting. What is the correct resolution?

A. Extend the 30-day debug log retention policy to seven years for everything, including verbose traces
B. Create a separate, immutable audit log store for compliance-relevant events (citizen-record access, consequential tool calls) meeting the retention requirement, distinct from short-lived operational debug logs
C. Tell compliance that observability data can never serve audit purposes
D. Maintain the seven-year record manually in a spreadsheet

**Answer:** B
**Explanation:** Compliance-grade audit trails typically require a dedicated, immutable, long-retention store for specific auditable events, kept separate from high-volume, short-retention debug logs meant for a different purpose. Extending full debug retention to seven years is costly and full of irrelevant noise, dismissing the compliance requirement is not a valid response, and manual spreadsheet tracking does not scale or provide adequate audit integrity.

### Q19.
An insurance company's architecture team is deciding how a Claude-based underwriting agent should coordinate with an external vendor's actuarial risk-modeling service, which is itself an independent reasoning system that may need to ask clarifying questions. What protocol characteristic matters most here?

A. Whether the connection supports only a single stateless request/response, since that is always sufficient
B. Whether the protocol supports richer, potentially multi-turn interaction appropriate for coordinating with another autonomous reasoning agent, a consideration central to agent-to-agent (A2A) style designs
C. Whether the vendor's service can be run entirely inside Claude's own infrastructure
D. Whether authentication can be skipped because the vendor is a trusted partner

**Answer:** B
**Explanation:** Coordinating with a remote autonomous reasoning system that may need back-and-forth clarification requires a protocol supporting richer, potentially stateful or multi-turn interaction, which is a central design consideration for A2A-style communication rather than a simple one-shot API call. Assuming one-shot request/response always suffices ignores the clarification need, it is not feasible to host a third-party vendor's service inside Claude's infrastructure, and trusted-partner status never substitutes for proper authentication.

### Q20.
A retail company's RAG system returns technically relevant but unhelpful chunks (e.g., warranty terms) when a customer asks "how do I reset this device?" because of shared vocabulary driving high similarity scores. What should be added to the pipeline?

A. A reranking step using a more precise relevance model (e.g., cross-encoder) to reorder initially retrieved candidates based on deeper query-intent relevance
B. Removal of the warranty document from the corpus entirely
C. An increase in the number of initial candidates with no further relevance refinement
D. A switch to exact keyword matching only, dropping semantic search

**Answer:** A
**Explanation:** Reranking with a more precise relevance model is designed exactly to address cases where initial embedding-based retrieval surfaces lexically similar but intent-mismatched results, re-scoring candidates against actual query intent to surface the truly helpful chunk. Removing the warranty document discards content useful for other legitimate queries, retrieving more unranked candidates doesn't fix ordering, and pure keyword matching loses the semantic understanding needed for paraphrased troubleshooting queries.

### Q21.
A hospital network's architecture review finds that an MCP server exposing clinical scheduling tools accepts any client connection on the internal network with no verification of client identity or scoped permissions, relying solely on network firewall rules. What is the core risk?

A. No risk, since MCP automatically handles authentication without any server-side implementation needed
B. Any client reachable on the network, including a compromised internal host, could invoke sensitive scheduling tools, since authentication and authorisation must be explicitly implemented at the MCP server layer rather than assumed to be provided by the protocol itself
C. This is acceptable permanently, since firewalls alone are sufficient for any clinical system
D. MCP servers cannot expose write-capable actions, so this concern is moot

**Answer:** B
**Explanation:** MCP defines a protocol for discovery and invocation, but authentication and fine-grained authorization must be explicitly designed and enforced by the server implementation; relying solely on network-level controls leaves the server exposed to any reachable client, including a compromised internal host. The protocol does not provide authentication "for free," network firewalls alone are not sufficient defense-in-depth for clinical scheduling data, and MCP servers are fully capable of exposing write/control actions, making proper authorization even more critical.

### Q22.
A telecom provider's network-diagnostics dashboard shows a healthy average error rate, but on-call engineers paged for a spike receive no indication of which specific tool or downstream dependency is failing. What improvement would most reduce mean-time-to-resolution?

A. Remove the alert entirely since it isn't actionable in its current form
B. Break down error-rate metrics and alerting by dimension (per tool, per downstream service, per error type) so on-call engineers can immediately identify the likely failing component
C. Raise the alert threshold so it pages less frequently
D. Replace real-time paging with a daily summary email

**Answer:** B
**Explanation:** Dimensional breakdown of error-rate metrics turns a vague "something is wrong" signal into an actionable one, directly reducing diagnosis time during an incident by pointing engineers toward the likely failing component. Removing the alert or delaying detection to a daily email would harm incident response, and simply raising the threshold risks missing real problems rather than making the existing signal more useful.

### Q23.
A fintech's remote MCP server wrapping a payments API is found during review to (1) forward any bearer token a client sends straight to the downstream payments API without checking who it was issued for, and (2) request every available payments scope ("read, initiate, approve, reverse transactions") at first connection so users are never interrupted later. Which combination of fixes addresses both findings?

A. Enable TLS on the connection, which resolves both the token-forwarding and scope-breadth concerns
B. Have the server validate that each token was actually issued for it before use (eliminating token passthrough, which enables confused-deputy and audience-circumvention risks), and replace the broad up-front scope grant with a minimal initial scope plus targeted, logged incremental elevation as specific actions are actually needed
C. Leave token handling as-is since downstream services will reject bad tokens anyway, but fix only the scope issue
D. Fix only the token-forwarding issue, since broad scope requests are a UX optimization with no security downside

**Answer:** B
**Explanation:** Token passthrough is a named, forbidden anti-pattern precisely because it skips audience validation and can turn the server into a confused-deputy or exfiltration vector, while requesting every scope up front maximizes blast radius and makes future revocation disruptive — the correct fix addresses both independently: audience-validate every token at the server, and replace broad up-front consent with minimal initial scope, targeted elevation, and logged elevation events. TLS only protects data in transit and validates neither token audience nor scope appropriateness, assuming downstream rejection is a sufficient safety net ignores that the server itself is the first and most important enforcement point, and dismissing scope breadth as a pure UX matter ignores its direct bearing on blast radius and revocation risk.

### Q24.
A platform team's agent has grown to over 400 internal tools across microservices, and the team is deciding how to let Claude find the right 2-4 tools for a given task without loading all 400 definitions on every turn. One engineer proposes a custom "tool search" layer and asks what mechanisms are documented for this kind of on-demand discovery against a large catalogue. Which answer best reflects the available approaches and how this problem relates to retrieval strategy more broadly?

A. There is only one correct mechanism — natural language queries — and anything else is unsupported
B. On-demand discovery against a large tool catalogue can be implemented the same way retrieval against a large document corpus is: via pattern/regular-expression matching, via natural-language queries scored against a lexical method like BM25, or via a custom embedding-based semantic search — selecting the right few items from a large set at request time is the same underlying problem whether the set is documents or tools
C. Tool discovery and document retrieval are unrelated problems that share no useful architectural parallel
D. The only valid approach is to always load all 400 tool definitions, since partial loading is not supported by any mechanism

**Answer:** B
**Explanation:** Selecting a small relevant subset from a large catalogue at request time is structurally the same problem whether the catalogue holds documents or tools, and documented approaches for tool search mirror retrieval strategy choices: regex/pattern matching (lexical/keyword-style), natural-language queries against a BM25-style ranker (hybrid lexical-semantic), or a custom embeddings-based semantic search — giving the architect the same keyword-vs-semantic trade-off space covered elsewhere in this domain. Claiming only one mechanism is valid ignores the documented variety, treating tool discovery and document retrieval as unrelated misses the direct architectural parallel, and insisting all 400 definitions must always load defeats the stated goal and ignores that progressive, on-demand loading is a supported and recommended pattern at this scale.

### Q25.
A healthcare company's observability dashboard shows healthy error rates and normal latency, yet a clinician discovers that the RAG assistant quietly answered a drug-interaction question using a superseded guideline version that still carried valid-looking citations, and a separate conversation received a flat refusal that never triggered any alert. What is the common root cause linking both incidents, and what should the team do?

A. Both are unrelated one-off bugs requiring no systemic change
B. Both incidents are failure modes that present as healthy to conventional monitoring — a grounded-looking answer built on stale, citation-bearing content, and a refusal arriving on a successful response stream rather than an error — so the team should expand its failure taxonomy to explicitly define and instrument for these "looks-like-success" cases: metadata-based filtering/exclusion of superseded guideline versions at retrieval time, and alerting wired to refusal events specifically, not just API error events
C. The fix for both is simply to lower the alert threshold on existing error-rate metrics
D. The fix for both is to disable retrieval entirely and rely on the model's own judgment

**Answer:** B
**Explanation:** Both failures belong to a class that reads as a success to standard monitoring — stale-but-plausible retrieved content with intact citations, and a refusal delivered on a normal response stream rather than as an error — so the underlying fix is the same: explicitly name these failure modes in the system's failure taxonomy and instrument for them directly, via metadata-based exclusion of superseded content at the retrieval layer and dedicated alerting on refusal events rather than error events alone. Treating them as isolated bugs misses the shared "invisible to existing monitoring" pattern, lowering an error-rate threshold does nothing since neither incident ever produced an error event, and abandoning retrieval entirely removes a working capability instead of fixing the specific gap in version filtering and event-channel coverage.
