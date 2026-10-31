# Objective 30: Address Ethical AI Considerations

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Address ethical AI considerations including bias detection, fairness, transparency, explainability, responsible AI, accountability, user disclosure, and monitoring discriminatory outcomes.

---

### Q1.
A bank's Claude-powered loan pre-screening assistant is found, after a quarterly fairness audit, to approve pre-screening at a meaningfully lower rate for applicants from certain zip codes that correlate strongly with race, even though race is never an input field. What is the most appropriate response?

A. Conclude there is no bias issue since race was never explicitly provided as an input
B. Treat zip code (and similar proxy variables) as a potential source of indirect/proxy discrimination, investigate the correlation, and adjust the model's inputs, prompts, or decision logic with ongoing disparate-impact monitoring
C. Stop performing fairness audits since they create legal risk by surfacing problems
D. Add a disclaimer to the application stating that results may vary by location

**Answer:** B
**Explanation:** Proxy discrimination (where a seemingly neutral variable like zip code correlates with a protected class) is a well-known fairness risk requiring active investigation and mitigation, not dismissal just because the protected attribute wasn't directly used. A is a common but incorrect assumption, and C and D avoid rather than address the underlying problem.

### Q2.
A hospital network wants to deploy a Claude-based tool to help triage patient messages by urgency. The ethics board asks what transparency measure should be provided to patients. What is the best practice?

A. Say nothing to patients, since disclosure might make them distrust the system
B. Clearly disclose to patients that an AI system is involved in triaging their messages, along with how a human clinician remains involved in final decisions
C. Only disclose AI involvement if a patient specifically asks
D. Disclose AI involvement only in the fine print of a lengthy terms-of-service document

**Answer:** B
**Explanation:** Proactive, clear user disclosure of AI involvement (and the role of human oversight) is a core transparency and responsible-AI practice, especially in healthcare contexts where patients have a right to understand how their care decisions are being supported. A, C, and D all represent inadequate or hidden disclosure that undermines trust and, in many jurisdictions, legal disclosure requirements.

### Q3.
A retail company's hiring-assistant tool built on Claude recommends candidates for interviews. A hiring manager asks "why was this candidate recommended over that one?" What capability should the system provide to support ethical, accountable AI use?

A. A generic statement that "the AI knows best"
B. An explainability feature that surfaces the specific factors or evidence (e.g., skills match, relevant experience) that contributed to the recommendation, in a way a human reviewer can evaluate and challenge
C. No explanation should ever be given, to protect proprietary model details
D. Only the final ranked list, with no supporting rationale

**Answer:** B
**Explanation:** Explainability — surfacing the factors behind a recommendation in human-interpretable terms — is essential for hiring managers to meaningfully evaluate, challenge, and take accountability for AI-assisted decisions, particularly given employment discrimination risk. A, C, and D leave the decision unexplainable and unaccountable.

### Q4.
A government agency's public benefits chatbot is found to give meaningfully less helpful and more frequently inaccurate answers to users writing in non-native English/dialectal patterns compared to standard English speakers. What ethical AI concern does this illustrate, and what should the agency do?

A. This is expected and acceptable since the model was trained primarily on standard English
B. This is a discriminatory outcome disparity requiring investigation, targeted evaluation across language/dialect variations, and remediation (e.g., improved prompting, additional evaluation data, or human fallback) to ensure equitable service quality
C. The agency should restrict the chatbot to only standard English speakers
D. No action is needed since the chatbot still provides some response to everyone

**Answer:** B
**Explanation:** Disparate quality of service correlated with language/dialect (which often correlates with national origin or socioeconomic factors) is a discriminatory outcome that government services must actively monitor and remediate, consistent with equity obligations. A and D normalize an inequitable outcome, and C would unlawfully exclude a population from public services.

### Q5.
A manufacturing company's internal "Responsible AI" policy requires that any AI system influencing employee performance evaluations have a named accountable owner within the organization. What is the purpose of this requirement?

A. To have someone to blame if the AI vendor is sued
B. To ensure there is clear organizational accountability for the system's design, monitoring, and outcomes, so that governance, escalation, and corrective action have a responsible party rather than diffusing responsibility onto "the algorithm"
C. To satisfy a purely bureaucratic checkbox with no practical effect
D. To allow the AI system to operate without any further oversight once an owner is named

**Answer:** B
**Explanation:** Assigning clear accountability ensures a real person/team is responsible for governance, monitoring, and remediation of an AI system's impacts — a core "accountability" principle in responsible AI frameworks, preventing diffusion of responsibility. A is a cynical mischaracterization, and C and D misunderstand the ongoing-oversight purpose of the requirement.

