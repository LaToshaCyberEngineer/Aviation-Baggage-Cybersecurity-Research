1. What is Notebook 13 trying to find out?
It compares Logistic Regression, Support Vector Machine, and Random Forest to see how well they detect malicious IoT network traffic from devices that were not used for training. This is a supplemental network detection test related to H3.

2. What is the N BaIoT dataset?
It is a public dataset of network traffic recorded from nine commercial IoT devices. It includes normal activity and attacks from Mirai and Gafgyt, also called BASHLITE, botnets. It is not a dataset of airline baggage scans.

3. Why am I using N BaIoT for H3?
H3 asks whether cybersecurity analytics can reduce the effects of denial of service disruptions on baggage tracking. Notebook 13 checks whether machine learning can recognize malicious network traffic. Finding attacks is one part of a possible response, but this test does not measure whether baggage operations improved.

4. How many CSV files did the notebook find?
The saved inventory found 90 CSV files: nine benign traffic files, 80 botnet attack files, and one demonstration file that was not used for model training. The actual test used files with recognized benign or attack labels.

5. What are the 115 features?
They are numerical measurements describing patterns in network traffic, such as activity over different time periods. The models use those measurements to make predictions. Device names, filenames, and attack labels were kept out of the predictors.

6. Why did I use 7,200 records?
The code sampled records from the larger files to keep the experiment manageable. The final sample had 3,600 benign and 3,600 malicious records across nine devices.

7. Why were the two classes balanced?
Balancing lets the models be compared with equal numbers of benign and malicious examples. It also makes the test different from a real network, where attacks may be much less common. The reported precision should not be treated as a real airport false alert rate.

8. What does device held out validation mean?
A device used for testing is not used for training in that same fold. This checks whether the model can recognize malicious traffic from a different device rather than only from devices it has already seen.

9. Why are there three validation folds?
The nine devices are divided into three testing groups. The code trains on the other devices and tests on the held-out group, repeating the process three times. Step 6 confirmed that the training and testing devices did not overlap.

10. Which models were compared?
The notebook compared Logistic Regression, Support Vector Machine, and Random Forest. It also included a majority class baseline, which simply predicts the most common training label. All four used the same held-out records.

11. What did the majority class baseline show?
It achieved 50% accuracy in the balanced sample but found none of the 3,600 malicious records. That shows why accuracy alone cannot tell me whether a model is useful for detecting attacks.

12. What were Random Forest's results?
Random Forest had the highest accuracy at 99.83%. It correctly detected 3,599 of the 3,600 malicious records, with 99.97% recall and 99.70% precision. It made 11 false-positive errors and one false-negative error.

13. How did the other two models perform?
Logistic Regression achieved 99.60% accuracy, with 24 false positives and five false negatives. Support Vector Machine achieved 99.21% accuracy, with 45 false positives and 12 false negatives. Random Forest ranked highest among these three models in this test.

14. Did Random Forest work equally well on every device?
No. All 11 false positives came from the SimpleHome XCS7 1002 security camera, and the one missed malicious record came from the Provision PT 838 security camera. That matters because a strong overall score can hide device-specific problems.

15. Why does Step 6 report 28,800 predictions?
Each of the four classifiers made predictions on the same 7,200 sampled records across the three folds. So 7,200 times 4 equals 28,800 predictions. That does not mean the study had 28,800 different network records.

16. Does testing unfamiliar devices mean the models can detect unfamiliar attacks?
No. The test held out devices, but it still used the known Mirai and Gafgyt attack families. A new botnet or a different network setting could produce different results.

17. Does Notebook 13 prove H3?
No. It shows that the tested models, especially Random Forest, identified malicious network traffic well in this sample. It did not measure scan delivery, lost baggage events, recovery time, or an adaptive response. Those operational questions belong to the other H3 simulations.

18. What should I be careful about when explaining or saving this experiment?
The results come from a balanced sample of commercial IoT network traffic, not airport RFID equipment. The notebook reported saving its results under 09_H3_Results, but those exported files and the GitHub commit still need to be checked. Step 5 has no saved output, although Step 6 checked the device split. Neither the original data nor earlier results should be overwritten.
