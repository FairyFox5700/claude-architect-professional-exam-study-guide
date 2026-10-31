# Objective 16: Design RAG Pipelines

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design retrieval-augmented generation (RAG) pipelines for Claude-based systems, including document ingestion, chunking strategies, chunk size and overlap, contextual retrieval, embeddings, vector indexing, metadata filtering, document permissions, retrieval quality, and reranking.

---

### Q1.
A legal services firm is ingesting thousands of multi-hundred-page contracts into a RAG pipeline. Initial testing shows that fixed 2,000-token chunks frequently split key clauses across chunk boundaries, degrading retrieval relevance. What is the best remediation?

A. Increase chunk size to 10,000 tokens so no clause can ever be split
B. Use smaller, semantically aware chunking (e.g., splitting on clause/section boundaries) combined with modest overlap between adjacent chunks to preserve context across boundaries
C. Switch to word-level chunking with one word per chunk
D. Disable chunking and embed entire contracts as single vectors

**Answer:** B
**Explanation:** Semantically aware chunking aligned to natural document structure (clauses, sections) with overlap is the standard fix for boundary-splitting problems, preserving coherent units of meaning for embedding and retrieval. Extremely large chunks reduce retrieval precision and increase cost, word-level chunking destroys semantic coherence entirely, and embedding whole documents as single vectors loses the granularity needed for precise retrieval.

### Q2.
A healthcare RAG system ingests clinical guideline PDFs that contain tables, headers, and footnotes. Chunking logic treats the document as a flat stream of text, causing table data to be split mid-row and headers to be interspersed incorrectly. What ingestion improvement addresses this?

A. Skip all documents containing tables
B. Use structure-aware document parsing during ingestion (detecting tables, headers, and sections) so chunking respects the document's actual layout rather than treating it as undifferentiated text
C. Convert all PDFs to images and rely on the model's visual understanding exclusively for every query
D. Manually retype every document into plain paragraphs before ingestion

**Answer:** B
**Explanation:** Structure-aware parsing (recognizing tables, headers, sections) during ingestion ensures chunking boundaries respect the document's real layout, preventing broken tables and misplaced headers, which is a foundational RAG pipeline design concern. Skipping table-containing documents loses valuable clinical data, relying solely on image-based understanding for every query is inefficient and unnecessary when structured parsing is available, and manual retyping does not scale.

### Q3.
An architect is choosing a chunk size and overlap strategy for a SaaS product's internal knowledge base. Chunks of 150 tokens are highly precise for retrieval but frequently lack enough surrounding context for the model to generate a complete answer. What adjustment best addresses this without abandoning fine-grained retrieval?

A. Switch to 150-token chunks with zero overlap to save storage
B. Retrieve the small, precise chunk as the primary match, but include its surrounding context (e.g., neighboring chunks or a parent section) when assembling the prompt, preserving both retrieval precision and generation completeness
C. Increase chunk size to 8,000 tokens so no context is ever missing
D. Remove the retrieval step and give the model the entire knowledge base at once

**Answer:** B
**Explanation:** A common pattern (often called "small-to-big" retrieval) keeps embeddings/retrieval granular and precise while expanding the context sent to the model with surrounding content at generation time, getting the benefits of both precision and completeness. Zero overlap with small chunks worsens the context gap, large chunks sacrifice retrieval precision, and removing retrieval entirely is not scalable for large knowledge bases.

### Q4.
A financial services firm's RAG pipeline embeds each chunk independently, without any surrounding document context, causing ambiguous chunks (e.g., "the rate increases by 2% after the first year") to be embedded without knowing which product or policy they belong to. What technique directly addresses this ambiguity?

A. Increase the embedding model's dimensionality
B. Apply contextual retrieval by prepending chunk-specific context (e.g., document title, section heading, brief summary) to each chunk before embedding, so the resulting vector captures disambiguating context
C. Randomly shuffle chunk order before embedding
D. Remove ambiguous chunks from the index entirely

**Answer:** B
**Explanation:** Contextual retrieval — enriching each chunk with surrounding document context (titles, headings, summaries) before embedding — directly resolves the ambiguity problem where an isolated chunk's meaning depends on context not present in the chunk itself. Increasing embedding dimensionality does not resolve a missing-context problem, shuffling order is irrelevant, and removing ambiguous chunks discards potentially important content rather than fixing the retrieval of it.

### Q5.
An insurance company must ensure that a RAG-powered claims assistant only retrieves policy documents the requesting agent is authorized to view, based on region and product line. Where should this enforcement primarily occur?

A. Only in the system prompt, instructing the model to "only use documents relevant to the user's region"
B. At the retrieval layer itself, via metadata filtering (region, product line, document permissions) applied to the vector search query before any results are returned to the model
C. Only after the model generates its final answer, by checking the output for policy numbers
D. Nowhere, since all policy documents are considered public within the company

