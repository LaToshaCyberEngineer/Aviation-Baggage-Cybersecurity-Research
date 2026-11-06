1. What is Notebook 09 checking?
It looks at what happens when baggage scan messages cannot reach the tracking system during a simulated disruption. The comparison is between losing those updates and keeping some of them until the connection is available again.

2. What does denial of service mean here?
For this experiment, it means scan records are delayed or blocked from reaching the backend. The code models the effect on the tracking record; it does not show a live attacker shutting down an airport network.

3. Why use the same 75 scans in each condition?
It keeps the comparison fair. We can compare what happens to the same interrupted population under different recovery methods rather than changing both the problem and the response.

4. What happens when there is no recovery method?
All 75 affected scan updates stay unavailable to the backend in the baseline scenario. The notebook treats the 75 related journeys as incomplete because those updates are missing.

5. What does store and forward mean?
Instead of throwing away a scan that cannot be sent, the system keeps it for later and forwards it when a connection is available. That can restore a tracking history, but it may arrive late.

6. How many scans were buffered and restored?
The saved run buffered 66 of the 75 affected scans. Of those, 64 were restored. Eleven of the original 75 remained permanently unavailable in the modeled result.

7. Why wasn't every scan recovered?
The simulation has limits and recovery rules. Some records were not buffered or were not restored successfully. That's why the measured result must come from the actual counts rather than assuming 100% recovery.

8. What is the overall recovery rate?
64 restored scans divided by 75 affected scans = 85.33%. That is the percentage recovered from the whole disrupted group.

9. Why is 96.97% also mentioned?
That is 64 restored scans divided by 66 buffered scans. It answers a different question: of the scans that were buffered, how many came back? The denominator changes the meaning.

10. Why does the original CSV still show the disrupted scans?
The CSV is the input record of what the simulation was supposed to handle. The baseline models those records as unavailable to the backend. It is a modeled loss of delivery, not a deletion of the input rows.

11. What is record staleness?
It is how old a scan's information is by the time the system receives it. A restored update can still be too old to give a current view of a bag's location.

12. What were the delay results?
The saved result shows an average modeled recovery delay of 2.70 minutes and average staleness of 23.34 minutes for restored events. They measure different parts of the timing, so they should not be treated as the same delay.

13. Did analytics automatically detect the denial-of-service events in this notebook?
No. This first H3 analysis mainly tests what recovery can do once a disruption is modeled. Later H3 notebooks look more closely at detection and response.

14. Does this support H3?
It supports the idea that a modeled continuity control can reduce permanent scan loss. It does not show that cybersecurity analytics caused the improvement or that a real airport would recover at the same rate.

15. What is the one result I should remember?
Without recovery, none of the 75 affected scan updates reached the backend in the modeled baseline. With store and forward, 64 of 75 were restored. That is a useful continuity result, with clear limits.
