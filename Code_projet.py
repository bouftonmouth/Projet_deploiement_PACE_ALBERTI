#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:55:19 2019

@author: tpace
"""

import numpy as np
import matplotlib.pyplot as plt

def creta(taille): #fonction qui permet de créer un génome.
"""
Function that creat a list that represents a genom.

Args:
	taille (int): list size
	
Return:
	List: contain a number "taille" of -1 and 1
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

def calc(gen,r0): # calcule le coût du génome par rapport aux nombres de pas 
     			  # en dehors de [-r0,r0].
"""
Function that calulate the genome cost in function of r0.

Args:
	gen (int): list that represent the genom
	r0  (int): threshold
	
Return:
	cout (int): contain the genom cost.
"""
    
    pos=0		 
    cout = 0
    for i in range(len(gen)):
        pos+=gen[i]
        if pos <= -r0 or pos >= r0:
            cout +=1
    return cout

        
def cretaN(nbr,taille): # crée un population de "nbr" génome de taille "taille".
"""
Function that creat a population with a size "nbr" and each individual
got a genom with a size "taille".

Args:
	nbr     (int): number of individuals in the population
	taille  (int): genome size
	
Return:
	pop (list): contain a list of each individual. Each of individual is 
	represented by a genom.
"""
    pop=[]
    for i in range(nbr):
        pop.append(creta(taille))
    return pop

def calcN(pop,r0): # calcule le coût de chaque population et retourne une liste
		        # du rang de la population dans la liste de la popualtion d'origine
  			    # trié dans l'ordre croissant
"""
Function that calulate the genome cost in function of r0 for each individual and 
return a list of position sorted by decreased cost.

Args:
	pop (list):  contain a list of each individual. Each of individual is 
	represented by a genom.
	r0  (int): threshold
	
Return:
	liste_ordre (list): contain position of individuals sorted by their increased cost.
"""
    liste_cout=[] 
    for i in range(len(pop)):
        liste_cout.append(calc(pop[i],r0))
    liste_cout=np.array(liste_cout)
    liste_ordre = np.argsort(liste_cout)
    return liste_ordre


def select(pop,liste_rang_): # sélectionne les N/2 individus avec les valeurs de coût les plus importantes. 

    nbr_select=int(len(pop)/2) 
    pop_select=[]
    for i in range(nbr_select):
        pop_select.append(pop[liste_rang_[nbr_select-1+i]])
    return pop_select

def mutation(pop_triée_,Tm): # fonction qui parcours chaque génome et a une probabilité
							 # de faire muter les gènes et renvoie les génomes mutés.
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
    nbr_select=int(len(pop)/2)
    pop_moins=[]
    for i in range(nbr_select):
        pop_moins.append(pop[liste_rang_[i]])
    pop_tot = pop_moins + pop_mutée_
    return pop_tot

def calc_cout(pop,r0): # calcule le coût de chaque population et retourne une liste
		        # du rang de la population dans la liste de la popualtion d'origine
    liste_cout=[] # trié dans l'ordre croissant
    for i in range(len(pop)):
        liste_cout.append(calc(pop[i],r0))
    liste_cout=np.array(liste_cout)
    return liste_cout
    
def algofinal(T,r0,N,Tm,Tc,tour):
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
#####################################################################################

# genome=creta(100)
# print(genome)

# print(calc(genome,4))

# pop_Ngenome = cretaN(100,200)
# print(pop_Ngenome)

# print(calcN(pop_Ngenome,4))

# liste_rang=calcN(pop_Ngenome,4) 
# pop_triée=select(pop_Ngenome,liste_rang)
# print(pop_triée)
# print(calcN(pop_triée,4))

# pop_mutée = mutation(pop_triée,0.5)
# print(pop_mutée[0])
# print(pop_triée[0])


# croisement(pop_mutée,0.05)

# pop = concatene(pop_Ngenome,pop_mutée,liste_rang)

# cout_totaux = calc_cout(pop,4)
# print(min(cout_totaux))
# print(np.mean(cout_totaux))

####### mini,moy=algofinal(500,4,100,0.05,0.1,500)
# critère d'arrêt nombre de tour où convergence vers une valeur (mais dure
# à trouver)

#def algofinal(T,r0,N,Tm,Tc,tour):

#mini,moy=algofinal(10,4,100,0.05,0.1,200)
#mini,moy=algofinal(1000,4,100,0.05,0.1,200)
#T est lié à la valeur de cout, plus il est petit plus le cout mayen
#et minimum sera faible

#mini,moy=algofinal(500,1,100,0.05,0.1,200)
#mini,moy=algofinal(500,2,100,0.05,0.1,200)
#mini,moy=algofinal(500,3,100,0.05,0.1,200)
#plus le r0 est petit plus la valeur de coût minimla est forte au début, mais 
#on observe aussi une baisse du coût minimal très rapide.
# plus le r0 est grand plus la valeur du coût minimum initial est faible
#mais on observe une baisse lente du coût minimla au fur et à mesure des générations

#mini,moy=algofinal(500,4,100,0.0005,0.1,200)
#augmentation du taux de mutation => cout mut mini augmente et la descente
#du cout mini est plus lente, le coût moyen augmente très légèrement
    
mini,moy=algofinal(500,4,100,0.05,0.001,200)











