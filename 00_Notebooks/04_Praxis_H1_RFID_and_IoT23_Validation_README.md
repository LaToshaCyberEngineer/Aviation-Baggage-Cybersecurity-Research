1. What is different about Notebook 04?
It looks at H1 from two angles. First, it tests the RFID checks on a held-out group of simulated bag journeys. Then it looks at a public IoT network dataset called IoT23.

2. Why use a held-out RFID group?
Those journeys are kept aside for another check instead of using every bag in the same comparison. It gives us a clearer look at how the rules perform on records not selected for the earlier analysis.

3. How much RFID data was in that check?
The saved run included 8,764 scan rows from 1,250 bag journeys. Remember, a journey contains several scans. The two numbers do not count the same thing.

4. What exactly is IoT23?
It is a public dataset of network connections involving IoT traffic. It is not a collection of airline baggage scans or RFID reader events.

5. Why include IoT23 at all?
It lets the research look at another kind of security signal: unusual network activity. That helps explain the broader security setting, but it must stay separate from what was measured on simulated bags.

6. Did the code match IoT23 network rows to individual bags?
No. The two datasets were evaluated separately. It would be wrong to claim that an IoT23 connection happened during one of the simulated baggage journeys.

7. How much IoT23 traffic was reviewed?
The saved run contains 23,145 connection rows: 21,222 labeled malicious and 1,923 labeled benign. Those labels describe network traffic, not baggage conditions.

8. How many IoT23 records did the alert rule flag?
The saved output shows 14,574 flagged network records. That number by itself does not tell us how many alerts were correct; it needs to be compared with the dataset labels.

9. What does a one-minute window mean?
The code groups network activity into one-minute periods so it can count how much activity happened close in time. A busy minute can be worth checking, but a high count does not automatically mean an attack.

10. Why does the label mix matter?
The IoT23 sample has far more malicious than benign rows. When one class dominates, accuracy can be misleading. We need to know how the rule treats both groups.

11. What is the main risk when explaining the two results?
Don't add the RFID rows and network rows into one sample or claim the IoT23 results measured airport attacks. They answer different questions.

12. Does this prove a Zero Trust system would work on actual baggage readers?
No. It adds a second look at the simulated RFID checks and a separate network example. Real RFID deployment would need data and testing from that environment.

13. What does this contribute to H1?
The held-out RFID comparison gives more information about the implemented security checks. The network portion adds context, not direct confirmation of RFID baggage anomaly detection.

14. What should I say if someone asks whether the results are independent?
The RFID records still come from the same simulation design. Holding journeys aside helps with testing, but it does not make them a new airport dataset. IoT23 is an independent source of network traffic, not an independent baggage experiment.
