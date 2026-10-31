# Objective 6: Align Architecture with Business Value

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Align Claude-based architecture decisions with measurable business value, including efficiency gains, productivity improvements, broader business transformation, cost reduction, performance against service-level agreements, and demonstrable return on investment tied to business impact.

---

### Q1.
A bank's Claude-based document processing system reduces average loan-document review time from 45 minutes to 12 minutes per file. Which statement BEST reflects proper business-value alignment in reporting this result?

A. Reporting only that "the system uses Claude 4" without any performance data
B. Reporting the reduced review time alongside the resulting throughput increase, reviewer labor cost saved, and impact on loan-approval cycle time
C. Reporting only the number of API calls made during the pilot
D. Reporting only that the development team enjoyed building the system

**Answer:** B
**Explanation:** Business-value reporting should translate technical performance (time per file) into business outcomes — cost saved, throughput gained and downstream cycle-time impact — which stakeholders can act on. A, C and D report technical or anecdotal detail that does not connect to measurable business impact.

### Q2.
A manufacturing company evaluating a Claude-based predictive-maintenance assistant must decide whether the project is worth pursuing. Which analysis BEST supports that decision?

A. Comparing the project's estimated implementation and ongoing API cost against the expected reduction in unplanned downtime and associated revenue loss
B. Comparing only the novelty of the technology against competitors' marketing claims
C. Counting the number of sensors already installed on the factory floor
D. Estimating how many engineers would enjoy working on the project

**Answer:** A
**Explanation:** A sound ROI case weighs full cost (build plus ongoing run cost) against quantifiable business benefit (reduced downtime and associated revenue protection), which is the correct basis for an investment decision. B, C and D do not address cost-versus-benefit at all.

### Q3.
A telecom company's customer support architecture has a target SLA of responding to 95% of chat inquiries within 30 seconds. Early testing shows a multi-agent orchestration design meets accuracy goals but averages 90 seconds per response due to sequential subagent calls. What is the BEST next step?

A. Accept the design since accuracy is more important than speed in all cases
B. Re-evaluate whether the subtasks can be parallelized, whether a simpler pattern would meet both accuracy and the SLA, or whether the SLA itself needs renegotiation with the business
C. Ignore the SLA since it was set arbitrarily
D. Reduce accuracy requirements without informing stakeholders to hit the SLA

**Answer:** B
**Explanation:** When an architecture fails to meet an agreed SLA, the correct response is to explore legitimate architectural alternatives (parallelization, simpler patterns) or to renegotiate the SLA transparently with the business, rather than silently sacrificing quality or ignoring the target. A dismisses a real constraint, C disregards a committed business requirement, and D is a dishonest and risky shortcut.

### Q4.
A retail company's leadership asks whether their new Claude-powered product-tagging tool delivered "business transformation" or merely "efficiency gains." Which outcome would qualify as business transformation rather than simple efficiency?

A. Tagging the same number of products in half the time with the same catalog structure
B. Enabling an entirely new personalized-search capability across the catalog that was not previously feasible, opening a new revenue channel
C. Reducing the number of typos in product tags
D. Running the tagging process on a faster server

**Answer:** B
**Explanation:** Business transformation refers to enabling fundamentally new capabilities or business models that were not previously possible, such as a new revenue-generating feature, rather than simply doing the same work faster or more cheaply. A, C and D describe incremental efficiency or quality improvements, not transformation.

### Q5.
An insurance company's architect proposes an autonomous multi-agent claims system projected to cost 3x more annually than the current semi-automated workflow, while improving processing speed by only 8%. What should the architect recommend?

A. Proceed regardless of cost since autonomous agents are strategically important
B. Present the cost-benefit trade-off clearly to the business, since a 3x cost increase for an 8% speed gain likely fails to justify the investment, and propose a lower-cost architecture that may deliver comparable business value
C. Proceed without informing the business of the cost increase
D. Recommend doubling the budget further to accelerate agent development

