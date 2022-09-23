#This program is based on Euler's basic pi formula series. 
#The formula: Infinite series starting at n = 1 of (1/(n^2)). This infinite summation is equal to (pi)^2/6.

"""
If this program had an infinite ram source, then it would calculate the exact value of pi. 
"""





import math 

#pi^2/6 = sigma 1/n^2


demominator = 1 #the "n" value : starting at the value of 1;
EXP = 2 #constant exponent. 
pi_part = 0 #starting value of pi
while True:
    pi_part += 1/(math.pow(demominator, EXP))
    demominator += 1    #basically the next value of n. 
    
    
    """
    This next part calculates the value of pi as it is in the program every iteration.
    """
    pi = math.sqrt(pi_part * 6) #isolates the value of pi in the equation. 
    print(pi)
    
    
    
    
    #How useful is this program: not at all since we already can use an almost exact value of pi with math.pi but
    #it is interesting to understand how we even know what the value of pi is with certainty. 
    #This is not the only method to calculate the value of pi, but one of the simplest, yet not the most efficient. 