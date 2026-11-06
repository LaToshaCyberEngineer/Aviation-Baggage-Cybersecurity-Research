1. Why did Notebook 10 add another dataset?
Notebook 09 showed that buffering could restore scans. Notebook 10 asks whether a network detector can help decide when to start that response. It uses CICIDS2017 to test the network detection side.

2. What is CICIDS2017?
It is a public network intrusion dataset that includes DDoS traffic. It is not a set of baggage scans, so the network detection results and the RFID recovery calculations have to be explained separately.

3. What is the difference between detecting an attack and recovering a scan?
Detection means the network model raises an alert. Recovery means a delayed or lost scan update becomes available again. One does not automatically cause the other unless the simulated response rules say it does.

4. How well did the network detector perform?
The saved test shows 64.98% accuracy, 66.21% DDoS recall, 70.31% precision, and a 36.63% false-positive rate.

5. What does 66.21% recall mean?
The detector found about two-thirds of the actual DDoS rows in that test. It missed about one-third. That matters if the recovery response is only triggered when an alert happens.

6. What does the false-positive rate mean here?
The detector wrongly flagged 10,739 of 29,316 benign test rows. That's a lot of unnecessary alerts, so the response itself could become disruptive if every alert caused action.

7. What are the three recovery ideas being compared?
One is doing nothing. Another is buffering scans automatically. The third only starts recovery when the modeled analytics alert is triggered. The last two are not the same thing.

8. Which recovery approach performed better in this run?
Automatic store and forward restored 64 of 75 scans, or 85.33%. The single analytics-triggered trial restored 57 of 75, or 76%. The detector-triggered option did not beat ordinary buffering here.

9. Why did analytics-triggered recovery restore fewer scans?
It depends on receiving an alert. When detection is missed or delayed, the response may not begin in time. Buffering that starts automatically does not have that same alert dependency.

10. Why does the notebook discuss a 90% detection assumption?
One modeled response scenario assumes that 90% of the disruptions trigger an alert. That is a simulation setting, not the network detector's measured recall.

11. What happens when the measured 66.21% recall is used instead?
The sensitivity calculation estimates 42.37 restored scans out of 75, or about 56.50%. A fractional 42.37 is an expected value from a calculation, not a count of restored rows in one run.

12. Why do the 57 and 42.37 results not match?
They come from different scenarios. Fifty-seven is the outcome of a particular simulated trial. Forty-two point three seven is an estimate using a different detection assumption.

13. Are the network rows matched to individual baggage scans?
No. The public network test provides detection performance. The baggage recovery result uses that performance in a separate model. It is not a recorded network-to-bag sequence from an airport.

14. What does this mean for H3?
It does not establish that analytics improves recovery beyond automatic buffering. The results actually show a detection-dependent response can do worse when the detector misses attacks or gives too many false alerts.

15. What is the practical lesson here?
An alert is only useful if it starts the right action at the right time. Better detection alone does not guarantee better tracking continuity.
