# Google has Code 2021
The hash code was around Google maps. It went around the possibility of controlling the street lamps.
Google Maps

Link to the demo
https://youtu.be/YPOVd-hQUjA
### Members
Team name: Semi-Azzi

* Jean Paul Chaiban
* Ebrahim Karam
* Abel Sostre 

### Our Score During Competition
We seemed to have a trouble with the submission of file d and were getting 0 points on it. This is an attempt to clean up and go through it. 

During the competition, we were able to get 
7,399,566 points
We were ranked 5112 in the world, ranked 23 in Lebanon, and 207 in the US.

It is divided in the following manner
![ScoreDuringCompetition](https://user-images.githubusercontent.com/10140799/109393997-aa544400-78f2-11eb-807e-50cb962b8cc3.png)

**PLEASE NOTE**
parising the information takes a while as well as figuring out how to parse the outputs

## The naive Algorithm
Well currently streets lamps just cycle through on the intersections. We just turn on for second for each of the intersections. The tricky part is getting the intersections connected to each street. We just make it it turn on for 1 second each.

Now I rewrote the naive implementation and we got the follwoiung score. 7,885,740 points. This is a bit upsetting since we would have gotten a higher score with File D which gave a score of zero during the implementation.

Now, here we considered the intersections to be considered at the end of the road. When we turn a green light, we turn the green light for the road that the car is already on. We aren't turning on for the road it will got to. (A key point to understand.)

![naiveImplementation](https://user-images.githubusercontent.com/10140799/109394042-ec7d8580-78f2-11eb-9092-d8dc5b7254e6.png)

You can check the implementaion by checking `Naive_implemtation.py`



## Removing Unessarary roads and turning on more frequent roads longer
The cars aren't passing on each road so if we removed the roads that aren't being used we can drastically improve the code. 

We understand that cars start at the end of the road mentioned. 
If a road is in the path for multiple cars, we prefer to keep it on longer than other routes since it's more used and we don't want it to get jammed. 

### Removing unecessary Roads
If we just remove the intersections that no car passes by or uses. We get the following score. 8,629,998 points
![removeUneccessaryRoads](https://user-images.githubusercontent.com/10140799/109398558-9ff27400-790b-11eb-8c64-abf0b38606d1.png)
This actaully improves our ranking to the following in the extended round
* 874 worldwide
* 6 in Lebanon
* 36 in the US

You can check the implementation by checking the code labeled `RemoveRoads_implemtation.py`

### Stay on for longer where more used
If cars are going to be using a road more often they need to be on more often then those that aren't used more often.


## Extra notes
* Some cars will never arrive to their destination. simple because the path they plan to take is longer than the simulation time even. If the car was able to hit every green light, it would be too slow to arrive. (this is why you can never get 2 cars to arrive in example 1)
* Given the above. A car will never travel the full path given the simulation time.



