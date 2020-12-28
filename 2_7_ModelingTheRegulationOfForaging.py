# Constants :

# Honey bees always have a small pollen reserve stored
# inside the hive. A value of FACTORpollenstorage = 6 
# means that the modeled colony regulates the pollen 
# stores around a level that represents a reserve for
# approximately 6 days,
FACTORpollenstorage = 6

# In nature, there is always a certain minimum number
# of pollen foragers within the cohort of foragers.
# The constant parameter FACTORminpollenforagers 
# expresses this predisposition of some bees for pollen
# foraging.
FACTORminpollenforagers = 0.01


# Models the daily number of potential foragers as 
# the sum of potential pollen foragers and
# potential nectar foragers. It reprensents the
# available workforce for the foraging task.
# Parameter :
#	t : day number
def FORAGERS(t):
	return FORAGERSpollen(t) + FORAGERSnectar(t)


# Calculate the actual number of foragers that fly out
# Parameter :
#	t : day number
def FORAGERSactive(t):
	return FORAGERSpollenactive(t) + FORAGERSnectaractive(t)


# Returns the pollen demands of the larvae of all ages (i)
# Parameter :
#	t : day number
def NEEDpollen_larvae(t):
	res = 0
	for i in range(1,LIFESPANlarva+1):
		res = res + POLLENNEEDlarva(i)*LARVAE(i,t)
	return res

# The adult’s pollen demand is calculated by adding the 
# basic daily pollen demand of adult bees (a constant, 
# POLLEN-NEEDadult) and an additional daily pollen demand
#of nursing bees (a constant, POLLENNEEDnurse).
# Parameter :
#	t : day number
def NEEDpollen_adult(t):
	return BEESadult(t)*POLLENNEEDadult + NURSES(t)*POLLENNEEDnurse

# Returns the daily need for pollen income. We use a 
# gliding average throughout 3 days (d goes from 0 to 2) 
# to model the needed pollen income.
# Parameter :
#	t : day number
def NEEDpollenincome(t):
	acc = 0
	for d in range(0,3):
		acc = acc + NEEDpollen(t-d)
	acc = acc/3
	acc = acc * FACTORpollenstorage - STORESpollen(t)
	return max(0, acc)

# calculate the needed number of pollen foragers 
# NEEDpollenforagers(t).
# LOADpollenforager is the amount of pollen collected 
# per foraging trip; expressed in the unit “cellfuls”
# TURNSpollenforager is the number of trips performed 
# per forager per day
# Parameter :
#	t : day number
def NEEDpollenforagers(t):
	return (NEEDpollenincome(t-1) / (LOADpollenforager*TURNpollenforager*FACTORforagingsuccess))

# Models the potential number of pollen foragers 
# each day.
# Parameter :
#	t : day number
def FORAGERSpollen(t):
	maximum = max(NEEDpollenforagers(t)*RATIOworkforce(t), (BEESadult(t)-NURSES(t))*FACTORminpollenforagers )
	return min(maximum, BEESadult(t)*FACTORforagingmax)

# Models the number of fragers that actually leave the 
# hive for foraging flights. It depends on two
# environmental factors : INDEXflight(t) expresses the 
# weather situation each day and INDEXpollenoutside(t)
# expresses the botanical pollen availability each day.
# Parameter :
#	t : day number
def FORAGERSpollenactive(t):
	return FORAGERSpollen(t)*INDEXflight(t)*INDEXpollenoutside(t)

# Models the demand for nectar (quite similar to the 
# pollen demand with the additional complication that
# the active foragers are also important nectar 
# consumers).
# Parameter :
#	t : day number
def NEEDnectar(t):
	return NEEDnectar_larvae(t) + NEEDnectar_adult(t)

# Returns the nectar demands of the larvae of all ages (i)
# Parameter :
#	t : day number
def NEEDnectar_larvae(t):
	acc = 0
	for i in range(1,LIFESPANlarva+1):
		acc = acc + (NECTARNEEDlarva(i)*LARVAE(i,t))
	return acc

# Returns the nectar demands of adult bees
# Parameter :
#	t : day number
def NEEDnectar_adult(t):
	# nectar needed for adult bees
	nectar_adults = BEESadult(t)*NECTARNEEDadult

	# nectar needed for nurses
	nectar_nurses = NURSES(t)*NECTARNEEDnurse

	# nectar needed for active foragers
	nectar_foragers = FORAGESactive(t)*NECTARNEEDactiveforager
	
	# Returns the nectar demands of adult bees
	return nectar_adults+nectar_nurses+nectar_foragers

# Because the number of available workers could already 
# be recruited for the high-priority jobs “nursing” and 
# “pollen foraging” (RATIOworkforce < 1), it is 
# necessary to limit WORFORCEnectar(t) to non-negative 
# values.
# Parameter :
#	t : day number
def WORKFORCEnectar(t):
	if RATIOworkforce(t)==1:
		res = BEESadult(t)*(1-FACTORothertasks)
		return res-NURSES(t)-FORAGERSpollen(t)
	else
		return 0





