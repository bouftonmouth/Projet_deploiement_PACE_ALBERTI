Welcome to bio-inspired algorithme's documentation!
===================================================

This algorithm aims to create a population of genomes and to modify them by mutation and crossing over to make them as optimal as possible.
Each genome is assigned a cost.
This cost is obtained by adding the genes one after the other. Each time the current sum exceeds a threshold value (in absolute value) the cost increases by 1. The total sum finally gives the final cost of the genome.

The objective of this module is to observe the evolution of a population. All the parameters can be modified to recreate a population and control its evolution during as many generations as desired.

Have fun !