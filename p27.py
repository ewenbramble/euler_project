# Project Euler
# Problem 27
# Solution by Ewen Bramble

# Find the product of the coefficients, a and b for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting with n=0

# need a function to check if result of quadratic function is prime for consecutive values of n
def check_if_prime(n):
    '''Function that returns True if n is a prime number'''
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

# counters
max_prime_count = 0 # running tally of number of primes for consecutive n values
max_a = 0 # value of a for the number of primes
max_b = 0 # value of b for the number of primes

for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0
        prime_count = 0 # count primes for each combination of a and b
        while True: # loop until non-prime result from quadratic function
            result = n**2 + a*n + b
            if check_if_prime(result): # Check if prime
                n+=1 # try next n
                prime_count += 1 # add to prime counter             
            else:
                if prime_count > max_prime_count:
                    max_prime_count = prime_count
                    max_a = a
                    max_b = b
                break

product = max_a * max_b # product of coefficients a and b

print(f"Maximum number of consecutive primes: {max_prime_count}")
print(f"Coefficient a: {max_a}")
print(f"Coefficient b: {max_b}")
print(f"Product of coefficients a and b: {product}")
