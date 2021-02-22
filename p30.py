# Project Euler
# Problem 30
# Solution by Ewen Bramble

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

nums = []
for n in range(1000000):
    str_num = str(n)
    sum_powers = 0
    for digit in str_num:
        sum_powers += int(digit)**5
    if sum_powers == n:
        nums.append(n)
print(nums)