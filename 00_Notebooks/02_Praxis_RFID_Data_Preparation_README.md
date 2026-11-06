1. What is Notebook 02 doing?
It checks the scan records from Notebook 01 and gets them ready for testing. It adds useful comparison fields, such as whether a reader or location matches what was expected.

2. Why not use the original CSV exactly as it was?
The original file tells us what happened in the simulation. The tests also need fields that can be compared in a consistent way. Preparation makes those checks easier to run and easier to repeat.

3. Did the number of scan records change?
The saved result still has 31,575 rows from 5,000 journeys. It also shows 31,575 unique scan IDs. The number of fields grew from 26 to 34 because preparation added information used for checking and labeling.

4. What is the difference between a row and a field?
A row is one recorded scan. A field is one piece of information about that scan, such as its bag ID, reader ID, location, or time. Thirty-four fields does not mean thirty-four separate security controls.

5. What is an expected reader?
It's the reader that should have handled a scan at that point in a bag's route. If the observed reader is different, the record gets flagged for that mismatch.

6. Why compare expected and observed locations?
A bag scan at the wrong location may mean bad data or suspicious activity. Comparing the two helps identify a problem, but the mismatch alone does not tell us who caused it.

7. What is an out-of-sequence scan?
It is a scan that appears in an order that does not match the expected baggage path. For example, a record showing Arrival before Loading would need attention.

8. What does a delayed scan mean?
The scan arrives later than the time allowed by the rule used in the simulation. That delay can affect how current the tracking record is, even when the bag itself has not disappeared.

9. What did the saved preparation output find?
It shows 375 reader mismatches, 225 location mismatches, 225 sequence mismatches, and 225 delayed scans. The spoofing label appears on 375 scans. These figures describe the prepared simulated data.

10. Why are 30,225 rows normal and 1,350 abnormal when Notebook 01 created 1,500 abnormal journeys?
The 30,225 and 1,350 numbers describe scan rows that actually exist. The other 150 abnormal journeys involve missing scans. A missing row cannot be labeled as if it were present in the CSV.

11. Why keep the unusual records instead of cleaning them out?
Those are the cases the tests are supposed to find. Removing them would make the data look cleaner while taking away the very problems the research is studying.

12. What is a label in this notebook?
A label is the known answer attached to a scan, such as normal or abnormal. The later methods are scored by comparing their decisions to those known answers.

13. Could any prepared field make a detection test look too good?
Yes. If a model is given a field that directly reveals the known answer, it may look accurate without learning anything useful. Input fields and answer fields need to stay separate when training a model.

14. What happens if the preparation step is wrong?
Every later comparison could be affected. A wrong reader mapping or incorrectly calculated label can make a correct security check look bad, or make a weak check look good.

15. How does Notebook 02 connect to the hypotheses?
It prepares the same consistent records for H1, H2, and H3. This notebook is a setup step. The performance claims come from the notebooks that run and compare the methods.
