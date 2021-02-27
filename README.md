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

It is divided in the fowllign manner
![ScoreDuringCompetition](https://user-images.githubusercontent.com/10140799/109393997-aa544400-78f2-11eb-807e-50cb962b8cc3.png)

**PLEASE NOTE**
parising the information takes a while as well as figuring out how to parse the outputs

## The naive Algorithm
Well currently streets lamps just cycle through on the intersections. We just turn on for second for each of the intersections. The tricky part is getting the intersections connected to each street. We just make it it turn on for 1 second each.

Now I rewrote the naive implementation and we got the follwoiung score. 7,885,740 points. This is a bit upsetting since we would have gotten a higher score with File D which gave a score of zero.

Now, here we considered the intersections to be considered at the end of the road. When we turn a green light, we turn the green light for the road that the car is already on. We aren't turning on for the road it will got to. (A key point to understand.)

![naiveImplementation](https://user-images.githubusercontent.com/10140799/109394042-ec7d8580-78f2-11eb-9092-d8dc5b7254e6.png)

You can check teh implementaion by checking `Naive_implemtation.py`



## Removing Unessarary roads
The cars aren't passing on each road so if we removed the roads that aren't being used we can drastically improve the code. 

We understand that cars start at the end of the road mentioned. In a way, we don't care if the car starts in a certain place and nno other car enters that road. So we should actually ignore the first path in the cars planned trajecotry.

If a road is in the path for multiple cars, we prefer to keep it on longer than other routes since it's more used and we don't want it to get jammed



## Extra notes
* Some cars will never arrive to their destination. simple because the path they plan to take is longer than the simulation time even. If the car was able to hit every green light, it would be too slow to arrive. (this is why you can never get 2 cars to arrive in example 1)
* Given the above. A car will never travel the full path given the simulation time.



