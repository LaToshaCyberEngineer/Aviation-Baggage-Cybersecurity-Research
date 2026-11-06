# Notebook 01 Defense README

**RFID Data Generation — Understanding Where the Research Data Came From**

**Paired notebook:** [`01_Praxis_RFID_Data_Generation.ipynb`](./01_Praxis_RFID_Data_Generation.ipynb)

**Guide type:** Personal working notes for reviewing the research and answering committee questions. These notes do not change or rerun the notebook.

> **Source note:** Prepared from an earlier saved copy of this notebook supplied during the research work. The notebook was later renamed and its internal title was updated in Codespaces. Before using an exact number or a code-specific answer at the defense, compare it with the latest committed notebook output.

## 1. What Is This Notebook Really Doing?

The notebook builds a pretend but organized baggage tracking environment. Each bag gets an identity, a route, several reader scans, and a known normal or abnormal condition. Later notebooks need these known answers to measure whether detection and response methods work.

**Research connection:** Research foundation for RQ1, RQ2, and RQ3. It creates the researcher generated baggage records used later; it does not test the hypotheses on its own.

**The one thing to remember:** The counts are design values. Explain how the number of journeys expands into scan records before discussing performance.

## 2. Walkthrough of the Actual Analysis

These steps follow the work shown in the saved notebook. Read the **what**, **why**, and **watch for** notes together.

### 2.1 Set the environment and random seed

**What happens and why:** Loads Python libraries, mounts the original Google Drive workspace, and sets NumPy random seed 42. The seed helps reproduce the selection of bags and attack assignments. It does not make synthetic data representative of a real airport.

**What a professor may challenge:** A later run must use the same code, package behavior, and input sequence. The saved source copy used Google Colab; the present project uses Codespaces.

### 2.2 Define direct and transfer custody routes

**What happens and why:** Direct bags visit six points: Acceptance, Screening, Sorting, Loading, Arrival, and Claim. Transfer bags add a Transfer point between Loading and Arrival. Reader IDs and expected order are explicitly defined.

**What a professor may challenge:** A missing Transfer scan is not automatically abnormal for a direct route. Expected path must be determined from route type.

### 2.3 Generate 5,000 bag journeys

**What happens and why:** Assigns 3,500 direct and 1,500 transfer journeys; 3,500 normal and 1,500 abnormal journeys. A bag ID follows a journey, while a scan ID follows one reader event.

**What a professor may challenge:** A bag may contribute six or seven scan records. Journeys and scan records are different denominators.

### 2.4 Build normal scan rows

**What happens and why:** Creates one record per expected custody point with expected and observed sequencing initially equal. Before injecting abnormal conditions, the generated table has 31,500 scans.

**What a professor may challenge:** 31,500 = 3,500 × 6 + 1,500 × 7. This is a useful defense calculation.

### 2.5 Inject abnormal activity

**What happens and why:** Assigns 375 spoofed reader journeys; 225 each of duplicate, invalid location, out of sequence, and delayed conditions; 150 missing scan journeys; and 75 DoS journeys. It then changes or removes scan records to represent these problems.

**What a professor may challenge:** The counts and changes were set by the simulation. A favorable detection result may partly reflect how obvious the abnormal patterns were made.

### 2.6 Define DoS windows and save

**What happens and why:** Creates 10 simulated DoS disruption windows across 75 affected scans. The final dataset contains 31,575 recorded scans with 31,575 unique scan IDs.

**What a professor may challenge:** 225 duplicate scan rows were added and 150 missing scan rows removed: 31,500 + 225 − 150 = 31,575. Do not confuse this with 1,500 abnormal journeys.

## 3. Findings to Explain, Not Just Memorize

The figures below are taken from the saved output reviewed for this guide. They describe those runs and should not be generalized beyond them.

1. 5,000 simulated baggage journeys: **3,500 direct** and **1,500 transfer**.
2. 3,500 journeys were assigned normal status and 1,500 were assigned an abnormal condition.
3. The saved scan table contains **31,575 rows**. One journey can have multiple scans, and a missing scan has no row to classify.
4. The abnormal event design includes **375 spoofed reader**, **225 duplicate**, **225 invalid location**, **225 out of sequence**, **225 delayed**, **150 missing scan**, and **75 DoS** journeys.
5. The notebook establishes controlled input data. **It does not establish that a real airport has these attack rates.**

### One calculation worth remembering

**31,500 original scan events + 225 inserted duplicates − 150 removed scans = 31,575 saved rows.**

