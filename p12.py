# Project Euler
# Problem 12
# Solution by Ewen Bramble

# What is the value of the first triangle number
# to have over five hundred divisors?


import math
def find_factors(n):
    '''Finds factors of n'''
    factors = []
    i = 1
    while i <= math.sqrt(n):
        if n%i == 0:
            # if divisors equal, list only one
            if n/i == i:
                factors.append(i)
            else:
                #otherwise print both
                factors.append(n/i)
                factors.append(i)
        i+=1
    return factors

result = 0
tri_num = 1
x = 2

while True:
    factors = find_factors(tri_num)
    if len(factors)>500:
        break
    else:
        tri_num += x
        x += 1

print(tri_num)