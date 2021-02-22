# Project Euler
# Problem 20
# Solution by Ewen Bramble

# Find sum of digits in the number 100!

def factorial(n):
    '''Returns factorial of input number n'''
    factorial = 1
    if n < 0: # check for negative input
        print("Sorry, number must be 0 or greater")
    elif n == 0: # check if n is zero
        return factorial
    else:
        for i in range(1, n+1):
            factorial = factorial*i
        return factorial

result = 0
for num in str(factorial(100)):
    result += int(num)
print(result)
