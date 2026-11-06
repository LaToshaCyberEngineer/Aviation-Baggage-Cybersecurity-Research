1. What is Notebook 11 trying to understand?
It asks whether an alert can trigger a useful response soon enough to reduce disruption. That goes a step beyond counting how many scans were buffered.

2. What is the difference between a traditional rule and machine learning here?
The traditional rule checks network activity against a fixed condition. The machine learning model uses several traffic features to make its classification. Both are evaluated on public network data.

3. What were the traditional rule results?
The saved run shows 41.14% accuracy, 0.04% attack recall, and a 5.02% false-positive rate. The rule missed almost all attack rows under the conditions used.

4. What were the machine learning results?
The saved comparison shows 64.98% accuracy, 66.21% attack recall, and a 36.63% false-positive rate. It found many more attacks but also flagged many more benign rows.

5. What is the tradeoff between the two methods?
The simple rule stayed quiet more often but missed nearly every attack. Machine learning caught more attack traffic but produced more false alarms. Which is better depends on the cost of missed alerts and unnecessary response.

6. Why is a false alert important in a baggage tracking process?
If a false alert starts a protective action, normal scan processing might be slowed down or interrupted. The response needs to help more than it hurts.

7. What are the four recovery conditions?
The notebook compares no mitigation, automatic buffering, traditional rule response, and machine learning response. These are modeled conditions, not four live airport systems.

8. How many scans were restored in the buffering conditions?
Each of the three buffering conditions restored 64 of the 75 affected scans in this saved test. The no-mitigation condition restored zero.

9. If recovery stayed at 64 scans, what improved with machine learning?
The modeled disruption time got shorter in the selected response setting. That is a timing result, not an increase in the number of scans restored.

10. How much shorter was the modeled disruption?
The average changed from 20.7 minutes to 16.7 minutes, a difference of 4 minutes. The percentage reduction is 4 ÷ 20.7 × 100 = about 19.32%.

11. Did the machine learning model directly shorten a real outage?
No. The decrease comes from the response behavior assumed in the simulation after an alert. The experiment did not measure a real network recovery action.

12. What does eight out of ten disruptions mean?
In one selected trial, machine learning detected eight of ten simulated disruption groups, while the traditional rule detected none. That group-level count is not the same measure as 66.21% recall on individual network rows.

13. Why do timing assumptions matter?
If the response starts too late, the interruption may already have caused the damage. Changing when the response begins can change the result even when the detector's classification score stays the same.

14. What does balanced accuracy mean?
It gives weight to how well both attack and benign traffic are classified. That is useful when one class has many more rows than the other.

15. Does Notebook 11 prove H3?
It suggests that an alert followed by a timely modeled action could shorten disruption. It does not prove the same benefit on an operating network, and it does not show better scan recovery than automatic buffering in this run.
