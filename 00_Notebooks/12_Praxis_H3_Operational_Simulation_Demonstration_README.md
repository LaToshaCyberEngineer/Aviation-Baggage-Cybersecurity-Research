1. What is Notebook 12 doing?
It models what happens to scan messages minute by minute during an outage. Instead of only looking at the final number restored, it checks arrivals, waiting space, processing capacity, alerts, and delays.

2. What is a queue in this experiment?
It is a waiting line for scan messages that cannot be processed immediately. If the line gets too full, some messages may be dropped. A bag's scan can be delayed even if the original event happened on time.

3. What does buffer capacity mean?
It is how many waiting messages the system can hold. If more scans arrive than the buffer can store, the excess may be lost under the model's rules.

4. What does protected throughput mean?
It is the amount of scan traffic a modeled protective path can still process during the disruption. An alert by itself does not move any scan data. The model needs actual processing capacity for that.

5. How many affected scans are being tested?
The main disruption test uses 75 affected scans. Keeping that group fixed makes the different recovery conditions easier to compare.

6. What happens without buffering?
The model delivers zero of the 75 affected scans during the disruption scenario. That is the no-protection baseline in this particular simulation.

7. What happens with ordinary buffering?
The saved run delivers 60 of 75 scans, or 80%. Buffer limits and processing rules explain why the result is not automatically 75 of 75.

8. What happens with the traditional rule response?
In this selected run, it also delivers 60 of 75 scans, or 80%. The response does not improve the delivery count over ordinary buffering under those settings.

9. What happens with the machine learning response?
The modeled protective response delivers 72 of 75 scans, or 96%. That is 12 more delivered scans than the buffering-only case in this specific scenario.

10. Did machine learning itself deliver the extra 12 scans?
No. The difference comes from the protective processing path that the model allows after its alert. If there is no capacity to process scans, an alert alone does not improve delivery.

11. What happened when protected throughput was set to zero?
The model lost the delivery advantage even if alerts still occurred. That check is useful because it shows the improvement depends on response capacity, not just predicting an attack.

12. What happened to the delays?
Among delivered scans, the saved average delay was 14.25 minutes with buffering and 3.74 minutes with the selected machine learning response. Those are delays from the modeled queue, not measurements at an airport.

13. What was tested with normal scans and false alerts?
A separate trial used 75 normal scans. Ordinary handling delivered all 75, but an unnecessary protective response delivered 69 and lost six. That shows a wrong alert can have a cost.

14. Why isn't the false alert trial combined with the attack trial?
It tests a different situation. One asks whether protection helps during a disruption; the other asks whether unnecessary protection hurts normal processing. Both matter, but they should be reported separately.

15. Why do the H3 notebooks show different recovery percentages?
They are different models and settings, even when they start with the same 75 disrupted scans. Notebook 09 studies basic store and forward. Notebook 10 adds an alert dependency. Notebook 11 looks at response timing. Notebook 12 adds queue and capacity limits. They are not four independent airport measurements.

16. Does this fully prove H3?
No. It shows that analytics-triggered protection can help in a simulation when enough capacity is available and the response arrives on time. The improvement depends on assumptions, and false alerts can make normal processing worse.

17. What is the main point I should remember?
The useful result is not just that 72 scans were delivered. The important idea is that an alert must lead to a workable response, and that response needs enough capacity without harming normal operations.
