# Objective 17: Apply Retrieval Strategies

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Apply appropriate retrieval strategies in Claude-based systems, including semantic search, keyword search, hybrid search, structured database queries, metadata-based retrieval, full-context retrieval, and choosing retrieval methods based on data structure and query patterns.

---

### Q1.
A legal research platform needs to retrieve case law where users often search using exact statute citations (e.g., "17 U.S.C. § 512") that must match precisely, as well as conceptual queries like "liability limits for online platforms hosting user content." Which retrieval approach best serves both needs?

A. Pure semantic search only, since it handles all query types equally well
B. Hybrid search combining keyword/exact-match retrieval (for precise citations and defined terms) with semantic search (for conceptual, paraphrased queries), merging and scoring results from both
C. Pure keyword search only, since legal queries are always exact
D. Full-context retrieval, loading the entire case law corpus into every query

**Answer:** B
**Explanation:** Hybrid search is specifically designed for scenarios mixing precise, lexical matching needs (exact citations, defined terms) with conceptual/semantic needs (paraphrased legal concepts), combining both signal types for better overall recall and precision. Pure semantic search often underperforms on exact identifiers and codes, pure keyword search fails on conceptual paraphrased queries, and full-context retrieval of an entire case law corpus is infeasible at scale and extremely costly.

### Q2.
A manufacturing company's inventory agent needs to answer "how many units of part #A4521-B are in warehouse 3 right now?" This requires an exact, up-to-the-second numeric answer. Which retrieval strategy is appropriate?

A. Semantic search over a vector index of warehouse documentation
B. A structured database query (e.g., SQL) directly against the live inventory system, since the answer requires precise, current, structured data rather than semantically similar text
C. Full-context retrieval of the entire warehouse management manual
D. Keyword search over historical inventory reports from the past year

**Answer:** B
**Explanation:** Exact, current, structured numeric data (like live inventory counts) is best served by a direct structured query against the system of record, since vector/semantic search over documents cannot guarantee precision or freshness for this kind of fact. Semantic search, keyword search over historical reports, and full-context document retrieval are all mismatched to a query that needs an exact, real-time number from a transactional system.

### Q3.
A SaaS company's internal agent needs to answer "what did we tell this specific customer in their last three support tickets?" where the universe of relevant documents is naturally small and well-defined (just that customer's ticket history). What retrieval approach is most appropriate?

A. Semantic search across the entire multi-tenant support ticket corpus with no filtering
B. Metadata-based retrieval (filtering directly by customer ID) to fetch exactly the relevant ticket set, potentially followed by full-context inclusion of that small, bounded set of tickets since the relevant scope is naturally limited
C. A generic hybrid search across all customers' tickets ranked by relevance score
D. Full-context retrieval of the entire company-wide support knowledge base

**Answer:** B
**Explanation:** When the relevant document set is naturally and precisely bounded by a structured attribute (customer ID), metadata-based filtering is the most direct and accurate retrieval method, and because the resulting set is small, including it in full context (rather than further semantic retrieval) avoids losing any relevant detail. Searching the entire multi-tenant corpus semantically or via hybrid ranking risks cross-customer leakage and imprecision, and retrieving the entire company-wide knowledge base is unnecessary and wasteful for a query scoped to one customer's history.

### Q4.
An insurance claims agent needs to find all claims involving "water damage" across millions of records, where the term appears in varied phrasing: "water damage," "flooding incident," "pipe burst," "moisture intrusion." Pure keyword search for "water damage" misses many relevant claims. What should be used instead or in addition?

A. Expand the keyword list manually to include every possible exact synonym, and nothing else
B. Semantic search (or hybrid search combining semantic and keyword), since embeddings can capture conceptual similarity between differently worded descriptions of the same underlying concept
C. Reduce the corpus size so fewer claims need to be searched
D. Switch entirely to a structured SQL query assuming all claims have a standardized "damage_type" field already populated correctly

**Answer:** B
**Explanation:** Semantic search captures conceptual similarity across varied phrasing that keyword matching misses, making it well suited to concept-based queries like "water damage" that can be described many different ways in free text; combining with keyword search in a hybrid approach adds robustness for exact terms that may still matter. Manually exhaustive synonym lists are brittle and incomplete, reducing corpus size doesn't fix a matching-method problem, and assuming a clean structured field exists may not reflect reality, especially for free-text claim narratives.

### Q5.
A government agency's citizen-facing assistant must answer "What are the eligibility requirements for the home energy assistance program?" where the full policy document is only 800 tokens long. What is a reasonable retrieval approach given the document's size?

