# calculates pi 

pi_part = 1
denominator = 3
alternator = 2

while True:
    pi_part -= (1/denominator)
    denominator += alternator
    pi_part +=(1/denominator)
    denominator += alternator
    print(pi_part * 4)