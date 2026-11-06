# Notebook 09 Defense README

**H3 Denial of Service — Comparing Lost Scans with Store and Forward Recovery**

**Paired notebook:** [`09_Praxis_H3_DoS_Analysis.ipynb`](./09_Praxis_H3_DoS_Analysis.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

The notebook keeps a set of 75 disrupted RFID scans fixed and tests two conditions. In the baseline, the backend never receives the affected scans. In the mitigation condition, some scans are buffered and sent later. The point is to measure continuity of tracking records, not to claim that an attacker was detected by a live network sensor.

**Research connection:** RQ3/H3: Does a modeled continuity control reduce the impact of the same simulated DoS interruptions on baggage scan availability?

**The one thing to remember:** The baseline data are preserved; backend availability is what changes. Event loss and file deletion are not the same concept.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Review affected events

**What happens and why:** Loads prepared RFID data with 31,575 rows, identifies 75 DoS affected scans and 10 disruption groups.

**What a professor may challenge:** The known disruption label defines the experimental population; it is not a prediction.

### 2.2 Create the no mitigation baseline

**What happens and why:** Treats all 75 affected scans as unavailable in a separate working copy of backend records.

**What a professor may challenge:** 75 losses and 75 incomplete baggage journeys describe this scenario, not physical destruction of the original CSV.

### 2.3 Apply store and forward

**What happens and why:** Simulates an assumed 90% buffering chance and 95% restoration chance for buffered scans.

**What a professor may challenge:** The displayed realization buffers 66 of 75 and restores 64 of the 66; these are outcome counts, not exactly 90% and 95%.

### 2.4 Calculate impacts and timing

**What happens and why:** Compares permanent record loss and incomplete custody paths. Uses separate original scan and recovery timestamps.

**What a professor may challenge:** Do not assign a numeric staleness value to a baseline scan that never arrived.

### 2.5 Validate and save

**What happens and why:** Checks the same affected set was used, that all event outcomes add up, and that original data were unchanged.

**What a professor may challenge:** Reproducible simulations require accounting checks, not just an attractive chart.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. No mitigation: **75 permanently unavailable scan records** and **75 incomplete baggage journeys**.
2. Store and forward: **66 buffered**, **64 restored**, **11 permanently unavailable**.
3. The realized overall recovery rate is **64 / 75 = 85.33%** and the reduction in permanent losses is **85.33%**.
4. Of the 66 buffered events, **64 / 66 = 96.97%** were restored.
5. Mean modeled recovery delay was **2.70 minutes**; mean record staleness among restored events was **23.34 minutes**.
6. This supports H3 for a modeled continuity control, but not the independent effectiveness of automatic attack detection.

### One calculation worth remembering

**Overall recovered = 64 / 75 = 85.33%.** Recovery from buffered events = 64 / 66 = 96.97%. These are different denominators.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Do not describe the 85.33% recovery as an observed airport performance statistic or confuse buffering effectiveness with detection effectiveness.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `05_Praxis_H3_DoS_Analysis (2)(1).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **Store and forward** | Keeping an event temporarily when the connection is unavailable, then sending it after communications return. |
| **Backend** | The central system expected to receive and store baggage scan events. |
| **Permanent event loss** | A scan event that is never delivered to the backend in the scenario. |
| **Incomplete custody path** | A bag journey missing a scan needed for the expected movement history. |
| **Recovery delay** | How long after service returns before a buffered scan becomes available. |
| **Record staleness** | How old the scan information is when it finally reaches the backend. |
| **Assumed parameter** | A rate chosen for the simulation rather than observed in live airport operations. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: What actually changes between the two conditions?

**Plain English answer:** The set of 75 affected scans stays the same. Only the modeled ability to hold and later restore scans changes.

### Question 2: Why were 64 scans restored rather than 90% of 75?

**Plain English answer:** The 90% setting applies to buffering and a separate 95% setting applies to restoration. The simulated realization buffered 66, then restored 64, so the overall recovered share is 64 out of 75.

### Question 3: Why are 75 baseline records counted as lost if the CSV still has them?

**Plain English answer:** Loss here means unavailable to the modeled backend. The source CSV is preserved to compare scenarios; it was not physically deleted.

### Question 4: Why is baseline record staleness blank?

**Plain English answer:** An event that never reaches the backend has no finite arrival time. Giving it an invented delay would make the comparison misleading.

### Question 5: Does this show analytics detected 75 DoS events?

**Plain English answer:** No. The notebook uses the known DoS labels to select cases and evaluates buffering and recovery. It does not independently detect attacks.

### Question 6: Does the 85.33% reduction prove a real airport benefit?

**Plain English answer:** It shows the benefit of the specified buffering and restoration assumptions for this simulated population. Different network behavior, device storage limits, or failure patterns could change the outcome.

### Question 7: Why preserve the original event timestamp?

**Plain English answer:** It records when the scan occurred. The recovery timestamp records when the backend received it, allowing staleness and delay to be measured without rewriting history.

### Question 8: What is the best defense statement for H3 at this stage?

**Plain English answer:** A store and forward continuity method reduced simulated missing records and incomplete paths. An added benefit from cybersecurity analytics still requires separate evidence.

## 7. A Natural Way to Explain It Out Loud

> Notebook 09 tests what happens to tracking records when communications are interrupted. Without mitigation, all 75 affected scans stay unavailable to the backend. With store and forward, 66 were buffered and 64 eventually reached the backend, reducing modeled permanent losses from 75 to 11. That supports the continuity method under the selected assumptions. It does not show that cybersecurity analytics independently detected or stopped the disruption.

## 8. Last Minute Defense Checklist

- [ ] Explain the problem and the experiment in less than a minute.
- [ ] Identify the **source dataset** and whether it is simulated or public.
- [ ] Explain what was compared and which results came from the same records.
- [ ] State the main **numerator and denominator** for the key percentage.
- [ ] Define the hardest term without quoting Python code.
- [ ] Describe at least one **weakness or assumption** without dismissing it.
- [ ] Separate what the output **supports** from what it **does not prove**.
- [ ] Confirm each exact figure against the latest GitHub notebook before the defense.

## 9. Writing Pattern Review (Heuristic, Not Turnitin)

**Review purpose:** Check whether these notes read like specific, understandable research explanations. This is a documented writing pattern review; it is not a proprietary Turnitin report, an AI authorship verdict, or a prediction of a detector score.

**Sentence pattern measure:** 85 longer prose sentences reviewed. Average length approximately 15.0 words; length variation approximately 5.4 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (5); “what a professor may” (5); “what happens and why” (5)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
