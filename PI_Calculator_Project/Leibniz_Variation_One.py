
#After searching for a formula which models what I have made here, I couldn't find anything. 
#But here is another program which finds pi. 

import math

multiplication_constant = 1/(math.sqrt(3))

denom_mult = 3
denom_constant = 3
pi_part = 1
denom_step = 2
denom_exp = 1
while True:
    
    pi_part -= 1/(denom_mult*(math.pow(denom_constant, denom_exp))) 
    
    denom_mult += denom_step
    denom_exp += 1
    pi_part += 1/(denom_mult*(math.pow(denom_constant, denom_exp)))
    denom_mult += denom_step
    denom_exp += 1
    print(6/(math.sqrt(3)) * (pi_part))
    