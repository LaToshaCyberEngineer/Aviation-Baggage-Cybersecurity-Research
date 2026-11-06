# Notebook 06 Defense README

**H2 Machine Learning — What the Three Models Really Predicted**

**Paired notebook:** [`06_Praxis_H2_Machine_Learning_Analysis.ipynb`](./06_Praxis_H2_Machine_Learning_Analysis.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

The notebook takes the prepared RFID scans, creates three working spoofing patterns, and trains three classifiers. A classifier tries to label each scan as spoofing or non spoofing. The comparison must use more than accuracy because only a small percentage of rows are spoofed.

**Research connection:** RQ2/H2: Compare Logistic Regression, Support Vector Machine, and Random Forest for identifying simulated spoofed RFID scan activity. The hypothesis predicts Random Forest will have the highest accuracy among these models.

**The one thing to remember:** A model with excellent attack recall can still be impractical when most alerts are false. Be ready to calculate precision in words.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Review the prepared data

**What happens and why:** Loads 31,575 RFID rows with the known labels and checks field types.

**What a professor may challenge:** Do not treat the existing abnormal label as a predictor.

### 2.2 Define spoofing conditions

**What happens and why:** Builds a working copy with unauthorized reader, cloned reader location, and replayed timing cases.

**What a professor may challenge:** These patterns are part of the researcher generated experiment, not independently collected attacker behavior.

### 2.3 Define the two-class outcome

**What happens and why:** Labels 375 scan rows as spoofing and 31,200 as non spoofing. Other anomalies are in the non spoofing class.

**What a professor may challenge:** Non spoofing does not always mean the event is normal.

### 2.4 Prepare 13 model predictors

**What happens and why:** Uses numerical and categorical scan context; encodes categories before training.

**What a professor may challenge:** Fields that directly state the spoofing answer must be kept out.

### 2.5 Split by baggage journey

**What happens and why:** Separates groups of bags so a bag does not appear in both training and testing.

**What a professor may challenge:** The original split produced different route distributions across groups. Notebook 08 later investigates why this matters.

### 2.6 Train three models

**What happens and why:** Fits Logistic Regression, Support Vector Machine, and Random Forest on training data.

**What a professor may challenge:** Each uses the same labeled prediction task; a fair comparison also needs suitable common evaluation measures.

### 2.7 Compare test results

**What happens and why:** Measures accuracy, precision, recall, F1, and confusion matrices using held out scans.

**What a professor may challenge:** A model that flags nearly everything as spoofing can achieve very high recall while generating many false alarms.

### 2.8 Save the model evidence

**What happens and why:** Stores comparison tables and outputs for later H2 review.

**What a professor may challenge:** Saved model output should not be confused with performance on a new independent airport dataset.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. The target contains **375 spoofing rows** and **31,200 non spoofing rows**, so spoofing is only about 1.19% of the scans.
2. Original Random Forest test: **85.84% accuracy**, **6.94% precision**, **100% recall**, **1,489 false positives**.
3. The Random Forest found all **111 spoofing records** in that test, but 1,489 non spoofing records were flagged too.
4. A model that always predicted non spoofing would score approximately **98.94% accuracy** on the same test. This baseline was examined explicitly in Notebook 08.
5. Random Forest ranked first for accuracy **among the three evaluated models in the original split**, but it was not operationally strong by all measures.

### One calculation worth remembering

**Random Forest precision = 111 / (111 + 1,489) = 6.94%.** Its recall = 111 / 111 = 100%. Both must be reported.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Never say Random Forest had 100% accuracy. Its 100% result was recall on spoofing in the original test, not its overall accuracy or precision.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `04_Praxis_H2_Machine_Learning_Analysis (1).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **Logistic Regression** | A classifier that estimates the probability of the two possible labels from a weighted combination of input values. |
| **Support Vector Machine (SVM)** | A classifier that tries to separate classes using a boundary defined by the training data. |
| **Random Forest** | An ensemble of decision trees whose combined predictions determine the final class. |
| **Predictor** | An input field provided to the model before prediction. |
| **Class imbalance** | One target class is much rarer than the other. |
| **Precision** | How many predicted spoofing alerts were correct. |
| **Recall** | How many actual spoofing records were detected. |
| **Grouped split** | Separating whole bag journeys rather than randomly mixing their scans. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why compare these three models?

**Plain English answer:** They offer different ways to classify records: a linear approach, a margin-based approach, and a tree ensemble. Comparing them on the same task tests the proposed model ranking, but it does not mean they are the only available algorithms.

### Question 2: Why can 85.84% accuracy be worse than a simple baseline?

**Plain English answer:** Because nearly every test scan was non spoofing. A model that always predicts non spoofing can achieve about 98.94% accuracy but detect no attacks. This is why accuracy cannot stand alone.

### Question 3: What does 100% recall mean with 6.94% precision?

**Plain English answer:** All 111 true spoofing records in that test were caught, but most alerts were wrong. That false alert burden could cause substantial unnecessary review in practice.

### Question 4: Why are other abnormal scans treated as non spoofing?

**Plain English answer:** The H2 target is spoofing specifically. Delayed or out of sequence events may be abnormal, but the model should not automatically call them spoofing.

### Question 5: Did the train/test split prevent leakage?

**Plain English answer:** Grouping by bag kept one journey’s records together, which helps. It did not prevent a route distribution issue: the original seed and split produced different route types between populations, which Notebook 08 examined.

### Question 6: What is target leakage in this setup?

**Plain English answer:** A feature such as a direct spoofing label or a comparison field that exactly encodes the injected condition could reveal the answer. Those need to be excluded or evaluated separately.

### Question 7: Does H2 receive full support?

**Plain English answer:** Only a limited ranking claim holds for this original three model comparison. The poor precision, high false positive count, and later robustness findings weaken broader claims that Random Forest is the best detector.

### Question 8: What should a deployment decision consider?

**Plain English answer:** False alarms, missed attacks, behavior on unfamiliar patterns, and the cost of interrupting legitimate scans, not just which model tops one table.

## 7. A Natural Way to Explain It Out Loud

> Notebook 06 trains three models to identify spoofing among simulated baggage scans. Random Forest had the highest accuracy among the three in the original comparison and caught every spoofing case in the test. However, precision was only 6.94%, because it also flagged 1,489 non spoofing scans. That means the result is mixed. It supports the model ranking in that one experiment, but it does not show a ready to deploy detector.

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

**Sentence pattern measure:** 94 longer prose sentences reviewed. Average length approximately 15.2 words; length variation approximately 5.5 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (8); “what a professor may” (8); “what happens and why” (8)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