**Answer:** B
**Explanation:** Enforcing access control via metadata filtering at the retrieval layer (before results ever reach the model) is the architecturally sound approach, since it guarantees unauthorized documents are never exposed to the model or user in the first place. Relying on prompt instructions alone is unreliable and bypassable, post-hoc output checking is reactive and risks the model having already used restricted content, and treating all policy documents as universally accessible ignores legitimate regional/product-line access boundaries.

### Q6.
A manufacturing company's RAG system uses a vector index with a single flat embedding space for millions of technical manuals, resulting in degraded retrieval latency and relevance as the corpus has grown. What architectural improvement should be prioritized?

A. Continue growing the flat index indefinitely since vector databases scale linearly with no trade-offs
B. Adopt appropriate vector indexing structures (e.g., approximate nearest neighbor indexes such as HNSW or IVF) and/or partition the index by logical boundaries (e.g., product line, manual category) to improve both query latency and relevance at scale
C. Switch from embeddings to storing raw text with no vector index at all
D. Reduce the embedding dimensionality to zero to simplify storage

**Answer:** B
**Explanation:** At large scale, approximate nearest neighbor indexing structures and logical partitioning (sharding by category or metadata) are standard techniques to maintain query performance and relevance as a corpus grows, since naive flat/exhaustive search degrades in both latency and precision over large collections. Assuming indefinite linear scaling without trade-offs is false, removing vector search entirely abandons semantic retrieval capability, and zero-dimensional embeddings are nonsensical.

### Q7.
A retail company's RAG pipeline for product support is returning technically relevant but unhelpful chunks — e.g., retrieving a product's full warranty terms when the user asked "how do I reset this device?" Initial similarity search returns these as top matches due to shared vocabulary. What should be added to the pipeline?

A. A reranking step using a cross-encoder or more precise relevance model to reorder the initially retrieved candidates based on deeper query-document relevance, surfacing the actually helpful chunk higher
B. Remove the warranty document from the corpus entirely
C. Increase the number of initial candidates retrieved without any further relevance refinement
D. Switch exclusively to exact keyword matching with no semantic component

**Answer:** A
**Explanation:** Reranking with a more precise (typically cross-encoder) relevance model is designed exactly for this problem: initial embedding-based retrieval can surface lexically similar but intent-mismatched results, and reranking re-scores candidates against the actual query intent to improve final ordering. Removing the warranty document loses legitimately useful content for other queries, retrieving more unranked candidates doesn't fix relevance ordering, and pure keyword matching would lose semantic understanding needed for paraphrased queries.

### Q8.
An architect is evaluating retrieval quality for a newly deployed RAG system and wants an objective, repeatable method beyond "it looks right" during manual spot checks. What should be implemented?

A. Rely solely on end-user complaints as the quality signal
B. Build an evaluation set of representative queries with labeled relevant documents/passages, and measure standard retrieval metrics (e.g., precision@k, recall@k, or groundedness of generated answers) against it on an ongoing basis
C. Ask the model itself whether its own answer was correct, with no independent verification
D. Judge quality purely by how fast the retrieval step executes

**Answer:** B
**Explanation:** Rigorous retrieval quality assessment requires a labeled evaluation set and standard information-retrieval metrics (precision@k, recall@k) or groundedness checks, enabling objective, repeatable measurement rather than subjective impressions. Relying only on user complaints is reactive and incomplete, having the model self-grade its own answer lacks independent verification and is prone to confirmation bias, and retrieval speed is a latency metric, not a quality metric.

### Q9.
A government document-management system wants to ingest a mix of scanned handwritten forms, typed PDFs, and structured spreadsheets into a single RAG pipeline. What ingestion design consideration is most critical to get right first?

A. Treat all formats identically with one generic text extractor, since differences in format are not architecturally significant
B. Apply format-appropriate extraction (OCR with quality checks for scanned handwriting, PDF text extraction, structured parsing for spreadsheets) before chunking, since poor extraction quality at the source will propagate errors through the entire pipeline regardless of downstream chunking or embedding sophistication
C. Skip ingestion of handwritten forms entirely since OCR is never reliable enough to use
D. Convert spreadsheets to prose paragraphs using a generic summarizer before any other processing

**Answer:** B
**Explanation:** Ingestion quality is foundational — garbage extracted text, from poor OCR or format-blind generic extraction, will degrade every downstream stage no matter how well chunking, embeddings, or retrieval are tuned, so format-appropriate extraction with quality checks must come first. Treating all formats identically ignores real differences in extraction needs, dismissing handwritten OCR entirely discards potentially valuable content without even attempting the task, and prematurely summarizing structured data into prose can lose precise values needed for accurate retrieval.