### Q6.
A telecom company's customer-churn prediction assistant (built on Claude plus structured data) is used to prioritize retention offers. An internal audit reveals that older customers are systematically deprioritized for retention outreach at a rate not justified by actual churn risk or value. What should the architecture and governance team do first?

A. Ignore the finding since age is not a legally protected class in all jurisdictions where the company operates
B. Investigate whether age (or a proxy for it) is driving the disparity independent of legitimate business factors, and if so, correct the logic/model and establish ongoing monitoring for this and other discriminatory patterns
C. Quietly stop auditing for this type of disparity going forward
D. Ask Claude to explain why older customers are being deprioritized and accept that explanation as the final answer

**Answer:** B
**Explanation:** Age is a protected class in many jurisdictions and a legitimate fairness concern regardless, so the correct response is a substantive investigation and correction with ongoing monitoring, not dismissal based on a jurisdictional technicality. A is risky and incomplete, C actively undermines governance, and D treats a model-generated explanation as authoritative without independent verification — explanations from the model itself are not a substitute for rigorous bias testing.

### Q7.
A legal services nonprofit builds a Claude-based tool to help pro se litigants understand court procedures. Leadership debates whether to disclose that the guidance is AI-generated versus presenting it as if from a human staff attorney to seem more authoritative. What is the ethically and professionally appropriate choice?

A. Present it as human-generated, since it increases user trust and usage
B. Clearly disclose that the guidance is AI-generated and is not a substitute for legal advice from a licensed attorney, preserving user autonomy and informed reliance
C. Only disclose AI involvement if a user explicitly asks
D. Avoid any disclaimer since the tool is "basically as good as a lawyer"

**Answer:** B
**Explanation:** Honest, upfront user disclosure of AI involvement and its limitations (especially in legal contexts, where it also has professional-ethics implications around unauthorized practice of law) is required for informed user reliance and transparency. A, C, and D all involve misleading users about the nature and limitations of the guidance they're receiving.

### Q8.
A manufacturing company's internal audit team wants to proactively test their Claude-based HR assistant for bias before it is deployed broadly, rather than waiting for complaints. What testing approach best supports this goal?

A. Deploy the tool broadly first and only investigate if an employee files a formal complaint
B. Run structured fairness testing using representative test sets across demographic groups and scenario variations, comparing outcome rates and quality before and during deployment, with ongoing monitoring post-launch
C. Rely on the AI vendor's general claim that "our model is unbiased"
D. Test only with a small group of engineers who built the tool

**Answer:** B
**Explanation:** Proactive, structured fairness testing across representative groups and scenarios — both pre-launch and ongoing — is the recommended practice for catching discriminatory patterns before they cause harm, rather than waiting reactively for complaints. A is reactive and harmful, C is an unverified vendor claim, and D lacks the representativeness needed to detect bias.

### Q9.
A SaaS company's marketing team wants to use a Claude-based tool to generate ad copy variations and automatically target different copy to different demographic segments. The ethics review raises a concern. What is most likely the concern?

A. Ad copy generation is inherently unethical regardless of context
B. Automated demographic-based targeting combined with AI-generated variations could inadvertently create discriminatory advertising practices (e.g., disparate impact in housing, credit, or employment ad categories) if not carefully governed
C. There is no ethical concern since the content is just marketing copy
D. The concern is purely about copyright, not fairness

**Answer:** B
**Explanation:** Demographic-targeted advertising intersects with anti-discrimination law and ethical AI concerns, particularly in regulated ad categories (housing, credit, employment) where targeting itself can be unlawfully discriminatory — this requires governance review regardless of how the copy was generated. A overstates the concern, and C and D understate or misdirect it.

### Q10.
An insurance company wants its Claude-based underwriting-support tool to be "explainable" to regulators who may audit specific denied applications. Which design choice best supports this goal?

A. Use the AI's output as the sole and final justification with no supporting data
B. Architect the system so that each recommendation is tied to specific underlying rating factors and data points that can be retrieved and presented in a regulator-readable format, separate from the model's free-form prose
C. Avoid keeping any record of what data led to a given underwriting outcome
D. Explain decisions only in internal technical jargon not understandable by regulators or policyholders

**Answer:** B
**Explanation:** Regulator-facing explainability requires traceable linkage between a decision and the specific, retrievable underlying factors in a clear format — not just the model's prose, which can vary and may not reliably reflect the true decision logic. A, C, and D all fail to provide a defensible, comprehensible explanation.

### Q11.
A customer-facing chatbot for a logistics company is asked directly by a user: "Are you a real person or an AI?" What is the appropriate, ethical response design?

