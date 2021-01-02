FACTORpollenstorage = 6
FACTORminpollenforagers = 0.01


# Nombre de butineuses potentielles
def FORAGERS(t):
	return FORAGERSpollen(t) + FORAGERSnectar(t)


# Nombre de butineuses qui sortent de la ruche
def FORAGERSactive(t):
	return FORAGERSpollenactive(t) + FORAGERSnectaractive(t)


# Demande en pollen de la part des larves
def NEEDpollen_larvae(t):
	res = 0
	for i in range(1,LIFESPANlarva+1):
		res = res + POLLENNEEDlarva(i)*LARVAE(i,t)
	return res

# Demande en pollen de la part des abeilles adultes
def NEEDpollen_adult(t):
	return BEESadult(t)*POLLENNEEDadult + NURSES(t)*POLLENNEEDnurse

# Besoin journalier en pollen
def NEEDpollenincome(t):
	acc = 0
	for d in range(0,3):
		acc = acc + NEEDpollen(t-d)
	acc = acc/3
	acc = acc * FACTORpollenstorage - STORESpollen(t)
	return max(0, acc)

# Nombre de butineuses de pollen requis
def NEEDpollenforagers(t):
	return (NEEDpollenincome(t-1) / (LOADpollenforager*TURNpollenforager*FACTORforagingsuccess))

# Nombre potentiel de butineuses de pollen
def FORAGERSpollen(t):
	maximum = max(NEEDpollenforagers(t)*RATIOworkforce(t), (BEESadult(t)-NURSES(t))*FACTORminpollenforagers )
	return min(maximum, BEESadult(t)*FACTORforagingmax)

# Nombre de butineuses de pollen qui sortent de la ruche
def FORAGERSpollenactive(t):
	return FORAGERSpollen(t)*INDEXflight(t)*INDEXpollenoutside(t)

# Besoin journalier en pollen
def NEEDnectar(t):
	return NEEDnectar_larvae(t) + NEEDnectar_adult(t)

# Demande en nectar de la part des larves
def NEEDnectar_larvae(t):
	acc = 0
	for i in range(1,LIFESPANlarva+1):
		acc = acc + (NECTARNEEDlarva(i)*LARVAE(i,t))
	return acc

# Demande en nectar de la part des abeilles adultes
def NEEDnectar_adult(t):
	# Besoin en nectar pour les abeilles adultes
	nectar_adults = BEESadult(t)*NECTARNEEDadult

	# Besoin en nectar pour les abeilles infirmières
	nectar_nurses = NURSES(t)*NECTARNEEDnurse

	# Besoin en nectar pour les butineuses actives
	nectar_foragers = FORAGESactive(t)*NECTARNEEDactiveforager
	
	# Retourne la demande totale en nectar de la part des abeilles adultes
	return nectar_adults+nectar_nurses+nectar_foragers

#Force de travail restante pour le nectar
def WORKFORCEnectar(t):
	if RATIOworkforce(t)==1:
		res = BEESadult(t)*(1-FACTORothertasks)
		return res-NURSES(t)-FORAGERSpollen(t)
	else:
		return 0