### Q10.
A telecom company's RAG-based network-troubleshooting assistant frequently retrieves outdated documentation because the vector index was built once at launch and never updated as internal wikis changed. What pipeline design addresses this?

A. Rebuild the entire index manually once per year
B. Implement an ongoing ingestion/indexing pipeline that detects source document changes (e.g., via webhooks, change-detection polling, or CDC) and incrementally updates or re-embeds affected chunks, keeping the index synchronized with source-of-truth content
C. Instruct the model via the system prompt to "assume documentation might be outdated"
D. Stop using RAG entirely and rely on periodic manual fine-tuning instead

**Answer:** B
**Explanation:** A production RAG pipeline needs an ongoing synchronization mechanism (change detection and incremental re-indexing) to keep retrieval content current with the evolving source of truth, rather than treating ingestion as a one-time event. Annual manual rebuilds leave long windows of staleness, prompt disclaimers don't fix the underlying stale-data problem, and abandoning RAG for periodic fine-tuning is a much heavier, slower, and less appropriate solution for keeping fast-changing operational documentation current.

### Q11.
A SaaS company embeds both short FAQ snippets (avg. 50 tokens) and long technical whitepapers (avg. 5,000 tokens per chunk) in the same vector index using the same fixed chunk-size strategy applied uniformly. Retrieval quality suffers for FAQ-type queries. What should the architect reconsider?

A. Apply a uniform chunking strategy to all content types, since consistency is always the top priority
B. Tailor chunking strategy to content type (e.g., keep FAQ entries as natural, small self-contained units; use section-based chunking with overlap for long whitepapers) rather than forcing one fixed size across fundamentally different content
C. Remove all FAQ content from the knowledge base since whitepapers are more authoritative
D. Increase the whitepaper chunk size further to compensate for the issue

**Answer:** B
**Explanation:** Different content types often warrant different chunking approaches — short, naturally atomic content like FAQs benefits from being kept intact, while long technical documents need structure-aware splitting — and forcing one-size-fits-all chunking across heterogeneous content is a common source of degraded retrieval quality. Rigid uniformity is the actual problem here, not a goal to double down on; removing FAQ content discards valuable short-form answers; and simply enlarging whitepaper chunks doesn't address the FAQ-specific quality issue.

### Q12.
An architect designing a RAG pipeline for a multinational manufacturing company must support documents in multiple languages (English, German, Japanese) with cross-lingual queries (e.g., an English query should retrieve relevant German documentation). What embedding approach is required?

A. Use a monolingual, English-only embedding model and machine-translate all non-English documents to English before embedding, accepting translation artifacts
B. Use a multilingual embedding model trained to place semantically equivalent content from different languages close together in vector space, enabling direct cross-lingual retrieval without a separate translation step
C. Maintain entirely separate, language-specific vector indexes with no cross-lingual retrieval capability at all
D. Embed only the document titles, ignoring body content, to simplify multilingual handling

**Answer:** B
**Explanation:** A multilingual embedding model designed to align semantically equivalent meaning across languages in a shared vector space is the standard solution for cross-lingual retrieval, avoiding both translation-induced artifacts and the loss of cross-lingual capability from separate indexes. Pre-translating everything to English introduces translation errors and extra pipeline steps, maintaining fully separate language indexes defeats the cross-lingual requirement outright, and embedding only titles discards the substantive content needed for accurate retrieval.

### Q13.
A logistics company notices that its RAG pipeline's retrieval quality metrics look good in testing but degrade in production because real user queries are often short, informal, and contain typos (e.g., "wheres my pakage"), unlike the well-formed test queries used for evaluation. What should the architect do?

A. Reject all informal or misspelled queries and require users to rephrase them perfectly
B. Expand the evaluation set to include realistic, representative production-style queries (informal phrasing, typos, abbreviations) so retrieval quality is measured and tuned against conditions that reflect real usage, not just idealized test queries
C. Ignore the discrepancy since production metrics are not meaningful for RAG systems
D. Switch to exact-match keyword search only, since it handles typos better than semantic search

**Answer:** B
**Explanation:** Evaluation sets must reflect real-world query distribution (including informal phrasing and typos) or retrieval quality metrics will be misleadingly optimistic; expanding the eval set to match production reality is the correct diagnostic and design step. Rejecting imperfect queries creates poor user experience, dismissing production metrics ignores the very signal that matters most, and pure exact-match keyword search generally handles typos and paraphrasing worse than semantic approaches, not better.

### Q14.
A healthcare organization's RAG pipeline retrieves clinical guideline chunks correctly, but the final generated answer sometimes includes details not actually present in any retrieved chunk (i.e., the model appears to be filling gaps from its own training data). What pipeline-level mitigation most directly reduces this risk?

