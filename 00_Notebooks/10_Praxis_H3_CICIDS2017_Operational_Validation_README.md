# Notebook 10 Defense README

**H3 CICIDS2017 — Testing Whether Analytics Adds More Than Buffering**

**Paired notebook:** [`10_Praxis_H3_CICIDS2017_Operational_Validation.ipynb`](./10_Praxis_H3_CICIDS2017_Operational_Validation.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

This notebook adds a public DDoS network dataset to H3. It trains a detector and then explores what would happen if simulated RFID recovery required a network alert. The important question is whether analytics improves on ordinary buffering after accounting for missed attacks and false alerts.

**Research connection:** Supplemental RQ3/H3 evaluation that separates network attack detection accuracy from the assumed effect of triggering RFID scan recovery.

**The one thing to remember:** Detection measured on public network flows cannot be treated as confirmed detection of simulated baggage disruptions.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Load RFID disruption cases

**What happens and why:** Confirms the same 75 affected scan records across 10 simulated DoS events.

**What a professor may challenge:** Do not count the same cases as a new independent airport experiment.

### 2.2 Load CICIDS2017

**What happens and why:** Reads 225,745 network traffic records with 128,027 DDoS and 97,718 benign labels.

**What a professor may challenge:** These are not baggage reader records, and an attack label in CICIDS2017 is not a bag’s disruption ID.

### 2.3 Train and score network detection

**What happens and why:** Uses 158,021 training and 67,724 testing records; reports accuracy, balanced accuracy, precision, recall, F1, and confusion matrix.

**What a professor may challenge:** The saved detector had 66.21% DDoS recall and a 36.63% false positive rate. Those costs matter.

### 2.4 Set three RFID response scenarios

**What happens and why:** Models no mitigation, automatic store and forward, and analytics triggered restoration.

**What a professor may challenge:** The single analytics triggered run assumed 9 of 10 disruption groups were detected; that 90% rate exceeds measured detector recall.

### 2.5 Compare modeled restoration

**What happens and why:** Automatic buffering restores 64 scans. Analytics triggered recovery restores 57 in the single simulated trial.

**What a professor may challenge:** A detector that misses events can prevent the response from being activated, reducing restoration.

### 2.6 Measure timing and staleness

**What happens and why:** Examines delays for restored records while leaving permanently unavailable cases without finite recovery delay.

**What a professor may challenge:** Recovery timing cannot be compared fairly if lost records are given arbitrary numbers.

### 2.7 Test detection sensitivity

**What happens and why:** Uses the observed 66.21% network recall as a separate detection assumption.

**What a professor may challenge:** Expected analytics restoration falls to about 42.37 scans, or 56.50% of the 75 affected population.

### 2.8 Save evidence and conclusion

**What happens and why:** Writes comparison, sensitivity, timing, and conclusion outputs.

**What a professor may challenge:** The notebook explicitly does not confirm an added benefit from analytics beyond buffering in this setup.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. CICIDS2017 network detection: **64.98% accuracy**, **66.21% DDoS recall**, **70.31% precision**, and **36.63% false positive rate**.
2. The network detector made **10,739 false positive predictions** among **29,316 benign test rows**.
3. Automatic store and forward recovered **64 / 75** RFID scans (**85.33%**).
4. The single analytics triggered scenario restored **57 / 75** (**76.00%**) using a **90% simulated disruption detection assumption**.
5. A sensitivity calculation using measured **66.21%** recall estimated **42.37 restored scans**, an expected recovery rate of **56.50%**.
6. The saved conclusion states that **H3 was not independently confirmed as an added benefit of analytics** in this test.

### One calculation worth remembering

**Single trial: 57 / 75 = 76%.** A separate sensitivity calculation estimates 42.37 / 75 ≈ 56.50%, not 42.37 observed events.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Never describe the calculated 56.50% recovery estimate as an observed run or present CICIDS2017 records as matching RFID scanner events.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `09_H3_CICIDS2017_Operational_Validation (1).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **CICIDS2017** | A public network intrusion dataset used here for DDoS versus benign detection. |
| **DDoS** | Distributed denial of service: traffic from multiple sources intended to overwhelm a service. |
| **Detection recall** | The share of real labeled DDoS records a classifier identifies. |
| **False positive rate** | Among truly benign records, the portion incorrectly labeled as attacks. |
| **Sensitivity calculation** | Testing how a modeled outcome changes when an uncertain assumption changes. |
| **Triggered recovery** | A modeled response that activates only after a detection alert. |
| **Expected value** | A calculated average under a probability assumption, not the outcome of an actual run. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why did analytics triggered recovery restore fewer scans than buffering alone?

**Plain English answer:** Analytics required an alert first. Missed disruptions could therefore stop recovery from being triggered even though buffering alone could preserve those scans.

### Question 2: Why report both 90% and 66.21% detection rates?

**Plain English answer:** The 90% rate is what was assigned to the single RFID response simulation. The 66.21% is measured recall on held out CICIDS2017 network records. The sensitivity analysis shows the consequence of using the measured result.

### Question 3: Are the network detection results and baggage recovery results directly linked by real observations?

**Plain English answer:** No. They come from separate datasets. The notebook connects them through a modeled assumption and clearly should describe that as a simulation.

### Question 4: What does the 36.63% false positive rate imply?

**Plain English answer:** A large share of benign network traffic would produce alarms in that test. Unnecessary protective actions could have costs, which later operational simulations examine.

### Question 5: Does a 76% recovery rate support the original H3 claim?

**Plain English answer:** Not as independent added value from analytics. Automatic buffering restored 85.33% in the same framework, so the analytics trigger did not outperform it.

### Question 6: Why compare to an always attack baseline?

**Plain English answer:** When labels are imbalanced, even a trivial rule can look good on some metrics. The notebook reports baseline measures to show whether the classifier adds value.

### Question 7: What is the difference between 42.37 and 57 restored scans?

**Plain English answer:** 57 is the outcome of the selected single simulation. 42.37 is a calculated expectation under an alternative recall assumption. It is not a fractional observed scan.

### Question 8: What is the defensible conclusion?

**Plain English answer:** Buffering improved continuity in the simulation. The extra analytics detection step was not shown to improve recovery compared with buffering alone.

## 7. A Natural Way to Explain It Out Loud

> Notebook 10 tests the part of H3 that asks whether cybersecurity analytics adds value beyond buffering. It measures a DDoS detector on CICIDS2017 network traffic and then uses modeled alerts to trigger recovery of simulated baggage scans. The detector caught about 66% of DDoS traffic and produced many false alarms. The triggered scenario restored fewer scans than buffering alone. The results therefore do not independently confirm an analytics advantage, even though the continuity control itself helped.

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

**Sentence pattern measure:** 90 longer prose sentences reviewed. Average length approximately 15.3 words; length variation approximately 4.9 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (8); “what a professor may” (8); “what happens and why” (8)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