**Answer:** B
**Explanation:** Sound architecture decisions require transparently weighing cost against actual measured benefit; a disproportionate cost increase for marginal gains should prompt the architect to recommend a more cost-effective alternative rather than proceeding blindly. A, C and D all ignore the business's legitimate interest in a favorable cost-benefit ratio.

### Q6.
A SaaS company wants to justify continued investment in its Claude-based code-review assistant. Which metric BEST demonstrates measurable ROI to finance stakeholders?

A. The number of distinct prompt templates created
B. Developer hours saved per week multiplied by average loaded developer cost, compared against the tool's total operating cost
C. The number of GitHub stars on the open-source libraries used
D. The total number of tokens processed per month

**Answer:** B
**Explanation:** ROI calculations require translating operational savings into monetary terms (hours saved times cost) and comparing that to total spend, which is directly meaningful to finance stakeholders. A, C and D are technical or vanity metrics with no direct financial translation.

### Q7.
A hospital network's Claude-based intake assistant meets its accuracy targets but increases average patient wait time because the architecture requires three sequential model calls per patient. Leadership's primary KPI is patient throughput. What is the architect's BEST course of action?

A. Celebrate the accuracy win and consider the project complete
B. Investigate whether some of the three sequential calls can be parallelized, combined, or replaced with deterministic logic to reduce latency, since the architecture is currently misaligned with the business's primary throughput KPI
C. Recommend hiring more intake staff instead of using the tool at all
D. Reduce the number of patients served per day to maintain accuracy

**Answer:** B
**Explanation:** When an architecture achieves a secondary goal (accuracy) but undermines the primary business KPI (throughput), the architect must revisit the design to better align with what the business actually values most, exploring latency-reduction techniques. A ignores the core business priority, and C and D abandon the automation's value rather than fixing the misalignment.

### Q8.
A government agency wants to justify a Claude-based citizen-inquiry system to its oversight board using cost-reduction framing. Which comparison is MOST appropriate?

A. Comparing the system's cost to an unrelated agency's unrelated IT project
B. Comparing the fully loaded cost of current manual inquiry handling (staff time, overhead) against the total cost of the new system (build, run, oversight), across a consistent time horizon
C. Comparing only the salary of one employee to the system's monthly API bill
D. Comparing the system's cost to its own marketing budget

**Answer:** B
**Explanation:** A valid cost-reduction case requires an apples-to-apples comparison of fully loaded current-state cost against fully loaded future-state cost over the same time horizon. A, C and D all introduce irrelevant or incomplete comparisons that would mislead the oversight board.

### Q9.
A logistics company's architect is choosing between two designs: Design X costs less but cannot guarantee the agreed 99.5% on-time delivery-notification SLA; Design Y costs more but reliably meets it. The business has stated that missing this SLA triggers contractual penalties exceeding Design Y's added cost. What should the architect recommend?

A. Design X, because it is cheaper
B. Design Y, because the cost of SLA non-compliance (contractual penalties) exceeds the additional cost of the architecture that reliably meets it
C. Neither design, since SLAs should be ignored in architecture decisions
D. Design X, with a plan to apologize to customers if the SLA is missed

**Answer:** B
**Explanation:** When the financial consequence of missing an SLA is quantified and exceeds the incremental cost of a more reliable design, the economically rational and business-aligned choice is the design that reliably meets the SLA. A and D optimize narrowly for upfront cost while ignoring larger downstream financial risk, and C dismisses a legitimate business constraint.

### Q10.
A manufacturing executive asks an architect to describe the "productivity" impact, as distinct from "efficiency," of a new Claude-based engineering-documentation assistant. Which answer BEST distinguishes the two?

A. Efficiency and productivity mean exactly the same thing in this context
B. Efficiency refers to completing the same documentation work with less time or cost, while productivity refers to engineers now producing a greater volume or richer scope of documentation output in the same time, enabling more total work to get done
C. Efficiency refers only to server costs, and productivity refers only to employee satisfaction
D. Productivity cannot be measured for knowledge work

**Answer:** B
**Explanation:** Efficiency and productivity are related but distinct: efficiency is doing the same work with fewer resources, while productivity is the increase in valuable output achievable within the same resources, and a good business-value narrative distinguishes both. A collapses an important distinction, and C and D are inaccurate or dismissive mischaracterizations.

