1. What is Notebook 06 trying to find out?
It compares Logistic Regression, Support Vector Machine, and Random Forest to see which one does better at recognizing the simulated spoofing records. This is the main model comparison for H2.

2. What is spoofing in this notebook?
The code creates examples where reader information or scan timing looks wrong. It is testing whether the models recognize those simulated patterns. It is not testing every type of RFID spoofing that could happen at an airport.

3. How much data is being classified?
There are 31,575 scan rows. Only 375 are labeled spoofing. The other 31,200 are labeled non-spoofing for this specific task.

4. Does non-spoofing mean the scan is normal?
Not necessarily. A scan could have another problem, such as a delay, and still be non-spoofing. The model is being asked one question: is this a spoofing example or not?

5. Why compare these three models?
They make decisions differently. Logistic Regression uses weighted inputs, SVM looks for a separating boundary, and Random Forest combines decisions from many trees. The comparison checks how those methods behave on the same task.

6. What are predictors?
These are the input fields a model can look at before making a prediction, such as reader or scan context. The notebook prepares 13 predictors. A field that gives away the true spoofing label would make the test unfair.

7. Why split the data by bag instead of by individual scan?
One bag has several related scans. If some of its scans are used for training and others for testing, the model may be seeing information from the same journey twice. Grouping by bag helps avoid that overlap.

8. Was the original split completely fair?
It kept bag journeys separate, but a later check found that the training and test groups had different route types. That matters because direct and transfer journeys do not follow the same scan path. Notebook 08 examines this issue.

9. What does class imbalance mean here?
Spoofing is rare compared with non-spoofing. A model can look good on overall accuracy simply by saying almost everything is non-spoofing.

10. What were Random Forest's original test results?
The saved test shows 85.84% accuracy, 100% spoofing recall, 6.94% precision, and 1,489 false positives. Those numbers must be read as a group, not separately.

11. What does 100% recall mean here?
Random Forest found all 111 actual spoofing rows in that test. It did not mean every prediction was correct.

12. Why was precision only 6.94%?
There were 111 correct spoofing alerts and 1,489 incorrect spoofing alerts. So 111 ÷ (111 + 1,489) = 6.94%. Most alerts would have sent someone to check a scan that was not spoofing.

13. Why is 85.84% accuracy not enough to call it the best detector?
A model that always answered non-spoofing would score about 98.94% accuracy in that test, even though it would catch no spoofing at all. Accuracy alone hides that problem.

14. Did Random Forest win H2?
It ranked highest among the three models on the original comparison's accuracy measure, but the false alarms were serious. Notebook 08 adds testing that makes the conclusion more limited. I should not describe the model as generally best for airport use.

15. What is the difference between a false positive and false negative?
A false positive is a normal-for-this-task scan incorrectly flagged as spoofing. A false negative is a spoofing scan the model misses. This test had many false positives even though it missed none of the spoofing rows.

16. What needs to be explained when discussing this notebook?
Why the labels are uneven, why the split matters, and why accuracy, precision, and recall point to different conclusions. The numbers show what happened under this simulated test, not what would happen at an airline.
