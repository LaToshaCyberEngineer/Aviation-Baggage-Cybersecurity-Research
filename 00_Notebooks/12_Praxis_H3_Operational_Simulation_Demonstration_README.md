# Notebook 12 Defense README

**H3 Operational Simulation — What Happens to Scan Queues and False Alerts**

**Paired notebook:** [`12_Praxis_H3_Operational_Simulation_Demonstration.ipynb`](./12_Praxis_H3_Operational_Simulation_Demonstration.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

Instead of presenting only an overall recovery percentage, this notebook models scan arrivals, buffer capacity, protective throughput, and the time at which alerts become active. It also runs a separate false alert trial on normal scans, which shows that security controls can themselves interfere with baggage tracking.

**Research connection:** Supplemental RQ3/H3. A minute by minute queue model tests whether modeled buffering and protective capacity preserve scan delivery, and whether false alarms harm otherwise normal processing.

**The one thing to remember:** Defense questions may target queue capacity, processing rate, false alert cost, and why 75 cases are used again. These are modeled, not field-measured.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Identify existing disruptions and alert settings

**What happens and why:** Uses 75 affected scans in 10 groups. The selected scenario has 0 rule alerts and 8 ML alerts.

**What a professor may challenge:** Those alerts are scenario settings, not freshly measured real time airport alarms.

### 2.2 Set queue and recovery assumptions

**What happens and why:** Defines buffer capacity 6, recovery capacity 2, response activation at minute 5, and protective capacity 1 scan per minute.

**What a professor may challenge:** These are the model settings that control outcomes; changing them can change the answer.

### 2.3 Place arrivals inside outage windows

**What happens and why:** Reconstructs simulated arrival times and checks they fit within each disruption.

**What a professor may challenge:** These new arrival times are operational modeling inputs, not original scanner timestamps.

### 2.4 Build minute by minute scan handling

**What happens and why:** For each minute, tracks new arrivals, outage state, whether alerts are active, queue contents, deliveries, and losses.

**What a professor may challenge:** The timeline makes it possible to see why scans were lost or delayed instead of only showing totals.

### 2.5 Compare four operating conditions

**What happens and why:** Runs no buffering, buffering only, rule response, and ML response on the same affected set.

**What a professor may challenge:** No buffering delivers 0; buffering and rule response deliver 60; ML response delivers 72 in the saved run.

### 2.6 Inspect charts and a disruption example

**What happens and why:** Shows queue and delivery behavior over time.

**What a professor may challenge:** A chart illustrates the modeled logic; it is not evidence of an actual operational airport system.

### 2.7 Vary response settings

**What happens and why:** Tests when response begins and how many scans can be protected per minute.

**What a professor may challenge:** The notebook verifies that an alert with zero protective capacity behaves like buffering alone.

### 2.8 Save outputs and run settings

**What happens and why:** Writes scenario summaries, per scan outcomes, queue timelines, sensitivity tables, figures, and a JSON settings file.

**What a professor may challenge:** The settings file matters for reproducibility.

### 2.9 Simulate a false alert on normal scans

**What happens and why:** Selects 75 otherwise normal scans and applies an unnecessary protective reaction.

**What a professor may challenge:** Under the chosen false alert rule, only 69 of 75 were delivered; normal processing delivered all 75.

### 2.10 Validate final accounts

**What happens and why:** Checks delivered plus lost equals the starting scan count in each scenario and saves the final summary.

**What a professor may challenge:** Counting every event prevents hidden losses and makes the simulation auditable.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. Modeled DoS scenarios on **75 affected scans**: no buffering **0/75 delivered**, buffering **60/75**, rule response **60/75**, ML response **72/75**.
2. Delivery rates: **0%**, **80%**, **80%**, and **96%**, respectively.
3. Average delay among delivered scans: **14.25 minutes** under buffering and **3.74 minutes** under the selected ML response run.
4. The sensitivity test shows **alerts alone do not help** when protected throughput is set to zero.
5. In the separate normal scan false alert test, unnecessary response delivered **69/75**, losing **6**, while ordinary processing delivered **75/75**.
6. These are simulated queue model outcomes using assumed capacities, not real baggage handling measurements.

### One calculation worth remembering

**ML scenario delivery = 72 / 75 = 96%. Buffering only = 60 / 75 = 80%.** An alert without protective capacity has no delivery advantage.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Do not use the 72/75 queue result as another independent confirmation of the 64/75 event restoration result in Notebook 09. They apply different modeled rules to the same underlying DoS affected population.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `11_H3_Operational_Simulation_Demonstration (1).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **Queue** | Records waiting to be delivered when the system cannot process them immediately. |
| **Buffer capacity** | The maximum number of waiting scan records stored in a modeled local queue. |
| **Throughput** | How many events the model can deliver or protect per minute. |
| **Store and forward** | Saving events locally for later delivery when communication resumes. |
| **Sensitivity analysis** | Changing a model setting to learn which assumptions drive the results. |
| **False alert** | An alarm raised even though the selected scans are normal. |
| **Operational simulation** | A model of how a process might behave under chosen settings, rather than a field measurement. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why does no buffering deliver zero scans?

**Plain English answer:** In this scenario, every one of the 75 selected arrivals occurs during the modeled outages and there is no place to retain them. That is a deliberate scenario condition.

### Question 2: Why did the ML response deliver 72 while buffering delivered 60?

**Plain English answer:** The ML scenario had assumed alert timing and one scan per minute of protective capacity. That extra modeled processing protects additional records before the buffer overflows.

### Question 3: Does ML itself deliver the extra 12 scans?

**Plain English answer:** No. The model assumes protective processing becomes available after the alert. The benefit is from that action and its timing, not merely from a classifier producing a label.

### Question 4: Why was buffering only limited to 60 scans?

**Plain English answer:** The queue has finite capacity and the disruption arrivals can exceed what it retains. The minute by minute simulation records which scans fit and which are lost.

### Question 5: Why did a false alert lose six normal scans?

**Plain English answer:** The simulated protective response reduced normal processing capacity even though there was no attack, creating a backlog and drops. This illustrates a possible cost of unnecessary alerts under the chosen rules.

### Question 6: Why use 75 normal scans for the false alert trial?

**Plain English answer:** It gives a controlled same-size comparison with the affected scan set. It is not evidence that 75 normal scans would behave this way across airports.

### Question 7: What does the zero protected capacity test tell us?

**Plain English answer:** An alert by itself did not improve delivery. Protective ability and activation timing are necessary for any modeled benefit.

### Question 8: Do the delivery percentages directly confirm H3 in the real world?

**Plain English answer:** No. They show that this specific queue model benefits from timely response and enough capacity. The result is conditional on its assumptions.

### Question 9: How are the different H3 notebooks related?

**Plain English answer:** Notebook 09 tests event retention with probabilistic buffering; 10 checks detection dependence; 11 models faster response; 12 demonstrates minute by minute queue behavior. The same 75 affected scans appear across them, so these are not independent replications.

### Question 10: Which evidence would a committee member likely challenge?

**Plain English answer:** Why the buffer has capacity 6, recovery capacity 2, and the selected response timing. Those choices drive the comparison and were set in the model rather than measured from airline equipment.

## 7. A Natural Way to Explain It Out Loud

> Notebook 12 shows how the modeled baggage scan queue behaves minute by minute during 10 simulated outages. With no buffer, all 75 selected scans are lost. Basic buffering delivers 60, while the assumed ML triggered protective response delivers 72. The same notebook shows a cost: an unnecessary alert on 75 normal scans can cause six modeled losses. These are useful demonstrations of both benefits and tradeoffs, not actual airport performance measurements.

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

**Sentence pattern measure:** 100 longer prose sentences reviewed. Average length approximately 16.1 words; length variation approximately 5.7 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (10); “what a professor may” (10); “what happens and why” (10)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