### Q11.
A SaaS company reports that its Claude-based onboarding assistant "saved 10,000 hours this year" without connecting that figure to any cost or revenue outcome. What is the architect's BEST critique of this reporting?

A. The number is impressive on its own and needs no further context
B. The figure should be translated into a dollar value (hours saved multiplied by loaded cost) or linked to a business outcome like faster time-to-value for customers, to be meaningful to business stakeholders
C. Hours saved is not a legitimate metric at all
D. The report should instead focus exclusively on the number of Claude API calls made

**Answer:** B
**Explanation:** Raw operational metrics like "hours saved" only become actionable business evidence once translated into financial or outcome terms that stakeholders can weigh against cost and strategic priorities. A leaves the metric disconnected from decision-making value, and C and D dismiss or misdirect the reporting entirely.

### Q12.
An architect is asked to align a Claude-based legal-research tool's design with the firm's stated business goal of "winning more client retention through faster turnaround." Which design choice BEST reflects this alignment?

A. Prioritizing the cheapest possible architecture regardless of turnaround time
B. Prioritizing an architecture that measurably reduces research turnaround time, even at moderately higher operating cost, since faster turnaround is the explicitly stated driver of the targeted business outcome (client retention)
C. Prioritizing the most technically novel architecture available
D. Prioritizing a design that minimizes the number of Claude API calls regardless of its effect on turnaround time

**Answer:** B
**Explanation:** Architecture decisions should be driven by the specific business outcome the stakeholder cares about; since turnaround time was explicitly named as the retention driver, an architecture optimized for that metric, even at some added cost, is correctly aligned. A, C and D optimize for factors unrelated or secondary to the stated business goal.

### Q13.
A telecom provider's finance team asks the architect to quantify the ROI of a Claude-based network-fault-triage system before renewing its contract. Which calculation BEST represents a credible ROI case?

A. (Value of reduced outage time and reduced manual triage labor − total system cost) ÷ total system cost, expressed as a percentage
B. The number of faults detected, with no cost comparison
C. The architect's personal estimate of how "useful" the system feels
D. The total number of lines of integration code written

**Answer:** A
**Explanation:** A credible ROI calculation nets the quantified business benefit against total cost and expresses it as a return percentage, giving finance a standard, comparable figure for the renewal decision. B, C and D either omit cost entirely or substitute subjective or irrelevant measures for a financial calculation.

### Q14.
A manufacturing company implemented a Claude-based assistant that reduced defect-report turnaround time but the business has seen no change in overall product recall rates, which was the original stated goal. What should the architect conclude?

A. The project is successful because turnaround time improved
B. The architecture may be solving a proxy metric (turnaround time) without actually addressing the root business KPI (recall rate), and the design should be re-evaluated against the original success criterion
C. Recall rates are unrelated to defect reporting and should be ignored
D. The business should lower its expectations to match the turnaround-time improvement

**Answer:** B
**Explanation:** When a system improves an intermediate metric but fails to move the actual business KPI it was built to serve, the architect must revisit whether the design addresses the true causal driver of that KPI rather than declaring success on a proxy. A mistakes a proxy win for the real goal, and C and D avoid confronting the actual gap.

### Q15.
Which of the following BEST describes a mature business-value alignment practice for an enterprise Claude architecture program?

A. Defining success metrics once at project kickoff and never revisiting them regardless of business changes
B. Continuously tracking agreed KPIs (efficiency, cost, SLA compliance, ROI) post-launch, and using that data to justify further investment, course-correct the architecture, or sunset underperforming components
C. Relying solely on anecdotal praise from end users as the measure of success
D. Measuring success purely by how advanced or novel the underlying architecture pattern is

**Answer:** B
**Explanation:** Mature programs treat business-value alignment as an ongoing discipline, continuously measuring against agreed KPIs post-launch to inform investment, iteration or sunset decisions rather than a one-time exercise. A treats alignment as static, and C and D substitute subjective or technical vanity measures for genuine business-value tracking.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
