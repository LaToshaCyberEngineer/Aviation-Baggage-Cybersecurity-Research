1. What am I comparing in Notebook 03?
Two ways of checking the same simulated baggage scans. One uses basic traditional rules. The other adds Zero Trust checks for reader identity and whether the scan fits the expected bag journey.

2. What does Zero Trust mean in this test?
It means a scan is not accepted just because it arrived. The method checks information such as the reader, location, and behavior before treating it as trustworthy.

3. What is the traditional method doing?
It applies a smaller set of checks to the same records. That gives us a comparison point so we can see what the added validation catches.

4. Why use the same scans for both methods?
If each method had different data, the comparison would be harder to interpret. Keeping the records the same helps show the effect of the checks being compared.

5. What does a true positive mean here?
An abnormal scan was correctly flagged as abnormal. A false negative is an abnormal scan that the method missed.

6. What did the traditional rules catch?
In the saved run, they found 825 of 1,350 abnormal scan rows and missed 525. That is 61.11% recall. The recorded false-positive count was zero in this controlled test.

7. What did the Zero Trust checks catch?
They found 1,275 of the 1,350 abnormal scan rows and missed 75. That is 94.44% recall. The saved run also reported zero false positives.

8. How much better was the recall?
It increased from 61.11% to 94.44%, an improvement of 33.33 percentage points. That's a difference between two percentages, not a claim that the system became 33.33% safer.

9. What does recall actually tell me?
Out of all the abnormal scans that were really there, recall tells me how many were found. High recall is useful when the cost of missing a suspicious scan is important.

10. What about accuracy?
Accuracy measures how many total decisions were right. The saved results show 98.34% for traditional rules and 99.76% for Zero Trust. Because most scans are normal, recall gives a clearer picture of the abnormal scans that were missed.

11. Why did both methods show no false positives?
The test conditions and rules were very controlled. That is what the saved output reports, but it is not evidence that real airport operations would have no false alarms.

12. What happened to the missing-scan journeys?
A separate journey check found all 150 missing-scan cases in the simulated set. That is different from classifying the 1,350 abnormal scan rows. Those numbers should not be mixed into the same recall calculation.

13. What could explain the better Zero Trust score besides the idea of Zero Trust itself?
The added checks line up with the simulated problems. That makes it possible for the method to catch more cases. It is a useful test of the rules, but it also means the result depends on how the abnormal data were made.

14. What does this say about H1?
The result supports H1 under these simulated conditions: the added checks caught more abnormal scans than the traditional checks. It does not establish the same improvement on unfamiliar attacks or live airport data.

15. What is the one calculation to remember?
Traditional recall is 825 ÷ 1,350 = 61.11%. Zero Trust recall is 1,275 ÷ 1,350 = 94.44%. Both use the same 1,350 abnormal scan rows.

16. What would make this finding stronger?
Trying different attack patterns, more realistic mistakes, and data from another source would show whether the improvement holds when the conditions are less predictable.
