# Notebook 02 Defense README

**RFID Data Preparation — How Raw Scans Become Testable Variables**

**Paired notebook:** [`02_Praxis_RFID_Data_Preparation.ipynb`](./02_Praxis_RFID_Data_Preparation.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

The raw records from Notebook 01 must be checked and organized before they can be used. Here the notebook creates comparisons such as actual reader versus expected reader, along with final scan labels that later tests use as the answer key.

**Research connection:** Prepares the inputs and labels for H1, H2, and H3. This is a data preparation step, not a separate hypothesis result.

**The one thing to remember:** Confirm whether a field is a predictor, a known answer, or a calculated comparison. That distinction can decide whether a model test is fair.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Connect the source file

**What happens and why:** Loads the generated RFID scan table and confirms the file is accessible in the research environment.

**What a professor may challenge:** The source must be the approved simulation output rather than an alternate sample.

### 2.2 Check the shape and identity of records

**What happens and why:** Checks 31,575 rows, 5,000 distinct bag journeys, and unique scan identifiers.

**What a professor may challenge:** If any of those counts differ, later H1/H2/H3 denominators may not match.

### 2.3 Prepare reader, location, time, and sequence checks

**What happens and why:** Builds fields that show a reader mismatch, location mismatch, a sequence problem, or timing deviation.

**What a professor may challenge:** A derived comparison flag can directly reveal a simulated attack; later ML models must not train on fields that give away the target.

### 2.4 Create the final scan outcome

**What happens and why:** Labels existing rows normal or abnormal and saves the prepared data with the added fields.

**What a professor may challenge:** The saved output has 30,225 normal scan rows and 1,350 abnormal scan rows. This is not the same as the 1,500 abnormal journeys.

### 2.5 Review the absent scan cases

**What happens and why:** Separately checks missing scan journeys that have no observed row to label.

**What a professor may challenge:** 150 missing scan journeys are found by examining expected versus observed custody paths, not by counting scan rows.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. **31,575 scan records**, **5,000 bag journeys**, and **31,575 unique scan IDs** are retained.
2. The prepared file has **34 fields** in the reviewed output, compared with 26 in the generated data.
3. It identifies **375 reader mismatches**, **225 location mismatches**, **225 sequence mismatches**, **225 delayed scans**, and **375 spoofed scans**.
4. The existing rows are labeled **30,225 normal** and **1,350 abnormal**; **150 missing scan journeys** are checked separately.

### One calculation worth remembering

**30,225 normal rows + 1,350 abnormal rows = 31,575 observed rows.** The 150 missing scan journeys are a separate journey level check.

## 4. Small Details That Can Change the Meaning

**Important limitation:** Treat derived match and mismatch flags carefully. They are useful for rule comparisons but may lead to target leakage if used improperly in machine learning.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `02_Praxis_RFID_Data_Preparation (4).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **Feature engineering** | Turning existing fields into a new measurement that a rule or model can use. |
| **Label** | The known correct answer associated with a record, such as spoofing or non spoofing. |
| **Mismatch flag** | A yes/no indication that observed and expected values differ. |
| **Data integrity** | Checks that the record counts, IDs, and meaning of fields stay consistent after preparation. |
| **Row versus journey** | A row describes one scan; a journey describes a bag’s full trip. |
| **Target leakage** | Using a derived answer or a field built from the known answer as a model input. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why create new columns instead of using the original records unchanged?

**Plain English answer:** The original data describe scans, but later security checks need clear comparisons: expected reader versus observed reader, or expected sequence versus actual sequence. Added columns make those comparisons repeatable.

### Question 2: Why are there 1,350 abnormal scans but 1,500 abnormal journeys?

**Plain English answer:** Missing scan cases remove records. Those missing records cannot be counted as abnormal rows, so the notebook checks missing journeys separately.

### Question 3: Can a high accuracy result be caused by prepared columns?

**Plain English answer:** Yes. If a model receives a field that directly states a mismatch used to create the label, performance may reflect the simulation rule instead of independent prediction. We need to inspect model inputs, not just the score.

### Question 4: Do the 34 fields mean 34 independent signals?

**Plain English answer:** No. Some are IDs, labels, or new measurements created from existing fields. More columns do not mean more independent evidence.

### Question 5: What happens if the preparation is wrong?

**Plain English answer:** Every downstream experiment could inherit incorrect labels or comparisons. That is why counts and spot checks are important before H1, H2, or H3 tests.

### Question 6: Why not delete missing or abnormal data?

**Plain English answer:** Removing them would erase the exact conditions the study intends to detect. Missingness must be understood instead of automatically cleaned away.

### Question 7: Does this notebook prove that Zero Trust works?

**Plain English answer:** No. It produces the inputs needed for the comparison. Notebook 03 runs the actual H1 comparison.

## 7. A Natural Way to Explain It Out Loud

> This notebook prepares the simulated baggage scans for analysis. It checks that the same 5,000 journeys and 31,575 scan rows are still present, then creates fields that help identify suspicious reader, location, timing, and sequence activity. Missing scan journeys are checked separately because they are absent from the scan table.

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

**Sentence pattern measure:** 77 longer prose sentences reviewed. Average length approximately 15.5 words; length variation approximately 5.7 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (5); “what a professor may” (5); “what happens and why” (5)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
