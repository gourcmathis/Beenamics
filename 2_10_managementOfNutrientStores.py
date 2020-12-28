# -*- coding: utf8 -*-

print("test de lancement")

#--------------------------------------------------------------#
def USAGEnectar(t):
    liste_var = []
    needNectar_var = NEEDnectar(t)
    storeNectar_var = STORESpollen(t-1)

    liste_var.append(needNectar_var)
    liste_var.append(storeNectar_var)

    return min(liste_var)

print(USAGEnectar(t))

#--------------------------------------------------------------#

def USAGEpollen(t):
    #Data given by Blaschon
    #et al. (1999) depicting pollen stores during artificial rain
    #periods suggested: FACTORpollensavingmax = 0.3 (0.33 in HoPoMo)
    FACTORpollensavingmax = 0.30

    liste_var = []
    needPollen_var = NEEDpollen(t-1)*(1-(FACTORpollensavingmax*(1-INDEXpollensituation(t-1))))
    storePollen_var = STORESpollen(t-1)

    liste_var.append(needPollen_var)
    liste_var.append(storePollen_var)

    return min(liste_var)

print(USAGEpollen(t))

#--------------------------------------------------------------#

def USAGEhoney(t):
    liste_var = []
    storeHoney_var = STOREShoney(t-1)
    nectar_var = (NEEDnectar(t)-USAGEnectar(t))
    #Data from Seeley(1995)
    ratioNectar = 0.4

    liste_var.append(storeHoney_var)
    liste_var.append(nectar_var)
    liste_var.append(ratioNectar)

    return min(liste_var)

print(USAGEhoney(t))

#--------------------------------------------------------------#

def STORESpollen(t):

    return STORESpollen(t-1)+INCOMEpollen(t)-USAGEpollen(t)

print(STORESpollen(t))

#--------------------------------------------------------------#

def STORESnectar(t):

    return STORESnectar(t-1)+INCOMEnectar(t)-USAGEnectar(t)-PROCESSEDnectar(t)

print(STORESnectar(t))

#--------------------------------------------------------------#

def STOREShoney(t):
    ratioNectar = 0.4
    return STOREShoney(t-1)-USAGEhoney(t)+(PROCESSEDnectar(t)*ratioNectar)

print(STOREShoney(t))

#--------------------------------------------------------------#

#Result in kilogramme
def WEIGHTcolony(t):
    # All the w varaible are in g

    #Represente the weight of the hive
    w_hivebase = 14000 #from Frisch, 1927; Stabe, 1930; Wang, 1965; Camazine et al., 1990).
    
    #represents the weight of one empty cell (wax only).
    w_cellsbase = 0.037

    # The three next w variable represent one cell filled with the given resource respectively
    w_pollen = 0.23
    w_nectar = 0.43
    w_honey = 0.5

    #The three next w variable represent the weight of a bee un the given stage
    w_egg = 0.0001
    w_pupa = 0.16
    #represent the weight of a larva in age i ∈ {1,2,3,4,5}
    w_larva = [0.0002,0.00059,0.00331,0.0644,0.160]
    w_adult = 0.1
    
	somme_res = 0
	for i in range (1, LIFESPANlarva) :
			sum_res += w_larva(i) * LARVAE(i,t)
	return sum_res

    return 1/1000 * (w_hivebase + (w_cellsbase * CELLShive) + (w_pollen * STORESpollen(t)) + (w_nectar * STORESnectar(t)) + (w_honey * STOREShoney(t)) + (w_egg * CELLSegg(t)) + (w_pupa * CELLSpupae(t)) + somme_res + w_adult * BEESadult(t) )

print(WEIGHTcolony(t))

#--------------------------------------------------------------#

def BEESlazy(t):
    FACTORothertasks = 0.2
    return (BEESadult(t)*(1-FACTORothertasks))-FORAGERSactive(t)-NURSES(t)-PROCESSORS(t)

print(BEESlazy(t))

#--------------------------------------------------------------#