# Notebook 08 Defense README

**H2 Model Robustness — Testing Whether the Good Results Hold Up**

**Paired notebook:** [`08_Praxis_H2_Model_Performance_and_Robustness_Validation.ipynb`](./08_Praxis_H2_Model_Performance_and_Robustness_Validation.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

This is the notebook a professor may question most closely. It does not just repeat the model table. It investigates why Random Forest caught spoofing but generated many wrong alerts, why validation appeared perfect, and what happened when the model faced unfamiliar simulated attack patterns.

**Research connection:** Deep review of RQ2/H2. This notebook checks how class balance, threshold selection, route distribution, and unfamiliar spoofing patterns change the original model ranking.

**The one thing to remember:** This notebook adds honesty to H2. Explain why the initial model ranking is conditional, not a universal finding.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Reconstruct original H2 work

**What happens and why:** Uses the same 31,575 generated scan rows and the same 375 spoofing cases divided into three 125-record patterns.

**What a professor may challenge:** It is a robustness study of the same simulation, not a newly collected sample.

### 2.2 Keep whole baggage journeys together

**What happens and why:** Uses grouped training, validation, and testing, with 13 predictors and target labels excluded.

**What a professor may challenge:** Grouping bags prevents repeated scans for one bag entering both training and testing.

### 2.3 Choose a threshold on training-derived validation

**What happens and why:** Examines Random Forest probability cutoffs without using final testing rows. A threshold of 0.65 was selected in the saved run.

**What a professor may challenge:** A perfect validation score does not guarantee the final testing result will be perfect.

### 2.4 Compare with a majority baseline

**What happens and why:** Reproduces 85.84% Random Forest accuracy and examines 1,489 false alerts.

**What a professor may challenge:** The majority baseline is about 98.94% accurate while missing every spoofing case.

### 2.5 Analyze error patterns

**What happens and why:** Looks at which non spoofing scans were incorrectly flagged and compares train, validation, and test distributions.

**What a professor may challenge:** Other abnormal events are negative for the spoofing-specific target and can confuse the classifier.

### 2.6 Estimate uncertainty by resampling journeys

**What happens and why:** Uses grouped bootstrap intervals rather than resampling unrelated scan rows.

**What a professor may challenge:** The intervals describe variation within the simulation, not a confidence guarantee for airports.

### 2.7 Withhold attack patterns

**What happens and why:** Removes one spoofing pattern during training and then tests whether the classifier recognizes that excluded pattern.

**What a professor may challenge:** This challenge examines controlled novelty and exposes sensitivity to how the generator constructed attacks.

### 2.8 Investigate surprising validation results

**What happens and why:** The selected validation set showed perfect classification while the final test retained many false positives.

**What a professor may challenge:** Do not tune thresholds against the final test after seeing that outcome.

### 2.9 Balance route types in both splits

**What happens and why:** Creates a second grouped split containing direct and transfer bags in training and test groups.

**What a professor may challenge:** The original random seed had produced a route separation that distorted the earlier comparison.

### 2.10 Repeat model and unfamiliar-pattern tests

**What happens and why:** On the route balanced set, SVM and Random Forest can classify familiar generated patterns perfectly, but unfamiliar withheld patterns have zero recall.

**What a professor may challenge:** The combination of perfect seen performance and zero unseen detection is a warning about relying on the generator’s signatures.

### 2.11 Audit direct rule signals

**What happens and why:** Compares reader identity, location, and timing differences and tests a simple identity/location rule.

**What a professor may challenge:** Some patterns are defined by exact mismatches. A rule with direct access to expected identity information can sometimes detect them without ML.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. Original grouped split: Random Forest **85.84% accuracy**, **6.94% precision**, **100% recall**, and **1,489 false positives** on **10,517 test scans**.
2. The non spoofing majority baseline has approximately **98.94% accuracy**, but **0% recall** for spoofing.
3. Route balanced test: **9,469 scan rows**, **116 spoofing records**. Random Forest and SVM reached **100% accuracy and recall** for the familiar patterns in that controlled set.
4. In the route balanced excluded-pattern test, the models had **0% recall on each withheld spoofing pattern** while still detecting most previously seen patterns.
5. A simple reader identity/location check reached approximately **66.38% spoofing recall**, showing why a direct field comparison is worth considering.
6. The fuller evidence gives only **conditional support** to the original Random Forest ranking and shows substantial limits to generalization.

### One calculation worth remembering

**Original test: 111 spoofing records and 10,406 non spoofing records.** The non spoofing baseline is correct on 10,406/10,517 = 98.94%, despite missing every spoofing scan.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Be ready to distinguish **original split**, **route balanced split**, **seen patterns**, and **withheld patterns**. Combining their scores into one headline would misrepresent what was tested.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `12_H2_Model_Performance_and_Robustness_Validation_Final_Review.ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **Robustness** | Whether a result remains meaningful when assumptions, data splits, or test conditions change. |
| **Distribution shift** | When training and testing populations differ, such as direct route bags in one group and transfer bags in another. |
| **Threshold tuning** | Changing the probability cutoff for making a positive prediction; it alters alert volume and missed cases. |
| **Bootstrap interval** | A range estimated by repeatedly sampling units from observed data, here entire baggage journeys. |
| **Unseen pattern** | An attack type deliberately withheld from the training examples. |
| **Generalization** | Performance on conditions not simply memorized from the training data. |
| **Overfitting** | Fitting known patterns so closely that unfamiliar examples are missed. |
| **Confounding** | A difference, such as route type, that could explain part of the observed model result. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why did Random Forest look strong at first but weak under scrutiny?

**Plain English answer:** Its original test caught all spoofing but falsely flagged 1,489 non spoofing records. Class imbalance, route composition, and the exact generated attack patterns made the single accuracy figure incomplete.

### Question 2: How did the route split affect conclusions?

**Plain English answer:** The original training and test partitions had different route types. With both route types represented in both partitions, familiar patterns became much easier to classify. That shows the split changed what was being tested.

### Question 3: Why is perfect route balanced performance not the final answer?

**Plain English answer:** The models performed perfectly on patterns they had seen, but failed to detect patterns intentionally excluded from training. That combination suggests they learned the particular synthetic signatures rather than a broad definition of spoofing.

### Question 4: Why select the Random Forest threshold without test data?

**Plain English answer:** Choosing a cutoff after looking at the test result would give the model an unfair advantage. Threshold 0.65 came from a validation subset of the training journeys.

### Question 5: What does zero recall on unfamiliar attacks mean?

**Plain English answer:** The classifier failed to flag any of that withheld simulated spoofing type. The test does not prove every real unknown attack would be missed, but it demonstrates a real weakness in this experiment.

### Question 6: Why use grouped bootstrap instead of row by row resampling?

**Plain English answer:** Multiple scans from one bag are related. Resampling each row as independent would give a misleading sense of how much information the study has.

### Question 7: Does this notebook reject H2?

**Plain English answer:** It weakens a broad claim that Random Forest is the best spoofing detector. Random Forest topped certain comparisons, but the stronger analysis finds high false alarms and no detection of unfamiliar patterns. The conclusion must be conditional.

### Question 8: How might a simple rule compare with machine learning?

**Plain English answer:** A direct reader identity or location check can catch patterns that were constructed from such mismatches. It does not catch all cases, but it shows why model complexity alone does not guarantee a better detector.

### Question 9: Why did the validation model get 100% but final testing fail?

**Plain English answer:** The validation population and final test were not equally challenging. A perfect score on one subset is not a guarantee across other route conditions or legitimate scan patterns.

### Question 10: Is this independent real world replication?

**Plain English answer:** No. The tests use the same simulated RFID source and adjusted splits or attack selection. They are important sensitivity analyses, not new real airport observations.

## 7. A Natural Way to Explain It Out Loud

> Notebook 08 checks whether the original machine learning results are dependable. The original Random Forest caught all spoofing cases but produced many false alerts. When both bag route types were represented in training and testing, the models handled known synthetic patterns very well. But when each attack type was withheld from training, they missed it completely. So the correct conclusion is that the original ranking was conditional and the models did not generalize well to unfamiliar attack patterns in this simulation.

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

**Sentence pattern measure:** 108 longer prose sentences reviewed. Average length approximately 16.1 words; length variation approximately 5.3 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (11); “what a professor may” (11); “what happens and why” (11)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