A. The bot should claim to be a human to seem more relatable
B. The bot should truthfully disclose that it is an AI assistant when asked (and ideally proactively, depending on jurisdictional requirements), consistent with transparency and anti-deception principles
C. The bot should deflect the question entirely and change the subject
D. The bot should only admit it is an AI if pressed multiple times

**Answer:** B
**Explanation:** Truthful disclosure of AI identity when asked (and often proactively, per emerging bot-disclosure laws in various jurisdictions) is a core transparency principle preventing user deception. A, C, and D all involve deceptive or evasive practices that undermine user trust and may violate disclosure regulations.

### Q12.
A government agency's Claude-based tool assists caseworkers in assessing child welfare risk scores. Civil rights advocates raise concerns about potential racial bias in historical case data used to build retrieval examples. What is the most responsible path forward?

A. Proceed without changes since the tool is "just a decision support aid" and caseworkers make the final call
B. Conduct a rigorous fairness and bias assessment of the historical data and retrieval examples, engage external stakeholders/civil-rights reviewers, and implement bias mitigation and ongoing outcome monitoring before and after deployment, given the severity of potential harm
C. Remove all human caseworker involvement to eliminate human bias from the process
D. Dismiss the concerns since the tool only "assists" and doesn't make binding decisions

**Answer:** B
**Explanation:** Given the severe real-world consequences of child-welfare decisions, a rigorous, externally-validated fairness assessment and ongoing monitoring is warranted — "it's just a decision aid" is not a sufficient defense against bias risk, since decision aids measurably influence human judgment (automation bias). A and D minimize real risk, and C misunderstands that removing humans doesn't resolve biased underlying data and could remove a check on AI bias.

### Q13.
A financial advisory SaaS platform wants to use Claude to generate personalized investment suggestions. The compliance team asks how to ensure "accountability" if a suggestion leads to a customer complaint or regulatory inquiry. What should be in place?

A. No specific accountability mechanism is needed since the AI vendor bears all responsibility
B. A clear internal governance structure defining who reviews/approves AI-assisted investment content, documented testing/validation processes, and records showing human oversight and responsibility for the content delivered to customers
C. A statement in the terms of service disclaiming all responsibility for AI output
D. Accountability is unnecessary as long as the suggestions are statistically reasonable

**Answer:** B
**Explanation:** Real accountability requires documented internal governance — defined ownership, review processes, and evidence of human oversight — not just vendor reliance or a disclaimer, especially in a regulated financial-advice context. A and C attempt to offload responsibility inappropriately, and D ignores the governance/documentation requirement.

### Q14.
A manufacturing company deploys a Claude-based tool to screen job applicants' resumes. Several months in, the diversity team notices candidate pools reaching final interviews have become less diverse than before the tool's deployment, though no single factor is obviously to blame. What is the best next step?

A. Assume this is a coincidental trend unrelated to the AI tool
B. Conduct a structured, periodic outcome audit comparing diversity metrics before and after tool deployment, drilling into which stages/criteria of the AI-assisted process may be contributing, since discriminatory outcomes can emerge from subtle, compounding factors
C. Discontinue tracking diversity metrics to avoid drawing unwanted scrutiny
D. Ask the AI tool itself whether it is being biased and trust its self-assessment

**Answer:** B
**Explanation:** Monitoring discriminatory outcomes requires structured, periodic auditing of real-world results (not assumptions), especially since bias can emerge from subtle, compounding effects across a multi-stage process. A and C avoid addressing a real signal, and D wrongly treats model self-report as a reliable bias-detection method.

### Q15.
A retail company's AI ethics committee is evaluating whether their Claude-based pricing-recommendation tool could lead to price discrimination against certain customer groups based on inferred characteristics (e.g., device type correlating with income level). What principle should guide their review?

A. Price discrimination concerns only apply to explicitly protected characteristics, so inferred proxies are not a concern
B. The committee should evaluate whether inferred characteristics (even indirect proxies) used in pricing decisions could produce unfair or discriminatory impact, since fairness analysis must consider proxy variables and real-world disparate impact, not just explicit protected-class fields
C. Pricing algorithms are inherently neutral and cannot be discriminatory since they are based on data, not opinions
D. No review is necessary since the company does not explicitly collect race, gender, or age data

**Answer:** B
**Explanation:** A rigorous fairness review must consider proxy variables and actual disparate impact on protected or vulnerable groups, not just whether explicit protected-class fields were used as direct inputs — this mirrors established legal and ethical standards around disparate impact. A, C, and D all reflect the common but incorrect assumption that avoiding explicit protected fields is sufficient to avoid discriminatory outcomes.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
