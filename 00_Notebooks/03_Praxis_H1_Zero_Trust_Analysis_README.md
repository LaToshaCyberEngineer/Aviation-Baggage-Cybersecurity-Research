# Notebook 03 Defense README

**H1 Zero Trust Analysis — Comparing Traditional Rules with Additional Validation**

**Paired notebook:** [`03_Praxis_H1_Zero_Trust_Analysis.ipynb`](./03_Praxis_H1_Zero_Trust_Analysis.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

The same prepared RFID records are screened two ways. The first method uses basic checks; the second adds more checks of who sent the scan and whether its behavior fits the expected baggage journey. The notebook then compares both decisions with the known simulated labels.

**Research connection:** RQ1: How can Zero Trust improve anomaly detection in RFID baggage tracking systems? H1 compares a traditional rule review with additional Zero Trust validation.

**The one thing to remember:** The strongest H1 point is the drop in missed abnormal rows. Its biggest weakness is that the generator and rules use matching definitions.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Load the prepared scans

**What happens and why:** Connects the prepared dataset and reviews its fields and class counts.

**What a professor may challenge:** There are 31,575 scan rows, including 1,350 abnormal rows.

### 2.2 Run traditional checks

**What happens and why:** Uses required scan information, known reader identity, location, and custody sequence to identify suspect records.

**What a professor may challenge:** Traditional rules flag 825 records. This is a rule implementation in the notebook, not a measured airport control.

### 2.3 Run the Zero Trust checks

**What happens and why:** Adds reader authorization, timing consistency, and duplicate scan review to the decision.

**What a professor may challenge:** Zero Trust flags 1,275 records. The extra checks are where the controlled detection improvement comes from.

### 2.4 Compare with actual labels

**What happens and why:** Creates confusion matrices and calculates accuracy, precision, recall, and F1 for both methods.

**What a professor may challenge:** Ask what changed in the confusion matrix, not just which percentage is larger.

### 2.5 Check incomplete baggage journeys

**What happens and why:** Separately identifies the 150 missing scan journeys.

**What a professor may challenge:** This path completeness result is a different unit of analysis from scan row classification.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. Traditional rules: **825 true positives, 525 false negatives, 0 false positives**, and **61.11% recall** on abnormal scan rows.
2. Zero Trust checks: **1,275 true positives, 75 false negatives, 0 false positives**, and **94.44% recall** on the same labeled scan rows.
3. Accuracy increased from **98.34%** to **99.76%**; F1 increased from **0.7586** to **0.9714**.
4. A separate journey completeness check flagged **150 of 150 simulated missing scan journeys** in this controlled dataset.
5. These results support improvement under the *implemented simulated rules*. They do not establish universal zero false alarm performance in live operations.

### One calculation worth remembering

**Traditional recall = 825 / 1,350 = 61.11%. Zero Trust recall = 1,275 / 1,350 = 94.44%.** Improvement = 33.33 percentage points.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Do not say Zero Trust eliminated false positives across airport environments. Zero false positives occurred only on the labeled simulated rows examined here.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `03_Praxis_H1_Zero_Trust_Analysis (3).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **Zero Trust Architecture** | A security approach that checks every access or activity decision rather than assuming an event is trustworthy because it is already inside a system. |
| **True positive** | An abnormal scan correctly flagged. |
| **False negative** | An abnormal scan that the method accepted or missed. |
| **False positive** | A normal scan incorrectly flagged as suspicious. |
| **Recall** | Of all truly abnormal scans, the portion successfully caught. |
| **Precision** | Of all scans flagged, the portion truly abnormal. |
| **F1 score** | A summary combining precision and recall, useful when one alone is misleading. |
| **Confusion matrix** | A four-part count of correct and incorrect predictions for normal and abnormal records. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why did recall increase by 33.33 percentage points?

**Plain English answer:** The additional timing and duplicate checks flagged abnormal patterns missed by the traditional rule set. The change is calculated as 94.44% minus 61.11%. It should be described as a difference in this experiment, not a guaranteed industry improvement.

### Question 2: Why were both precision scores 100%?

**Plain English answer:** No normal rows were flagged in this designed sample. Because the simulation labels and detection conditions are clear, this does not prove the methods would have no false alarms on live baggage traffic.

### Question 3: What is the difference between recall and accuracy here?

**Plain English answer:** Accuracy is dominated by the many normal rows. Recall focuses on catching the smaller abnormal group. Higher overall accuracy can conceal a large number of missed attacks.

### Question 4: Why did the traditional rules miss 525 abnormal scans?

**Plain English answer:** Those abnormal events were not captured by the traditional checks as implemented, including patterns addressed by the extra Zero Trust checks.

### Question 5: Were these truly independent security controls?

**Plain English answer:** The rules were simulated decision logic applied to the same prepared records. There was no independently deployed airport Zero Trust system in this experiment.

### Question 6: Why was missing scan detection tested separately?

**Plain English answer:** A missing event has no record to classify. The notebook reconstructs expected custody paths at the journey level, which is different from labeling existing scans.

### Question 7: Could the security logic have been tailored to the injected attacks?

**Plain English answer:** Yes. The controls and anomaly generator use related definitions. This is a key internal validity concern and a reason to keep claims limited to the controlled simulation.

### Question 8: What would strengthen H1 further?

**Plain English answer:** Changing thresholds, testing unseen patterns and more realistic noise, and assessing false alarm costs could show whether the improvement survives conditions beyond the original generator.

## 7. A Natural Way to Explain It Out Loud

> Notebook 03 uses the same prepared records to compare traditional rule checks against additional Zero Trust checks. The traditional method caught 825 of 1,350 abnormal scan rows. The Zero Trust version caught 1,275. That raises recall from 61.11% to 94.44% in the controlled simulation. The result supports the value of additional verification in this design, while the synthetic conditions limit claims about real airport use.

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

**Sentence pattern measure:** 88 longer prose sentences reviewed. Average length approximately 14.4 words; length variation approximately 5.7 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (5); “what a professor may” (5); “what happens and why” (5)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
