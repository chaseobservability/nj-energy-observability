## PR Rejection Response Templates

(You will use these more than you think. Having them written is power.)

Create a small internal file (or keep these handy).

---

### A. Rejection -- Nonpublic or Sensitive Data

Thanks for the contribution and for engaging with NJ Energy Observability.

We can't merge this PR as proposed because it relies on nonpublic or utility-confidential information. A hard boundary of this project is that all artifacts must be derived from publicly available sources so they can be independently verified by anyone.

If you're able to rework the contribution using only public data (or focus on structure, templates, or methodology), we'd be happy to take another look.

---

### B. Rejection -- Forecasting / Recommendations

Thanks for the thoughtful PR. We're going to decline this change in its current form.

NJ Energy Observability is intentionally limited to descriptive observability. We don't include forecasts, predictions, or recommended actions, even when they're well-intentioned.

If you'd like to reframe this contribution as a question, descriptive indicator, or governance artifact, that would be much more aligned with the project's scope.

---

### C. Rejection -- Metric Not Registered / Governance Drift

Thanks for the submission. Before we can consider merging this, the proposed metric needs to be registered in metrics/metric-catalog.yml with its taxonomy, allowed/disallowed claims, and baseline requirements defined.

This governance step is required so metrics don't drift into unintended uses over time. Once that's in place, we're happy to review again.

---

### D. Rejection -- Tone / Evaluation Risk

We appreciate the work here. We're going to hold off on merging this PR because the framing could be read as evaluating or judging specific actors or outcomes.

The project's role is to make systems observable, not to assess performance. If you can adjust the language to remain strictly descriptive, we'd welcome a revision.

---
