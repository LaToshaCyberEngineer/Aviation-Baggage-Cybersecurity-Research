1. What am I doing in Notebook 01?
I'm making a practice set of baggage tracking records. Each bag moves through a route, and some of those movements have problems added on purpose. Later notebooks use these records to test whether the security checks can find the problems.

2. Are these actual bags from an airport?
No. The records are simulated. That means the bag journeys, reader scans, and problems were created for testing. The results help compare methods under the same conditions, but they cannot tell us what happens at a real airport.

3. Why did I start with 5,000 bag journeys?
Five thousand was a setting chosen for the simulation, not an airport statistic. It gave the study enough journeys to build normal and unusual examples without pretending to have airline records.

4. Why are there direct and transfer routes?
Not every bag follows the same path. A direct bag goes through six expected scan points. A transfer bag has seven because it includes a transfer point. A scan is only missing when it should have been part of that bag's route.

5. What does a custody point mean?
It's a place where a bag's movement should be recorded, such as Screening, Sorting, Loading, Arrival, or Claim. The scan is a record of the event, not proof that someone physically watched the bag move.

6. Why are there 3,500 direct journeys and 1,500 transfer journeys?
That's the 70/30 route mix built into the simulation. It is useful for testing different paths. It is not presented as the normal route mix across airlines.

7. How did 5,000 bags turn into 31,500 scan events at the start?
Each of the 3,500 direct bags gets six expected scans. Each of the 1,500 transfer bags gets seven. So 3,500 × 6 plus 1,500 × 7 equals 31,500 scans before any problems are added.

8. Why does the saved file have 31,575 rows instead of 31,500?
The code added 225 duplicate scan rows and removed 150 expected scan rows. So 31,500 + 225 − 150 = 31,575. That's why the number of scans is not the same as the number of bags.

9. How many journeys were marked as unusual?
There were 1,500 abnormal journeys and 3,500 normal ones in this run. Those labels were assigned during data generation. They are the answers used to check detection later.

10. What kinds of problems did the code add?
The design included 375 reader spoofing journeys, 225 duplicate cases, 225 location problems, 225 out-of-sequence cases, 225 delays, 150 missing-scan journeys, and 75 denial-of-service cases. These are planned test cases, not observed attack rates.

11. What does reader spoofing mean in this test?
It means a scan looks like it came from a reader that should not have been trusted. The code changes the reader-related information to create that situation. It does not recreate every way someone could spoof a real RFID reader.

12. Why can't a missing scan be found by searching for a bad scan row?
Because the problem is that a row never appeared. To find it, the security check must know which scan points were expected for that bag and notice that one is missing.

13. What are the 75 denial-of-service events used for?
They give the later H3 notebooks a fixed group of interrupted scans. Those notebooks test how many scan records can be restored under different recovery rules. The 75 records are not proof of a real network attack.

14. What is a random seed, and why did I use 42?
A seed helps the random choices come out the same way when the code is run under the same conditions. It helps repeat the experiment. It does not make the generated records more realistic by itself.

15. How does Notebook 01 connect to my three research questions?
It supplies the baggage records that the later tests need. H1 checks the security rules, H2 checks spoofing predictions, and H3 checks scan recovery. Notebook 01 creates the test data; it does not prove any of those hypotheses.

16. What is the biggest thing to be careful about when explaining this data?
The abnormal conditions were deliberately built into the dataset. A method may do well partly because the patterns are clear. Any claim about real airport performance would need a different kind of evidence.
