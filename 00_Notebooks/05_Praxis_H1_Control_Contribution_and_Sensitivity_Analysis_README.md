1. What is Notebook 05 doing?
Notebook 05 tests how individual Zero Trust checks contribute to anomaly detection and how their performance changes when security thresholds or simulated normal operating conditions change. It extends the H1 experiments in Notebooks 03 and 04 instead of introducing a new dataset.

2. Which research question and hypothesis does it address?
It addresses RQ1: How can Zero Trust improve anomaly detection in RFID baggage tracking systems? H1 proposes that Zero Trust validation improves anomaly detection compared with traditional rules.

3. What data does the notebook use?
It uses the prepared simulated RFID baggage scan file, 06_Prepared_Data/02_Prepared_RFID_Data.csv. The file contains 31,575 scan records covering 5,000 baggage journeys, including 30,225 normal records and 1,350 abnormal records.

4. Is Notebook 05 an independent validation experiment?
No. All tests reuse the same prepared simulated RFID dataset. Notebook 05 evaluates the behavior of the existing security rules under controlled changes, not their performance in an operating airport or on a new dataset.

5. How was the original data protected?
The notebook reads the CSV and creates working copies for its experiments. It records the source file's SHA256 fingerprint and saves results in a separate timestamped folder without modifying the source data.

6. What was reproduced before the new tests?
Traditional rules detected 825 of 1,350 abnormal scans, giving 61.11% recall. The full Zero Trust checks detected 1,275, giving 94.44% recall. This reproduces the original H1 comparison from Notebook 03.

7. What is recall, and why does it matter here?
Recall is the share of abnormal scans correctly flagged. Higher recall means fewer abnormal scans are missed. Notebook 05 measures whether recall decreases when a control is removed or its settings change.

8. Which six Zero Trust checks were examined?
The checks verify required scan information, authorized reader identity, location matching, custody sequence, expected timing, and possible duplicate scans. A scan is flagged when it fails at least one active check.

9. How was each control's contribution tested?
The notebook removed one check at a time while leaving the other five active. It then recalculated true positives, false negatives, false positives, and recall. This is a one-control-at-a-time removal test, not a test of every possible control combination.

10. Which control had the greatest measured contribution?
Removing the authorized reader check reduced detected abnormal scans from 1,275 to 900, a loss of 375 detections. Removing location, custody sequence, timing, or duplicate checks individually reduced detection to 1,050, a loss of 225 detections each. Removing the required information check caused no change in this dataset.

11. Does a zero contribution mean a security check is unnecessary?
No. It means removing that check did not change detection in this particular simulated dataset while the other checks remained active. It does not prove the check is unnecessary in a real system or under other conditions.

12. What thresholds were tested?
The timing thresholds were 5, 10, 15, 20, 25, and 30 minutes. Duplicate scan thresholds were 0, 0.5, 1, 2, and 5 minutes. The original settings were a 15-minute timing limit and a 1-minute duplicate limit.

13. What happened when the timing threshold changed?
With limits of 5, 10, or 15 minutes, recall stayed at 94.44%. At 20, 25, or 30 minutes, recall fell to 77.78%, with 300 abnormal scans missed instead of 75. These results reflect the timing values in the simulated records.

14. What happened when the duplicate threshold changed?
A zero-minute duplicate threshold reduced recall to 77.78%. Thresholds of 0.5, 1, 2, or 5 minutes preserved the original 94.44% recall in the tested dataset. These results do not show how the rule would behave for every possible duplicate interval.

15. How were legitimate operating variations tested?
The notebook selected 300 originally normal scans from different baggage journeys using a fixed random seed. In separate working copies, it shifted their expected timestamps earlier by 5, 10, 20, or 25 minutes. The scans were assumed to remain legitimate for this stress test; no new real-world scan data were collected.

16. What did the legitimate variation test show?
Offsets of 5 and 10 minutes produced no false alerts among the 300 sampled scans. Offsets of 20 and 25 minutes flagged all 300 sampled scans. These are hypothetical false alerts under the explicit assumption that the changed schedules still represent legitimate activity.

17. Did the original Zero Trust checks detect every abnormal scan?
No. They missed 75 abnormal records labeled Denial of Service at the scan level. Missing-scan effects were also evaluated at the baggage journey level in Notebook 03, so scan-level results should not be presented as a complete measure of denial-of-service impact.

18. What conclusions and limitations should be reported?
The six-check Zero Trust approach improved recall by 33.33 percentage points over traditional rules in the original simulated RFID data. Individual control removal and threshold tests show that this improvement depends on the chosen checks and settings. The legitimate variation test exposes a possible false-alert tradeoff. The results support a controlled simulation finding, not independent field validation or guaranteed airport performance.

19. What files were saved for reproducibility?
Step 7 reports eight outputs in a timestamped folder under 07_H1_Results: H1_NB05_All_Scenario_Metrics.csv, H1_NB05_Baseline_Comparison.csv, H1_NB05_Control_Contribution.csv, H1_NB05_Experiment_Manifest.json, H1_NB05_Legitimate_Variation_Test.csv, H1_NB05_Missed_Scan_Conditions.csv, H1_NB05_Threshold_Sensitivity.csv, and H1_NB05_Variation_Scan_Audit.csv. The manifest records source, settings, and test assumptions.
