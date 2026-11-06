# Notebook 07 Defense README

**H2 CICIoT2023 — Network Attack Classification and Specific Spoofing**

**Paired notebook:** [`07_Praxis_H2_CICIoT2023_Spoofing_Analysis.ipynb`](./07_Praxis_H2_CICIoT2023_Spoofing_Analysis.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

The notebook asks two different questions using public IoT network traffic. First, can the models distinguish broadly labeled attack traffic from benign traffic? Second, can they find specific spoofing categories when the positive class is very rare? Those results should be read separately.

**Research connection:** Supplemental RQ2/H2 work. This notebook uses a public network dataset for broad attack classification and a second, narrower ARP/DNS spoofing task. Neither dataset is real baggage scan activity.

**The one thing to remember:** Explain the two tasks separately: broad attack detection and targeted network spoofing. The scores have different denominators.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Load CICIoT2023

**What happens and why:** Reads 704,067 network flow records and reviews available protocol, packet, and traffic fields.

**What a professor may challenge:** A network flow is not a single RFID reader scan.

### 2.2 Create general attack labels

**What happens and why:** Maps 687,560 entries to attack and 16,507 to normal traffic in the reviewed dataset.

**What a professor may challenge:** The positive class dominates; a high accuracy score can be misleading.

### 2.3 Prepare a train/test split

**What happens and why:** Uses 492,846 training and 211,221 testing records, with network feature scaling where appropriate.

**What a professor may challenge:** The split must keep preprocessing fit on training data. Review whether traffic from similar sources appears in both groups.

### 2.4 Address imbalance

**What happens and why:** Applies class weights in the modeling process.

**What a professor may challenge:** Class weights change the cost of errors. They do not create new observations or guarantee fair predictions.

### 2.5 Train the three algorithms

**What happens and why:** Runs Logistic Regression, SVM, and Random Forest on broad attack labels.

**What a professor may challenge:** The broad attack task is not identical to the spoofing specific hypothesis.

### 2.6 Evaluate general attack classification

**What happens and why:** Reports confusion matrices, accuracy, recall, F1, balanced accuracy, and normal traffic recall.

**What a professor may challenge:** Random Forest reaches 98.37% accuracy and 99.16% F1 in the saved broad attack comparison.

### 2.7 Build a spoofing specific target

**What happens and why:** Uses ARP spoofing and DNS spoofing categories, with 7,167 spoofing records across the full dataset.

**What a professor may challenge:** This is a much rarer class than the general attack label.

### 2.8 Compare spoofing models with a majority baseline

**What happens and why:** Evaluates 211,221 test records, including 2,150 spoofing examples.

**What a professor may challenge:** Random Forest has the highest accuracy among the three trained models here but a non spoofing baseline is even more accurate in aggregate.

### 2.9 Save both result sets

**What happens and why:** Writes model and confusion matrix results without changing the simulated baggage dataset.

**What a professor may challenge:** Keep the two analyses distinguishable in written discussion.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. General network attack task: Random Forest **98.37% accuracy** and **99.16% F1** in the saved output. The attack labels dominate this dataset.
2. Spoofing task: **2,150 real labeled network spoofing records** were present among **211,221 test flow records**.
3. Random Forest spoofing detection: **96.84% accuracy**, **24.38% precision**, **99.95% recall**, with **6,664 false positives** and **1 missed spoofing case**.
4. The simple always non spoofing baseline reached **98.98% accuracy**, while detecting zero spoofing cases.
5. This is supplemental network evidence, not a test on recorded baggage RFID readers.

### One calculation worth remembering

**Network spoofing precision = 2,149 / (2,149 + 6,664) = 24.38%.** The model missed one of 2,150 spoofing test examples.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Do not combine 98.37% general attack accuracy with 96.84% spoofing accuracy as though they are one experiment or one kind of event.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `07_CICIoT2023_H2_Experiment(1).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **CICIoT2023** | A public Internet of Things network traffic dataset used here to evaluate attack classification. |
| **Network flow** | A summarized communication exchange with packet and protocol measurements. |
| **ARP spoofing** | A network technique that misleads device address mappings; not the same as cloning a physical RFID tag. |
| **DNS spoofing** | Providing or redirecting false name resolution information. |
| **Majority baseline** | Always predicting the most frequent class to test whether a sophisticated model adds value. |
| **Balanced accuracy** | Average of recall for both classes, useful when one class is rare. |
| **False alert burden** | The amount of legitimate activity incorrectly flagged, which creates potential operational work. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why are there two different model comparisons?

**Plain English answer:** The first treats many network attack types as positive. The second isolates ARP and DNS spoofing. A score from the first should not be presented as spoofing detection performance.

### Question 2: Can the public network results validate real RFID baggage spoofing?

**Plain English answer:** Not directly. They examine network patterns and are useful supporting cybersecurity context, but they do not reproduce RFID tag and reader conditions in an airport.

### Question 3: Why is 96.84% accuracy not an impressive stand alone spoofing result?

**Plain English answer:** The non spoofing baseline reaches 98.98% because only a small share of rows are spoofing. The model detects nearly all spoofing but creates thousands of false alarms.

### Question 4: How many spoofing events did Random Forest miss?

**Plain English answer:** One among the 2,150 test spoofing records. It also falsely flagged 6,664 non spoofing records, so both numbers belong in the answer.

### Question 5: Does 99.95% recall mean an operational detector is ready?

**Plain English answer:** No. Precision was 24.38%, so a large share of alerts would be wrong. Also, the test represents this network dataset rather than a baggage tracking system.

### Question 6: Why include balanced accuracy and normal recall?

**Plain English answer:** The dataset is unevenly labeled. Those measures reveal whether performance is strong for both attack and normal traffic instead of only for the dominant class.

### Question 7: What is different between network spoofing and reader spoofing?

**Plain English answer:** Network spoofing changes address or name resolution behavior. The simulated RFID spoofing test changes aspects of a reader identity, location, or timestamp. They share a security theme but not the same signals.

### Question 8: Can H2 be called proven from this notebook?

**Plain English answer:** No. It supports an algorithm ranking under the two evaluated network tasks, but the baseline comparison, false alarms, and different data domain require more careful wording.

## 7. A Natural Way to Explain It Out Loud

> Notebook 07 uses public IoT network data to compare the same three models. The first test covers many attack types; the second focuses on ARP and DNS spoofing. Random Forest ranked highest among the trained models in both tests, but the spoofing result still produced 6,664 false alerts. A simple model that always says non spoofing was more accurate overall. That is why the results need precision, recall, and baseline comparisons, not just one accuracy number.

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

**Sentence pattern measure:** 94 longer prose sentences reviewed. Average length approximately 14.9 words; length variation approximately 5.2 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (9); “what a professor may” (9); “what happens and why” (9)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
