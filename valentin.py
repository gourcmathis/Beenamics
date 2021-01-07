# importations

import random


# a supprimer, permet simplement de verifier que les fonctions soient correctement codees, qu'il n'y ait pas d'erreur dans le code

def FORAGERSpollenactive(t):
    return 1.

def STORESpollen(t):
    return 1.

def NEEDpollen(t):
    return 1.

def FORAGERSnectaractive(t):
    return 1.

def CELLSempty(t):
    return 1.

def STORESnectar(t):
    return 1.

def WORKFORCEnectar(t):
    return 1.

def USAGEnectar(t):
    return 1.


# constants

# This constant permits to make a stochastic factor of the foraging factor
# If stochasticForagingFactor is set to 0, there is no stochastic factor. Otherwise, the interval will be between 1-stochasticForagingFactor and 1+stochasticForagingFactor
# This constant is used in FACTORforagingstoch(t), (47) 
stochasticForagingFactor = 0.25

LOADpollenforager = 0.06

TURNSpollenforager = 10.

FACTORforagingsuccess = 0.8

FACTORpollenstorage=6.

LOADnectarforager = 0.04

TURNSnectarforager = 15.

ProcessorsPerCell = 2.


# functions

#----------------------------------------------------------------------------------------------------------------------#
# Name : INCOMEpollent()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description : Permet de calculer le pollen produit chaque jour
# Variable : t
# Variation : LOADpollenforager can be 0.06 ; TURNSpollenforager can be 10. ; FACTORforagingsuccess can be 0.8
#---------------------------------------------------------------------------------------------------------------------#
def INCOMEpollent(t):
    return FORAGERSpollenactive(t) * LOADpollenforager * TURNSpollenforager * FACTORforagingstoch(t) * FACTORforagingsuccess


#----------------------------------------------------------------------------------------------------------------------#
# Name : FACTORforagingstoch()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description : Permet de calculer le facteur stochastique
# Variable : t
# Variation : stochasticForagingFactor can be 0.25
#---------------------------------------------------------------------------------------------------------------------#
def FACTORforagingstoch(t):
    return(random.uniform(1-stochasticForagingFactor , 1+stochasticForagingFactor))

#----------------------------------------------------------------------------------------------------------------------#
# Name : INDEXpollensituation()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description : Decrit le niveau de pollen, stoché par rapport aux besoins de la popûlation
# Variable : t
# Variation : FACTORpollenstorage can be 6.
#---------------------------------------------------------------------------------------------------------------------#
def INDEXpollensituation(t):
    return(min([1 , (STORESpollen(t)) / (NEEDpollen(t)*FACTORpollenstorage+1)]))

#----------------------------------------------------------------------------------------------------------------------#
# Name : INCOMEnectar()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description : Decrit la production de nectar
# Variable : t
# Variation : FACTORforagingsuccess can be 0.8 ; LOADnectarforager can be 0.04 ; TURNSnectarforager can be 15.
#---------------------------------------------------------------------------------------------------------------------#
def INCOMEnectar(t):
    return(min([FORAGERSnectaractive(t) * LOADnectarforager * TURNSnectarforager * FACTORforagingstoch(t) * FACTORforagingsuccess , CELLSempty(t-1)]))

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDprocessors()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description : determine les processeurs de nectar necessaires
# Variable : t
# Variation : ProcessorsPerCell can be 2.
#---------------------------------------------------------------------------------------------------------------------#
def NEEDprocessors(t):
    return STORESnectar(t-1) * ProcessorsPerCell


#----------------------------------------------------------------------------------------------------------------------#
# Name : PROCESSORS()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description :
# Variable : t
# Variation :
#---------------------------------------------------------------------------------------------------------------------#
def PROCESSORS(t):
    return(min([NEEDprocessors(t) , WORKFORCEnectar(t)]))

#----------------------------------------------------------------------------------------------------------------------#
# Name : PROCESSORS()
# Author : LABAT Valentin
# Date : 03/01/2021
#
# Description : Determine le nectar produit 
# Variable : t
# Variation : ProcessorsPerCell can be 2.
#---------------------------------------------------------------------------------------------------------------------#
def PROCESSEDnectar(t):
    return(min([STORESnectar(t-1) - USAGEnectar(t) , PROCESSORS(t) / ProcessorsPerCell]))



# Display

print(INCOMEpollent(1))
print(FACTORforagingstoch(1))
print(INDEXpollensituation(1))
print(INCOMEnectar(2))
print(NEEDprocessors(2))
print(PROCESSORS(2))
print(PROCESSEDnectar(2))
