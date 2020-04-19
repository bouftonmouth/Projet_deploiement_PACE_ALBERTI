#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:55:19 2019

@author: tpace
"""

import numpy as np
import matplotlib.pyplot as plt

def creta(taille):
    """
    Function that create a list that represents a genome.

    Args:
        taille (int): list size

    Return:
        List: contain a number "taille" of -1 and 1
    
    Exemple:
    		>>> creta(5)
    		[-1, 1, -1, 1, 1] #value are randomly generate, but all the list will contain 1 and/or -1.
    		
    """
    T=[]
    for i in range(0,taille):
        a=np.random.random(1)
        if a >= 0.5:
            d=1
        else:
            d=-1
        T.append(d)
    return T

def calc(gen,r0): 
    """
    Function that calulate the genome cost in function of r0.

    Args:
        gen (int): list that represent the genom
        r0  (int): threshold

    Return:
        cout (int): contain the genom cost.
        
    Exemple:
    		>>> a = [-1, 1, -1, 1, 1]
    		>>> calc(a, 1)
    		>>> 3
    """
    
    pos=0		 
    cout = 0
    for i in range(len(gen)):
        pos+=gen[i]
        if pos <= -r0 or pos >= r0:
            cout +=1
    return cout

        
def cretaN(nbr,taille):
    """
    Function that create a population with a size "nbr" and each individual
    got a genom with a size "taille".

    Args:
        nbr     (int): number of individuals in the population
        taille  (int): genome size

    Return:
        pop (list): contain a list of each individual. Each of individual is 
        represented by a genom.
        
    Exemple:
    		>>> cretaN(3,5)
    		>>> [[-1, 1, -1, -1, 1], [-1, -1, -1, 1, 1], [-1, 1, -1, 1, 1]]

    """
    pop=[]
    for i in range(nbr):
        pop.append(creta(taille))
    return pop

def calcN(pop,r0):
    """
    Function that calulate the genome cost in function of r0 for each individual and 
    return a list of position sorted by decreased cost.

    Args:
        pop (list): contain a list of each individual. Each of individual is 
                                represented by a genom.
        r0   (int): threshold

    Return:
        liste_ordre (list): contain position of individuals sorted by their increased cost.
     
    Exemple:
    		>>> p = [[-1, 1, -1, -1, 1], [-1, -1, -1, 1, 1], [-1, 1, -1, 1, 1]]
				>>> calcN(p,1)
				array([2, 0, 1])  
    """
    liste_cout=[] 
    for i in range(len(pop)):
        liste_cout.append(calc(pop[i],r0))
    liste_cout=np.array(liste_cout)
    liste_ordre = np.argsort(liste_cout)
    return liste_ordre


def select(pop,liste_rang_):
    """
    Function that select the N/2 individuals which have the highest score value
    and return them in a new list.

    Args:
        liste_rang_ (list): contain position of individuals sorted by their increased cost.
        pop         (list): list that contain the population.

    Return:
        pop_select  (list): list that contain the selected individuals.
        
    Exemple:
    		>>> p = [[-1, 1, -1, -1, 1], [-1, -1, -1, 1, 1], [-1, 1, -1, 1, 1]]
    	  >>> l = [2, 0, 1]
    	  >>> select(p,l)
    		 [[-1, 1, -1, 1, 1]]
    		 
    """
    nbr_select=int(len(pop)/2) 
    pop_select=[]
    for i in range(nbr_select):
        pop_select.append(pop[liste_rang_[nbr_select-1+i]])
    return pop_select

def mutation(pop_triée_,Tm):
    """
    Function that mutate the genome of individuals with a probability Tm. 

    Args:
        pop_triée_ (list): list of individuals with the highest score.
        Tm        (float): threshold which determine if the individal will be mutated.

    Return:
        pop_mutée_ (list): list of individuals after the mutation.
    
    Exemple:
    		>>> p = [[1, -1, -1, -1, -1, 1, 1, 1, 1, 1], [-1, 1, -1, 1, 1, 1, -1, -1, -1, -1], [-1, 1, 1, -1, 1, 1, 1, 1, -1, 1], [-1, -1, 1, -1, -1, 1, 1, -1, 1, -1], [1, -1, 1, 1, 1, 1, 1, 1, 1, -1]]
    		>>> l = [1, 0, 2, 3, 4] 
    		>>> pop = select(p,l)
    		[[1, -1, -1, -1, -1, 1, 1, 1, 1, 1], [-1, 1, 1, -1, 1, 1, 1, 1, -1, 1]]
    		>>> mutation(pop, 0)
    		[[-1, 1, 1, 1, 1, -1, -1, -1, -1, -1], [1, -1, -1, 1, -1, -1, -1, -1, 1, -1]]

    """
    pop_mutée_ = [[0 for x in range(len(pop_triée_[0]))] for x in range(len(pop_triée_))]
    for i in range(0,len(pop_triée_)):
        for j in range(0,len(pop_triée_[i])):
            a=np.random.random(1)
            if a >= Tm:
                pop_mutée_[i][j] = pop_triée_[i][j]*(-1)
            else:
                pop_mutée_[i][j] = pop_triée_[i][j]
    return pop_mutée_

def croisement(pop_mutée_,Tc):
    """
    Procedure that cross the genome between two individuals with a probability Tc. 


    Args:
        pop_mutée_ (list): list of individuals after the mutation.
        Tc        (float): threshold which determine if the genome of an individual will 
                           be crossed.

    Return:
    		>>> pop_mutated = [[-1, 1, 1, 1, 1, -1, -1, -1, -1, -1], [1, -1, -1, 1, -1, -1, -1, -1, 1, -1]]
    		>>> croisement(pop_mutated,0)
    		>>> pop_mutated
    		[[-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, 1, 1, -1, 1]]

    """
    for i in range(0,len(pop_mutée_)):
        a=np.random.random(1)
        if a > Tc:
            individu = np.random.choice(len(pop_mutée_))
            pos = np.random.choice(len(pop_mutée_[i]))
            part_ind_i = pop_mutée_[i][:pos]
            part_ind_crois = pop_mutée_[individu][:pos]
            pop_mutée_[i][:pos] = part_ind_crois
            pop_mutée_[individu][:pos] = part_ind_i
		
def concatene(pop,pop_mutée_,liste_rang_):
    """
    Function that conatenate individuals that weren't mutated and those who were.

    Args:
        pop 				(list): list that contain the population.
        pop_mutée_  (list): list of individuals after the mutation.
        liste_rang_ (list): contain position of individuals sorted by their increased cost.

    Return:
        pop_tot 		(list): list that contain all individuals mutated or not.
        
    Exemple:
    		>>> p = [[1, -1, -1, -1, -1, 1, 1, 1, 1, 1], [-1, 1, -1, 1, 1, 1, -1, -1, -1, -1], [-1, 1, 1, -1, 1, 1, 1, 1, -1, 1], [-1, -1, 1, -1, -1, 1, 1, -1, 1, -1], [1, -1, 1, 1, 1, 1, 1, 1, 1, -1]]
    		>>> pop_mutated = [[-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, 1, 1, -1, 1]]
    		>>> l = [1, 0, 2, 3, 4]
    		>>> pop_tot = concatene(p,pop_mutated,l)
    		[[-1, 1, -1, 1, 1, 1, -1, -1, -1, -1], [-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, 1, 1, -1, 1]]
    		
    """	
    nbr_select=int(len(pop)/2)
    pop_moins=[]
    for i in range(nbr_select):
        pop_moins.append(pop[liste_rang_[i]])
    pop_tot = pop_moins + pop_mutée_
    return pop_tot

def calc_cout(pop,r0):
    """
    Function that calulate the genome cost in function of r0 for each individual and 
    return a list of there individual cost.

    Args:
        pop (list): contain a list of each individual. Each of individual is 
                    represented by a genom.
        r0   (int): threshold

    Return:
        liste_cout (list): contain the cost of each individual in the populataion
        
    Exemple:
    		>>> pop_tot = [[-1, 1, -1, 1, 1, 1, -1, -1, -1, -1], [-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [-1, 1, 1, -1, 1, 1, 1, 1, 1, 1], [1, -1, -1, -1, -1, 1, 1, 1, -1, 1]]
    		>>> calc_cout(pop_tot,2)
    		array([2, 5, 5, 3])
    
    """
    liste_cout=[] # trié dans l'ordre croissant
    for i in range(len(pop)):
        liste_cout.append(calc(pop[i],r0))
    liste_cout=np.array(liste_cout)
    return liste_cout
    
def algofinal(T,r0,N,Tm,Tc,tour):
    """
    Function that -1: use the function cretaN
                  -2: use the function calcN
                  -3: use the function select
                  -4: use the function mutation
                  -5: use the procedure croisement
                  -6: use the function concatene
                  -7: use the function calc_cout
                  -9: calculate the mean and the minimum of the cost in the population
    the fucntion repeat step 2 to 9 "tour" times and then plot the cost evolution throught the
    time.

    Args:
        T    (int): genome size
        r0   (int): threshold
        N    (int): number of individuals in the population
        Tm (float): threshold which determine if the individal will be mutated.
        Tc (float): threshold which determine if the genome of an individual will 
                                be crossed.
        tour (int): algorithm iterations number

    Return:
        Liste_cost_min  (list): List that contain the minimum cost for each iteration.
        Liste_cost_mean (list): List that contain the average cost for each iteration.
        
    Exemple:
    		>>> algofinal(10,2,5,0,0,10)
    		[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1.25, 1.0, 1.0, 0.75, 2.75, 3.5, 2.0, 0.75, 0.75, 0.75]]

    """
    pop_Ngenome=cretaN(N,T)
    Liste_cost_min=[]
    Liste_cost_mean=[]
    liste=[k for k in range(0,tour)]
    for i in range(tour):
        liste_rang=calcN(pop_Ngenome,r0)
        pop_triée=select(pop_Ngenome,liste_rang)
        pop_mutée=mutation(pop_triée,Tm)
        croisement(pop_mutée,Tc)
        pop_Ngenome=concatene(pop_Ngenome,pop_mutée,liste_rang)
        cout_totaux=calc_cout(pop_Ngenome,r0)
        Liste_cost_min.append(min(cout_totaux))
        Liste_cost_mean.append(np.mean(cout_totaux))
    plt.plot(liste,Liste_cost_min)
    plt.plot(liste,Liste_cost_mean)
    plt.show
    return [Liste_cost_min,Liste_cost_mean]
    
