# calculates pi with the leibniz method. 

#this program is based off of the leibniz formula for pi. 

#The formula : pi/4 = the infinite alternating series of 1/(2n + 1)

pi_part = 1 #Just the first term in the series. 
INIT_DENOM = 3 #The first denominator of a "fraction" in the series. 
ALTERNATOR = 2 #The maginitude of the denominator is changing by this amount

while True:
    
    #############
    pi_part -= (1/INIT_DENOM)
    INIT_DENOM += ALTERNATOR
    #############
    #These two sections are for the alternating signs
    #############
    pi_part +=(1/INIT_DENOM)
    INIT_DENOM += ALTERNATOR
    #############
    
    print(pi_part * 4) #pi_part is just pi/4. 