1. Why did Notebook 08 need to be done?
The first H2 results looked strong in some ways but also had many false alarms. This notebook checks whether the result changes when the data split and the attack patterns are tested more carefully.

2. What was wrong with looking only at the original Random Forest accuracy?
It was 85.84%, while a simple non-spoofing guess would have been about 98.94% accurate. Random Forest found all the spoofing rows but flagged 1,489 non-spoofing rows incorrectly.

3. What is the majority baseline?
It is a simple check that always predicts the most common class. Here that means always answering non-spoofing. It catches no attacks, but it shows why accuracy can look high on uneven data.

4. What issue came up with the original train/test split?
The training group and test group ended up with different route types. Direct and transfer bags have different paths, so the model may have been responding partly to the route rather than only to spoofing.

5. What does a route-balanced split change?
It puts direct and transfer journeys in both training and testing. That makes the comparison less dependent on a route difference between the two groups.

6. What happened when the route types were balanced?
The saved test had 9,469 scan rows, including 116 spoofing examples. Random Forest and SVM reached 100% accuracy and recall on familiar simulated patterns.

7. Why is a perfect score still not the end of the story?
Those patterns were similar to what the models had already seen. A perfect result on familiar examples does not tell us whether the model can recognize a new type of spoofing.

8. What is an excluded-pattern test?
One spoofing pattern is left out during training and shown to the model later. This checks whether the model learned something broader than the exact patterns used to teach it.

9. What happened in the excluded-pattern test?
The models had 0% recall on each withheld spoofing pattern in the saved test. They were good at familiar simulated attacks but failed to flag those unfamiliar examples.

10. Does 0% recall mean machine learning can never catch a new attack?
No. It means these trained models missed the withheld patterns in this specific experiment. That is an important limitation, but it is not a claim about every possible model or real-world attack.

11. Why check a simple reader rule as well?
Sometimes an expected-reader or location mismatch can identify a problem without a complicated model. The simple rule reached about 66.38% spoofing recall in one saved comparison. It did not catch everything, but it gives a useful point of comparison.

12. What is data leakage?
It happens when a model is given information that makes the answer too easy, such as a field that directly tells it which records were spoofed. Preventing leakage matters more than getting an impressive score.

13. Why not choose the prediction threshold after looking at the final test?
That would mean adjusting the model to the answers in the test. The threshold of 0.65 was selected using a validation subset of training journeys instead.

14. What does a grouped bootstrap mean?
It repeats uncertainty calculations by sampling whole bag journeys rather than treating related scans as unrelated rows. Scans from one bag are connected, so grouping respects that structure.

15. Does this notebook support or challenge H2?
Both, depending on the claim. Random Forest did well on some familiar patterns, but high false alarms and failure on withheld patterns limit the claim that it is generally the best spoofing detector.

16. What is the main point to explain out loud?
A good score on one test can hide a weak model. Changing the route split and withholding attack patterns showed how much the conclusion depends on the way the simulated data were prepared.