A. Chunk the document into ten small pieces and run a full embedding-based retrieval pipeline for added rigor
B. Given the small, bounded size of the relevant document, consider full-context retrieval (including the entire short document directly) rather than building unnecessary retrieval infrastructure for content that easily fits within context
C. Always require a vector database regardless of document size, since that is the only valid RAG pattern
D. Retrieve a single random paragraph from the document, since any text provides acceptable context

**Answer:** B
**Explanation:** When relevant content is small enough to fit comfortably in context, full-context inclusion is a legitimate and often simpler, more accurate strategy than over-engineering a chunking/embedding pipeline for a short, self-contained document. Unnecessarily chunking and embedding a document that small adds complexity without benefit, insisting a vector database is the only valid pattern misunderstands that retrieval strategy should match data structure and query needs, and retrieving a random paragraph is simply unsound and risks missing the actual relevant eligibility criteria.

### Q6.
A retail company's agent fields two distinct query types: (1) "find me red running shoes under $80" (filterable by structured product attributes), and (2) "what's a good shoe for someone who wants a cushioned feel for long-distance running?" (a conceptual preference query). What retrieval design best serves both?

A. Use only semantic search for both query types, since it can technically still process structured filter terms as text
B. Use metadata/attribute filtering (color, price, category) for structured queries like the first, and semantic search over product descriptions/reviews for conceptual queries like the second, potentially combined within a single hybrid pipeline that applies filters before or alongside semantic ranking
C. Use only structured SQL filtering for both query types, since the second query can be reduced to a price and color filter
D. Require the user to manually indicate which retrieval method to use for every query

**Answer:** B
**Explanation:** Matching retrieval strategy to query structure is the key skill being tested: hard, filterable attributes (color, price) are best handled by structured/metadata filtering, while open-ended, preference-based queries benefit from semantic search over descriptive text, and a well-designed hybrid pipeline can combine both (e.g., filter first, then semantically rank). Using semantic search alone handles structured constraints poorly (e.g., exact price thresholds), reducing the preference query to pure structured filtering loses its qualitative nuance, and requiring users to specify retrieval method burdens them with an implementation detail they shouldn't need to know.

### Q7.
A telecom provider's network operations agent needs to retrieve configuration documentation that is tagged with metadata for device model, firmware version, and region. A technician asks, "What's the recommended firmware update procedure for model X200 routers in the EU region?" What retrieval strategy should be prioritized?

A. Pure semantic search over all documentation with no use of the available metadata tags
B. Metadata-based retrieval filtering directly on device model and region tags first, narrowing the candidate set precisely, optionally combined with semantic search within that filtered subset to find the most relevant procedure
C. Full-context retrieval of the entire documentation library regardless of relevance
D. Keyword search for the literal word "firmware" across all documents

**Answer:** B
**Explanation:** When documents carry structured, reliable metadata that directly maps to the query's explicit constraints (model, region), filtering on that metadata first is the most precise and efficient retrieval step, which can then be refined with semantic search within the narrowed set for the best-matching procedure. Ignoring available metadata and relying purely on semantic search wastes a precise, available signal, full-context retrieval of the entire library is wasteful and imprecise, and keyword search on a generic term like "firmware" would return far too broad and unfiltered a result set.

### Q8.
A financial institution building a research assistant needs to answer questions that sometimes require combining a precise numeric fact from a structured database (e.g., current prime rate) with contextual explanation from unstructured policy documents (e.g., how the rate affects loan terms). What retrieval design handles this combined need?

A. Use only semantic search over documents, assuming prime rate information is also described somewhere in text
B. Use a strategy that routes the numeric/structured portion of the query to a structured database query, and the explanatory/conceptual portion to semantic or hybrid search over documents, then combines both results before generation
C. Use only a structured database query, assuming it can also explain loan term implications
D. Randomly choose one retrieval method per session and stick with it for all queries during that session

**Answer:** B
**Explanation:** Queries that blend precise structured facts with conceptual explanation often benefit from decomposing the query and routing each part to the retrieval method best suited to it — structured queries for exact current data, document retrieval for explanatory context — then combining results for generation. Assuming a single document mention will reliably capture a frequently changing numeric fact is risky, a structured database alone cannot provide nuanced prose explanation, and randomly fixing one method for an entire session ignores that different queries within the session may have different needs.

### Q9.
A healthcare system's clinical decision-support agent needs to retrieve the most current treatment guideline for a given condition, but older superseded versions of guidelines remain in the document store for historical/audit purposes. Semantic search alone sometimes surfaces an outdated version because it is textually very similar to the current one. What should be added?

A. Delete all old guideline versions immediately so only the current one can ever be retrieved
B. Combine semantic search with metadata filtering on fields like `status=active` or `effective_date`/`superseded_by`, ensuring outdated versions are excluded (or clearly down-ranked) regardless of their textual similarity to the query
C. Increase the number of retrieved results so both old and new versions are shown without distinction
D. Rely on the model to infer which version is current based on its training data cutoff