A. Increase the model's temperature to make answers more varied
B. Strengthen groundedness through prompt instructions requiring citation of retrieved sources, combined with a post-generation validation/verification step that checks claims against the retrieved context before returning the answer to the clinician
C. Remove retrieval entirely and rely purely on the model's parametric knowledge, which is assumed to be more reliable
D. Retrieve fewer chunks so the model has less material to potentially misuse

**Answer:** B
**Explanation:** Combining explicit grounding/citation instructions with a verification step that checks generated claims against the actually retrieved context is the standard way to reduce ungrounded "hallucinated" additions in RAG outputs, which is especially critical in healthcare. Raising temperature increases variability and would likely worsen hallucination risk, abandoning retrieval removes the very mechanism meant to ground answers in current guidelines, and simply retrieving fewer chunks does not address the model's tendency to add unsupported content and could reduce answer completeness.

### Q15.
An architect designing a new enterprise RAG pipeline for a large law firm must decide between: (a) one large unified vector index across all practice areas, or (b) multiple indexes partitioned by practice area (litigation, M&A, IP) with a routing layer selecting the relevant index per query. Which factors should drive this decision?

A. Always choose option (a), since a single index is simpler to operate regardless of scale or access-control needs
B. Evaluate factors such as corpus size and query latency at scale, the need for practice-area-specific access permissions, and whether queries naturally map to a single practice area versus requiring cross-practice retrieval — partitioning (b) tends to help with scale, permissions, and relevance precision, while unified indexing (a) is simpler when corpora are small and access is uniform
C. Always choose option (b) regardless of corpus size, since partitioning is strictly better in every scenario
D. The decision should be based solely on which option the embedding model vendor recommends in their marketing materials

**Answer:** B
**Explanation:** This is a genuine architectural trade-off: partitioned indexes often improve scale, enforce access boundaries naturally (e.g., per practice area), and can improve relevance precision when queries map cleanly to one domain, while a unified index is simpler to maintain when the corpus is small and permissions are uniform across content — the right choice depends on these concrete factors, not a universal rule. Blanket "always choose A" or "always choose B" rules ignore the real trade-offs, and vendor marketing materials are not an appropriate basis for an architectural decision.

### Q16.
An engineering team is ingesting a mix of dense financial tables and narrative commentary from scanned 10-K filing PDFs. To save cost, they default every page to text-extraction-only processing, which is roughly seven times cheaper per page than full visual understanding. Users then complain that table values are frequently garbled or misaligned in generated answers. What is the correct remediation?

A. Switch every page in the corpus to full visual understanding regardless of content, since more expensive processing is always safer
B. Treat the processing mode as a deliberate cost-versus-quality decision per document type: use full visual understanding (which processes each page as both text and image) for pages where layout carries meaning, such as dense tables, and keep cheaper text extraction for plain narrative pages
C. Keep text-extraction-only for all pages and ask the model to "double-check" table values in the prompt instead
D. Abandon PDF ingestion entirely and require all filings to be manually retyped into plain text

**Answer:** B
**Explanation:** PDF processing mode is a cost decision, not a fixed quality setting — text extraction alone is far cheaper but discards layout information, while full visual understanding costs substantially more (on the order of seven times as many tokens for the same pages) but is worth paying specifically where layout carries meaning, such as tables, forms, or diagrams; applying it selectively by content type gets the benefit without paying the premium everywhere. Defaulting everything to the expensive mode wastes spend on narrative-only pages, prompting the model to "double-check" values it never received correctly cannot recover information lost at extraction, and abandoning PDF ingestion entirely discards a solvable problem in favor of an impractical manual process.

### Q17.
A legal-tech company's RAG system cites entire multi-paragraph pages for every answer, and attorneys complain the citations are too coarse to verify quickly. Separately, a different team assumes that enabling citations on their search-based retrieval tool was automatic and discovers in testing that no citations appear at all. What should the architecture team conclude about both issues?

A. Both issues require only a prompt change asking the model to "cite more precisely" and to "always include citations"
B. Citation granularity is determined by the boundaries of the retrieval unit supplied — the model cites whole blocks, not substrings within them, so finer citations require splitting content into smaller blocks at ingestion — and citations are disabled by default for search results and must be explicitly enabled, not assumed
C. Citations are a purely cosmetic UI feature with no connection to how content was chunked or ingested
D. Both issues can only be fixed by switching to a completely different embedding provider

**Answer:** B
**Explanation:** Because the minimal citable unit is the block supplied to the model (which cites whole blocks, never substrings), coarse citations are fixed by changing ingestion-time chunk/block boundaries rather than by prompting, and because citations on search results are disabled by default, a team that assumes they are automatic will ship without any attribution until they explicitly enable the behavior. Prompt instructions cannot create citation granularity that the underlying blocks don't support or enable a feature that is off by default, citation behavior is directly tied to how content was structured at ingestion (not purely cosmetic), and the embedding provider is unrelated to either the citation-granularity or citation-enablement problem described.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
