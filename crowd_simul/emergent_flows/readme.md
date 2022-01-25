# Emergent Fundamental Pedestrian Flows from cellular automata 

So I tried to implement the paper of this name in python. It's not a very complex code. We take a 2D circular array(list in this case) and have the pedestrians move in between them. There could be pedestrians with varying possible speeds. 

### The values of cells in the list could be:
1. 0, if the cell is unoccupied
2. n, if the cell is occupied, where n is the maximum possible speed of the pedestrian occupying the cell

Through every iteration, we first determine if the pedestrian would remain in its current lane(1D list) or switch to adjacent ones. If the parallel cells in adjacent lanes are unoccupied, we calculate the gaps which the pedestrian could move forward with in that lane. 
After comparing possible gaps, the pedestrian is moved forward by that many cells in case the gaps are less than the maximum possible speed. If not it is advanced by its maximum speed.

As the list is circular, the pedestrians keep moving forward indefinitely with the density constant