## 4. Small Details That Can Change the Meaning

**Important limitation:** Do not claim that 30% of real baggage journeys are abnormal or that the generated DoS windows resemble measured airport incidents. These are designed test settings.

**Source trace:** The findings above were checked against the saved outputs and code in the earlier source notebook: `01_Simulated_RFID_Data (1)(5).ipynb`. No external paper or public dataset documentation was treated as evidence for an unverified finding in this guide.

## 5. Difficult Terms in Plain English

| Term | Simple meaning |
|---|---|
| **RFID scan** | A recorded event showing that a tag was read at a specific place and time; not the same as an entire bag journey. |
| **Custody point** | A location where the baggage record is updated, such as Sorting or Loading. |
| **Ground truth** | The known normal or abnormal answer created by the simulation, used later to score detection. |
| **Random seed** | A fixed starting value that makes random selections repeatable under the same conditions. |
| **Synthetic data** | Researcher generated records that mimic useful features of a process but are not direct observations of real baggage operations. |
| **Denial of service (DoS)** | A simulated interruption that prevents or delays scan information from reaching the tracking system. |
| **Data leakage** | When information that gives away the answer reaches the detector or model before its prediction is evaluated. |

## 6. Professor Questions and Suggested Answers

These are study prompts, not rehearsed claims to repeat without understanding. Explain the numbers and the limits in your own words.

### Question 1: Why was simulation used instead of an airline dataset?

**Plain English answer:** The experiment needed a labeled set of baggage events with known custody paths and known anomalies. These were generated so detection methods could be compared under controlled conditions. The tradeoff is limited real world generalization.

### Question 2: Why 5,000 bags, and why a 70/30 route split?

**Plain English answer:** Those were chosen simulation settings, not measured airport traffic proportions. They create enough direct and transfer journeys for controlled comparisons. The research should not present the proportions as industry averages.

### Question 3: How can 5,000 journeys produce 31,575 scan records?

**Plain English answer:** Each direct route has six expected scans and each transfer route has seven. The starting 31,500 rows increase by 225 injected duplicate rows and decrease by 150 missing scan rows, leaving 31,575.

### Question 4: Why does a missing scan not appear as an abnormal row?

**Plain English answer:** The abnormal event is the absence of an expected record. It must be found by comparing a bag’s observed custody path with its expected path, not by labeling an already existing missing row.

### Question 5: Could the models learn the artificial attack rules?

**Plain English answer:** Yes. Since the attacks were deliberately injected, some identifying signals may be especially clean. Later robustness checks must test whether models are responding to the pattern design rather than learning a broader concept of spoofing.

### Question 6: Does the random seed make these results valid?

**Plain English answer:** It makes the experiment easier to reproduce. Validity also depends on realistic assumptions, fair splits, appropriate metrics, and whether findings hold beyond this generator.

### Question 7: How do the 75 DoS cases support H3?

**Plain English answer:** They provide a fixed affected population for later recovery and buffering scenarios. They do not prove the simulated outage was detected automatically.

### Question 8: What is the biggest limitation of this notebook?

**Plain English answer:** It controls the answers and the attack patterns. Results can test the internal logic of a proposed design, but cannot by themselves demonstrate airport performance.

## 7. A Natural Way to Explain It Out Loud

> The first notebook creates a controlled set of baggage movements. There are 5,000 simulated journeys, with direct and transfer paths, and the code adds several kinds of abnormal activity. The output gives the later experiments a known answer for every event that exists in the table. It is not airline data. Its value is that the same simulated conditions can be used to compare different security methods.

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

**Sentence pattern measure:** 101 longer prose sentences reviewed. Average length approximately 14.8 words; length variation approximately 5.8 words (standard deviation). This helps spot very uniform sentence rhythm but does not establish authorship.

**Repeated anchor phrases:** No occurrences of the six common filler phrases checked.

**Repeated four word spans:** “a professor may challenge” (6); “what a professor may” (6); “what happens and why” (6)

**Source alignment:** Numerical findings were drawn from the referenced saved notebook output. No outside sources were added merely to make the guide sound academic. If an external standard or study is later used to support a claim, add a verified source next to that claim.

**Writing consistency review:** Questions use direct language and notebook specific examples. Technical terms are defined near the defense answers. Repeated formatting is intentional for fast studying; repeated generic explanations should be trimmed if found during the final current-version comparison.

**Assessment:** Source linked working guide, with a **version comparison still required** against the latest Codespaces notebook. No AI detection or originality score is claimed.
