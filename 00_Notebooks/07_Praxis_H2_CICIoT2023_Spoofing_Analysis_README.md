1. What is Notebook 07 doing that Notebook 06 did not do?
It tests the machine learning methods with public IoT network traffic instead of the simulated RFID baggage scans. The notebook runs a general attack test and a separate spoofing test.

2. What is CICIoT2023?
It is a public cybersecurity dataset containing network traffic. It can help test network attack classification, but it is not a record of baggage readers at an airport.

3. Why are there two classification tasks?
The first asks whether a network row is broadly attack traffic or benign traffic. The second looks specifically at spoofing categories, including ARP and DNS spoofing. A score on the broad attack task cannot be used as the spoofing score.

4. What is the difference between network spoofing and RFID reader spoofing?
Network spoofing involves things like misleading address or name information. RFID reader spoofing in the baggage simulation involves reader identity, location, or scan timing. They are related security ideas, but the evidence in the records is different.

5. What happened on the broad network attack test?
The saved result shows Random Forest at 98.37% accuracy and 99.16% F1. This is the general network attack task, not the specific spoofing result.

6. What is an F1 score?
It puts precision and recall into one number. It is useful when both missed attacks and false alarms matter, but I still need to look at precision and recall separately.

7. How rare was spoofing in the specific spoofing test?
The test had 2,150 spoofing rows among 211,221 network rows. That means most rows were not spoofing, so a high accuracy score can be misleading.

8. What did Random Forest do on the spoofing test?
The saved results show 96.84% accuracy, 99.95% recall, 24.38% precision, 6,664 false positives, and one missed spoofing row.

9. How could it miss only one attack and still be a problem?
Finding 2,149 of the 2,150 spoofing rows gives excellent recall. But it also wrongly flagged 6,664 non-spoofing rows. Only 24.38% of its spoofing alerts were correct.

10. What is the precision calculation?
2,149 correct spoofing alerts ÷ (2,149 + 6,664 total incorrect alerts) = about 24.38%. The calculation explains the false alert problem better than accuracy alone.

11. Why does a no-spoofing model score 98.98% accuracy?
Almost every network row is non-spoofing. Always predicting non-spoofing gets most rows right but misses all 2,150 spoofing cases. That is why the baseline and recall matter.

12. Why compare a model to such a simple baseline?
It shows whether the model is providing useful detection beyond guessing the most common answer. A complicated model is not automatically useful just because it produces a high percentage.

13. Does this notebook prove which model is best for baggage systems?
No. It provides a second type of machine learning test, using network traffic rather than simulated RFID records. It supports the wider security discussion, but the two results cannot be treated as the same type of evidence.

14. What is the main thing to remember about Notebook 07?
The general attack model looks strong, while the spoofing model has a serious false alert issue. I need to say which task I'm discussing whenever I give a number.