**Answer:** B
**Explanation:** Metadata filtering on explicit status/validity fields is the correct way to exclude or deprioritize superseded content that would otherwise score highly on pure textual/semantic similarity, which is a critical safety control in clinical settings. Deleting old versions outright removes required audit history, showing both versions without distinction risks the model or clinician using outdated guidance, and relying on the model's training-data knowledge is unreliable since it has no visibility into the organization's specific guideline update timeline.

### Q10.
A logistics company's customer service agent must answer, "Where is package 1Z999AA10123456784 right now?" Which retrieval approach is correct, and why?

A. Semantic search, because tracking numbers are conceptually similar to other alphanumeric strings in the corpus
B. A direct structured lookup/query (e.g., database key lookup or API call) using the tracking number as an exact key, since this is a precise identifier lookup rather than a conceptual or ambiguous information need
C. Full-context retrieval of all shipment records company-wide
D. Keyword search treating the tracking number as a set of independent search terms

**Answer:** B
**Explanation:** An exact identifier like a tracking number calls for a direct key-based lookup against the system of record, which guarantees precision and freshness that no similarity-based search method can reliably provide for this kind of query. Semantic search is unnecessary and risks false-positive matches on similar-looking strings, full-context retrieval of all shipments is wildly inefficient, and treating a precise identifier as decomposable keyword terms misunderstands the nature of the query.

### Q11.
An architect is deciding on a retrieval strategy for an HR assistant that must answer "What is our company's parental leave policy?" (stable, well-defined content in one authoritative document) versus "Has anyone on my team taken parental leave in the last year?" (a query over structured, permissioned personnel records). What is the key architectural insight?

A. Both questions should use the same retrieval method, since they are both "HR-related" queries
B. These are fundamentally different query types requiring different strategies: the policy question is well suited to document-based semantic/full-context retrieval, while the personnel question requires a structured, permission-checked database query, since it involves exact records, aggregation, and strict access control rather than document similarity
C. Both questions should be answered using only the model's general knowledge with no retrieval at all
D. Both questions should be resolved using a single shared vector index containing both policy text and personnel records with no distinction

**Answer:** B
**Explanation:** Choosing retrieval strategy based on data structure and query pattern (not surface-level topic similarity) is the core architectural skill here: one is a stable-document lookup well-suited to semantic/full-context retrieval, while the other is a structured, access-controlled query over personnel data requiring database-style retrieval with strict permission enforcement, not vector similarity. Treating both as the same just because they're "HR-related" ignores the fundamentally different data shapes and sensitivity levels, relying on general model knowledge would fail for company-specific and individual-level data, and mixing permissioned personnel records into a shared vector index with policy text risks serious access-control violations.

### Q12.
A manufacturing plant's maintenance agent frequently receives queries combining a specific equipment identifier with an open-ended diagnostic question, e.g., "Machine ID PX-7731 is making a grinding noise, what should I check?" What retrieval design handles both the identifier and the open-ended portion effectively?

A. Treat the entire query as a single semantic search string with no special handling of the equipment ID
B. First use the equipment ID to filter/retrieve machine-specific metadata and maintenance history (structured/metadata-based retrieval), then use semantic search over maintenance manuals and troubleshooting guides for the "grinding noise" symptom, combining both pieces of context for the model
C. Ignore the equipment ID entirely and only search generically for "grinding noise" across all equipment types
D. Require the technician to split their query into two completely separate requests submitted independently

**Answer:** B
**Explanation:** Decomposing a mixed query into its structured component (equipment ID → metadata-based retrieval of machine-specific records) and its open-ended component (symptom → semantic search over troubleshooting content) and combining both is the correct way to serve a query that blends precise and conceptual needs. Treating the whole query as one semantic string risks diluting the precise identifier's value, ignoring the equipment ID discards important machine-specific context, and forcing the technician to split their natural single query into two requests is poor user experience and unnecessary given proper query decomposition.

### Q13.
A multinational bank's compliance search tool must let analysts find "all suspicious activity reports mentioning wire transfers over $10,000 to high-risk jurisdictions filed in Q3." This blends exact numeric/date filters with free-text content matching. What retrieval approach fits best?

A. Pure semantic search over report text only, ignoring the explicit numeric and date constraints
B. Hybrid retrieval: apply structured/metadata filters for the exact constraints (amount threshold, jurisdiction tags, filing quarter), then apply keyword or semantic search within that filtered subset for free-text relevance (e.g., matching "wire transfers" phrasing and context)
C. Pure keyword search for the literal phrase "high-risk jurisdictions" with no numeric or date filtering
D. Full-context retrieval of every suspicious activity report ever filed, regardless of quarter

