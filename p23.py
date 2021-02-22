# Project Euler
# Problem 23
# Solution by Ewen Bramble

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
# Upper limit to check: 28123

def sum_of_divisors(n):
    '''Returns sum of proper divisors of a number n'''
    divisor_list = []
    for i in range(1,int(n/2)+1): # only need to check up to half the value of n
        if n%i == 0:
            divisor_list.append(i)
    return sum(divisor_list)

def check_abundant(n):
    '''Takes a number n and returns True if abundant (sum of its proper divisors greater than n)'''
    divisor_sum = sum_of_divisors(n)
    if divisor_sum > n:
        return True
    else:
        return False

# 12 is smallest abundant number, so only need to find abundant numbers up to 28123-12 = 29111
abundant_numbers = []
for i in range(12,28112):
    if check_abundant(i):
        abundant_numbers.append(i)

# Numbers that can be written as the sum of two abundant numbers
abundant_sums = []
for j in range(len(abundant_numbers)):
    for k in range(len(abundant_numbers)):
        result = abundant_numbers[j]+abundant_numbers[k]
        if result<28124 and result not in abundant_sums:
            abundant_sums.append(result)

# Numbers that cannot be written as the sum of two abundant numbers are not in above list
non_abundant_sums = []
for i in range(1,28124): # positive integers. Given information is that all nums>28123 can be written as sum of
                            # two abundant numbers
        if i not in abundant_sums:
            non_abundant_sums.append(i)
result = sum(non_abundant_sums)
print(f'The sum of positive integers that cannot be written as the sum of two abundant nums is: {result}')