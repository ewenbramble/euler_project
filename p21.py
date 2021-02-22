# Project Euler
# Problem 21
# Solution by Ewen Bramble

# Sum of amicable numbers under 10000
# Two numbers are amicable if the sum of divisors is the same as the other number

def sum_of_divisors(n):
    '''Returns sum of proper divisors of a number n'''
    divisor_list = []
    for i in range(1,int(n/2)+1): # only need to check up to half the value of n
        if n%i == 0:
            divisor_list.append(i)
    return sum(divisor_list)

# Make a list of tuples where each is a pair: (number, sum-of-divisors)

divisor_tuples = []
for i in range(1,10000):
    div_sum = sum_of_divisors(i)
    if div_sum != i: # Don't need num/sum-divisor pairs (a,b) where a = b as they will not be amicable numbers
        divisor_tuples.append((i,div_sum))
    
# Iterate over list of tuples, find amicable numbers (in this case, tuple pairs in list where a,b = b,a)
amicable_numbers = []
for i in range(len(divisor_tuples)):
    for j in range(1,len(divisor_tuples)):
        if divisor_tuples[i][0] == divisor_tuples[j][1] and divisor_tuples[i][1] == divisor_tuples[j][0]:
            amicable_numbers.append(divisor_tuples[i])

flat_amicable_numbers = [e for l in amicable_numbers for e in l] # Flatten tuples into 1-d list
flat_amicable_numbers = set(flat_amicable_numbers) # Remove duplicate numbers so we don't count them twice

print('The sum of all amicable numbers under 10000 is: {}'.format(sum(flat_amicable_numbers)))