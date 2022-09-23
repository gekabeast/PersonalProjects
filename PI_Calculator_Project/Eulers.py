import math

#pi^2/6 = sigma 1/n^2
demominator = 1
exp = 2
pi_part = 0
while True:
    pi_part += 1/(math.pow(demominator, exp))
    demominator += 1
    pi = math.sqrt(pi_part * 6)
    print(pi)