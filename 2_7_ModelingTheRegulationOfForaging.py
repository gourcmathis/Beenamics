FACTORpollenstorage = 6
FACTORminpollenforagers = 0.01

#----------------------------------------------------------------------------------------------------------------------#
# Name : FORAGERS(t)
# Author : Guillaume Proton
# Date : 28/12/2020
#
# Description : Calcule le nombre de butineuses potentielles
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def FORAGERS(t):
	return FORAGERSpollen(t) + FORAGERSnectar(t)


#----------------------------------------------------------------------------------------------------------------------#
# Name : FORAGERSactive(t)
# Author : Guillaume Proton
# Date : 28/12/2020
#
# Description : Calcule le nombre de butineuses qui sortent de la ruche
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def FORAGERSactive(t):
	return FORAGERSpollenactive(t) + FORAGERSnectaractive(t)

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDpollen_larvae(t)
# Author : Guillaume Proton
# Date : 28/12/2020
#
# Description : Calcule le besoin en pollen de la part des larves
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDpollen_larvae(t):
	res = 0
	for i in range(1,LIFESPANlarva+1):
		res = res + POLLENNEEDlarva(i)*LARVAE(i,t)
	return res

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDpollen_adult(t)
# Author : Guillaume Proton
# Date : 28/12/2020
#
# Description : Calcule le besoin en pollen de la part des abeilles adultes
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDpollen_adult(t):
	return BEESadult(t)*POLLENNEEDadult + NURSES(t)*POLLENNEEDnurse

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDpollenincome(t)
# Author : Guillaume Proton
# Date : 28/12/2020
#
# Description : Calcule le besoin journalier en pollen
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDpollenincome(t):
	acc = 0
	for d in range(0,3):
		acc = acc + NEEDpollen(t-d)
	acc = acc/3
	acc = acc * FACTORpollenstorage - STORESpollen(t)
	return max(0, acc)

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDpollenforagers(t)
# Author : Guillaume Proton
# Date : 28/12/2020
#
# Description : Calcule le nombre de butineuses de pollen requis
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDpollenforagers(t):
	return (NEEDpollenincome(t-1) / (LOADpollenforager*TURNpollenforager*FACTORforagingsuccess))

#----------------------------------------------------------------------------------------------------------------------#
# Name : FORAGERSpollen(t)
# Author : Guillaume Proton
# Date : 29/12/2020
#
# Description : Calcule le nombre potentiel de butineuses de pollen
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def FORAGERSpollen(t):
	maximum = max(NEEDpollenforagers(t)*RATIOworkforce(t), (BEESadult(t)-NURSES(t))*FACTORminpollenforagers )
	return min(maximum, BEESadult(t)*FACTORforagingmax)

#----------------------------------------------------------------------------------------------------------------------#
# Name : FORAGERSpollenactive(t)
# Author : Guillaume Proton
# Date : 29/12/2020
#
# Description : Calcule le nombre de butineuses de pollen qui sortent de la ruche
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def FORAGERSpollenactive(t):
	return FORAGERSpollen(t)*INDEXflight(t)*INDEXpollenoutside(t)

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDnectar(t)
# Author : Guillaume Proton
# Date : 29/12/2020
#
# Description : Calcule le besoin journalier en nectar de la ruche
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDnectar(t):
	return NEEDnectar_larvae(t) + NEEDnectar_adult(t)

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDnectar_larvae(t)
# Author : Guillaume Proton
# Date : 29/12/2020
#
# Description : Calcule le besoin en nectar de la part des larves
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDnectar_larvae(t):
	acc = 0
	for i in range(1,LIFESPANlarva+1):
		acc = acc + (NECTARNEEDlarva(i)*LARVAE(i,t))
	return acc

#----------------------------------------------------------------------------------------------------------------------#
# Name : NEEDnectar_adult(t)
# Author : Guillaume Proton
# Date : 29/12/2020
#
# Description : Calcule la demande en nectar de la part des abeilles adultes
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def NEEDnectar_adult(t):
	# Besoin en nectar pour les abeilles adultes
	nectar_adults = BEESadult(t)*NECTARNEEDadult

	# Besoin en nectar pour les abeilles infirmières
	nectar_nurses = NURSES(t)*NECTARNEEDnurse

	# Besoin en nectar pour les butineuses actives
	nectar_foragers = FORAGESactive(t)*NECTARNEEDactiveforager
	
	# Retourne la demande totale en nectar de la part des abeilles adultes
	return nectar_adults+nectar_nurses+nectar_foragers

#----------------------------------------------------------------------------------------------------------------------#
# Name : WORKFORCEnectar(t)
# Author : Guillaume Proton
# Date : 29/12/2020
#
# Description : Calcule la force de travail restante pour le nectar
# Variable : t
# Variation : t peut prendre les valeurs de 1 à 365 -> numéro du jour dans l'année
#----------------------------------------------------------------------------------------------------------------------#
def WORKFORCEnectar(t):
	if RATIOworkforce(t)==1:
		res = BEESadult(t)*(1-FACTORothertasks)
		return res-NURSES(t)-FORAGERSpollen(t)
	else:
		return 0






