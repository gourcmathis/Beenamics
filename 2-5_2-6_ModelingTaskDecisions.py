
LIFESPANlarva=5

FACTORothertasks=0.2

def NEEDworkers(t):
	return NEEDnurses(t)+NEEDpollenforagers(t)

def RATIOworkforce(t):
	ratio=(BEESadult(t)*(1-FACTORothertasks))/(NEEDworkers(t)+1)
	if ratio<1:
		return ratio
	else:
		return 1

def NEEDnurses(t):
	total=0
	for i in range(1,LIFESPANlarva+1):
		total+=LARVAE(i,t)*NEEDnurses_per_larva(i)

	return total+(CELLSeggs(t)*NEEDnurses_per_egg)+(CELLSpupae(t)*NEEDnurses_per_pupa)

def NURSES(t):
	return NEEDnurses(t)*RATIOworkforce(t)

def INDEXnursingquality(t):
	return NURSES(t)/(NEEDnurses(t)+1)