**Answer:** B
**Explanation:** This query has clearly structured, exact constraints (amount threshold, jurisdiction, quarter) best handled by metadata filtering, combined with a free-text/semantic component for matching report content — a textbook case for hybrid retrieval that filters first and searches within the narrowed set. Ignoring the exact constraints via pure semantic search would return imprecise results, pure keyword search on one phrase misses the structured filters and paraphrased mentions, and retrieving every report regardless of quarter is both wasteful and non-compliant with the actual query scope.

### Q14.
An e-commerce platform's search-assisted shopping agent is criticized because semantic search sometimes returns products that are conceptually similar but out of stock or discontinued, frustrating customers. What retrieval refinement addresses this without discarding the value of semantic matching?

A. Disable semantic search entirely and switch to pure keyword search
B. Combine semantic search for relevance with a metadata filter (e.g., `in_stock=true`, `status=active`) applied either before or after semantic ranking, ensuring only purchasable products are ultimately surfaced to the customer
C. Leave the behavior as-is, since showing all conceptually related products regardless of availability is considered best practice
D. Increase the number of semantic search results returned without adding any availability filtering

**Answer:** B
**Explanation:** Combining semantic relevance ranking with a hard metadata filter for availability (in stock, active status) ensures that only purchasable items are ultimately shown, preserving the value of conceptual matching while eliminating a clear usability problem. Abandoning semantic search loses its ability to handle natural, descriptive shopping queries, accepting the current behavior ignores a real and fixable customer-experience issue, and simply returning more unfiltered results doesn't address the root cause of showing unavailable products.

### Q15.
A government agency is deciding retrieval strategy for two distinct agent features: Feature A answers "summarize the entire content of this 3-page public notice" (the full document is always needed), and Feature B searches "find any public notices related to zoning changes in district 7 filed this year" across tens of thousands of notices. What is the correct retrieval strategy for each?

A. Use full-context retrieval for both features, since consistency across features is more important than matching the method to the actual task
B. Use full-context retrieval for Feature A, since the entire short document is always relevant and summarization requires complete coverage; use metadata filtering (district, year) combined with semantic or hybrid search for Feature B, since it needs to narrow a large corpus down to relevant matches rather than process everything
C. Use metadata filtering for both features, since both involve "public notices"
D. Use semantic search alone for Feature A and full-context retrieval for Feature B, reversing the appropriate approaches

**Answer:** B
**Explanation:** The correct strategy depends on data structure and query pattern: a short document that must be summarized in its entirety is well served by full-context inclusion, while searching a large corpus for documents matching specific structured and conceptual criteria needs filtering and ranking rather than loading everything. Forcing consistency across fundamentally different tasks, applying only metadata filtering to a full-document summarization task, or reversing the two approaches would each produce either incomplete summaries or an infeasible, unscalable retrieval process.

### Q16.
An architect is reviewing two scenarios. Scenario 1: an agent repeatedly answers different questions about one 40-page contract within a single work session, with the contract text itself never changing between questions. Scenario 2: an agent answers questions against a 50,000-document standards library, where each question typically needs a different small slice of content. The team proposes building a vector index for both. For Scenario 1, a compliance officer also notes the contract "must not leave the customer's security boundary" by being copied into another system. What is the correct architectural judgment?

A. Build a vector index for both scenarios, since indexing is always the superior approach regardless of how content is reused versus how it is searched
B. Scenario 1 is a caching shape — the same material repeats while only the question changes, so it belongs in a cached prompt prefix rather than a separate index — and the boundary constraint reinforces this, since an index would create a durable second copy of the contract outside the customer's boundary, which a cache does not; Scenario 2 is a genuine retrieval shape, since each question needs a different slice of a large, non-repeating corpus
C. Scenario 2 should use caching since the standards library is large, and Scenario 1 should use retrieval since the contract is long
D. The boundary constraint is a cost consideration only and should be weighed against retrieval performance rather than treated as a hard constraint

**Answer:** B
**Explanation:** The discriminating test is what stays identical between consecutive requests: in Scenario 1 the material is constant and only the question changes, which is a caching shape (and caching, unlike an index, creates no durable copy of the content living in another system — making it the only viable option once the content cannot leave the customer's boundary), while Scenario 2 has a different relevant slice needed per question across a large corpus, which is a genuine retrieval shape. Indexing is not universally superior — it is actively unsuitable for Scenario 1 given the boundary requirement; reversing the two assignments misreads which scenario has repeating content versus which has a large, non-repeating corpus; and a data-residency/boundary constraint is a governance requirement that must be resolved before performance trade-offs are even considered, not weighed against them as one factor among others.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
