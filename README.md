# Election-Analysis

## Overview
Use Python to audit and declare a winner for an election. As well as gathering other information pertaining to the election such as: calculate the total number of votes casted, get a list of all the counties and their total votes, and create a list of the candidates, their total votes and percentage. Finally I had to find the winner based on the information collected during this audit. 

## Election audit results
* The total number of vote was 369,711 in the elction. This was calculated with a for loop where it counts the rows in the csv file that represents an individual voter then printed out in the terminal as shown:

![total_votes](https://user-images.githubusercontent.com/112291075/213797001-4ef82c49-10c6-48fe-8bc5-6a17b1d2110e.PNG)

* Here is how each county performed in the election as well as their overall percentage of voters.

![county_votes](https://user-images.githubusercontent.com/112291075/213797340-5d82f3b6-88ad-46be-9b57-e2f46161eae0.PNG)

* This shows that Denver had the largest number of voter turnouts at 82.8%.

* Here is the breakdown of how each candidate performed with the totalvotes that they received.

![candidate_votes](https://user-images.githubusercontent.com/112291075/213798008-97efd54b-f8b1-432e-89c5-13345053d013.PNG)

* The result of the election was Diana DeGette winning the overall election! I was also able to retrieve how many votes she received as well as her winning percentage. 

![winner](https://user-images.githubusercontent.com/112291075/213798246-a8400e1f-7b69-4cf4-8911-61cddd0860ce.PNG)

## ELection audit summary
The criteria was that the winner should have an equal or greater percentage than 50.1% overall. Diana DeGette won that by a supermajority at 73.8%. I would propose that instead this code could be altered to check for a supermajority of 66.7% instead. The counties total percentage weights could also represent the electoral college votes and then this code could be used for any election, not just on a local scale. 
