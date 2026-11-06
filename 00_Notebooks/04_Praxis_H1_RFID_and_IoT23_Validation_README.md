# Notebook 04 Defense README

**H1 RFID and IoT23 Validation — Separating Baggage Tests from Network Traffic**

**Paired notebook:** [`04_Praxis_H1_RFID_and_IoT23_Validation.ipynb`](./04_Praxis_H1_RFID_and_IoT23_Validation.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

This notebook extends the H1 comparison without claiming that the public network dataset contains airline baggage scans. It tests a held out group of simulated baggage journeys, then studies network connection activity in IoT23 on its own terms.

**Research connection:** Supplemental evidence for RQ1/H1. The RFID validation subset repeats the traditional versus Zero Trust comparison; the IoT23 network activity analysis is separate cybersecurity context.

**The one thing to remember:** Say clearly which evidence is from simulated RFID data and which is from public network traffic. Do not call them a merged operational dataset.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Connect both datasets

**What happens and why:** Loads prepared RFID scans and IoT23 network records and reviews each dataset’s columns and labels.

**What a professor may challenge:** The outputs show 31,575 RFID rows and 23,145 IoT23 network rows. They are different kinds of records.

### 2.2 Review conditions and missing measurements

**What happens and why:** Lists RFID scan abnormalities alongside IoT23 network categories.

**What a professor may challenge:** Network labels such as malicious activity cannot be relabeled as baggage mishandling.

### 2.3 Select an RFID validation population

**What happens and why:** Holds out full baggage journeys; the displayed sample has 1,250 journeys and 8,764 scan rows.

**What a professor may challenge:** Keeping a bag’s scans together avoids counting the same journey across the comparison groups.

### 2.4 Apply both RFID screening methods

**What happens and why:** Uses traditional reader, location, and sequence checks, then the fuller Zero Trust checks.

**What a professor may challenge:** Both methods must be scored on the exact same held out scans.

### 2.5 Compare RFID validation results

**What happens and why:** Calculates confusion matrices and performance measures with the known labels.

**What a professor may challenge:** This is additional assessment of the same simulated generator, not an independent real airport dataset.

### 2.6 Evaluate IoT23 connection activity

**What happens and why:** Counts connections by source over one-minute windows and flags sources crossing a chosen activity threshold.

**What a professor may challenge:** The network alerts are compared with IoT23 labels separately. A connection rate alert is not automatically a verified cyberattack.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. The RFID validation sample contains **8,764 scan rows** from **1,250 bag journeys**.
2. IoT23 contains **23,145 network records** in the saved run, with **21,222 malicious** and **1,923 benign** labels.
3. The IoT23 alert rule flagged **14,574 network records** in the recorded output. Its performance must be interpreted against the actual IoT23 labels, not against RFID scan labels.
4. The two analyses demonstrate separate forms of security checking. They are **not a combined or matched airport and network dataset**.

### One calculation worth remembering

**23,145 IoT23 network rows** and **8,764 sampled RFID rows** have different meanings. Do not add them together to create a baggage detection sample.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Be exact about what “validation” means: same generator held out RFID sample, plus separate IoT23 network analysis. Neither is a live airline field test.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `06_IoT23_H1_Zero_Trust_Experiment.ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **IoT23** | A public dataset of network traffic from Internet of Things settings, not a record of airline baggage movements. |
| **Holdout sample** | A portion set aside to examine performance without reusing the exact same journeys from training or setup. |
| **Connection window** | A time interval during which network connections are counted. |
| **Threshold** | The cutoff at which a rule decides activity is suspicious. |
| **Class imbalance** | One category, such as malicious traffic, occurs much more often than another. |
| **External validity** | How far results from one controlled setting can reasonably apply to other settings. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why include IoT23 if it is not airport data?

**Plain English answer:** It provides a separate public network security example. The baggage experiment tests RFID custody logic; IoT23 tests connection activity. The notebook keeps those findings separate instead of claiming they measure the same events.

### Question 2: Was IoT23 joined to individual baggage records?

**Plain English answer:** No. The reviewed notebook treats the datasets separately. There is no real one to one link between an IoT23 source address and a simulated baggage tag.

### Question 3: Does the held out RFID set count as independent validation?

**Plain English answer:** It is held out from the same simulated baggage generator, so it reduces some reuse within the analysis but is not independent real world validation.

### Question 4: Why use one-minute windows?

**Plain English answer:** The rule needs a fixed period for measuring activity rate. That is an implementation choice; different windows can change false alarms and detection.

### Question 5: Can a connection count prove malicious intent?

**Plain English answer:** No. High activity can be legitimate. Performance needs to be tested against labeled cases, and the threshold may behave differently in another network.

### Question 6: Are the IoT23 labels balanced?

**Plain English answer:** No. The saved run has far more malicious than benign entries. Accuracy alone can hide weak performance on the smaller class.

### Question 7: What does this add to H1?

**Plain English answer:** It provides an additional RFID sample and a separate illustration of network security screening. It does not independently establish that Zero Trust protects a live aviation system.

## 7. A Natural Way to Explain It Out Loud

> Notebook 04 has two related but different analyses. It repeats the RFID screening comparison on a held out group of simulated baggage journeys. It also examines a public IoT network dataset by measuring connection activity. Those network records are not baggage scans, so their results are kept separate. The notebook adds context and a second look at H1 without presenting the two datasets as a single real airport experiment.

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

**Sentence pattern measure:** 83 longer prose sentences reviewed. Average length approximately 14.8 words; length variation approximately 5.5 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (6); “what a professor may” (6); “what happens and why” (6)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
