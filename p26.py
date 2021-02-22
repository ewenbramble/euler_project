# Project Euler
# Problem 26
# Solution by Ewen Bramble

# Find the value of d < 1000 for which 1/d contains the
# longest recurring cycle in its decimal fraction part

def recurring_cycles(num,den):
    '''Function to take a numerator and denominator and return a decimal
    with recurring aspects in parenthesis'''
    
    # First some checks:
    if den == 0: # check if denominator = 0
        return 'Undefined'
    if num == 0: # check if numerator = 0
        return 0
    if num%den == 0: # check if numbers are evenly divisible
        return str(num/den)
    negative = False
    if num < 0 or den < 0: # check if one of numerator/denominator is negative
        negative = True
        
    numerator = abs(num) # in case negative
    denominator = abs(den)
        
    output = "" # initialise output string
    if negative:
        output += "-"
    whole_number = str(numerator//denominator) # floor division for integer/integram part of output
    output += whole_number
    output += "." # decimal point
    
    num_q = [] # initialise list for numerator quotient pairs
    while True:
        rem = numerator%denominator # find remainder
        if rem == 0: # if there is no remainder, we are finished
            for element in num_q:
                output += str(element[1])
            break
        numerator = rem * 10 # new numerator is remainder * 10
        q = numerator // denominator # find quotient with new numerator
        
        if [numerator,q] not in num_q:
            num_q.append([numerator,q])
        elif [numerator,q] in num_q: # we have found a repeating pattern
            index = num_q.index([numerator,q]) # we need the index where recurring pattern starts
            for i in range(index): # iterate through list until recurrence index, append to string before parenthesis
                output+=str(num_q[i][1])
            
            
            output += "("
            for i in range(index,len(num_q)): # iterate through list from recurrence index, append to string in parenthesis
                output+=str(num_q[i][1])
            output += ")"
            break
    return output

# --------
# MODIFIED VERSON OF ABOVE to find length of recurring pattern
# --------

def len_recurring_cycles(num,den):
    '''Function to take a numerator and denominator and returns length recurring aspect'''
    
    # First some checks:
    if den == 0: # check if denominator = 0
        return 'Undefined'
    if num == 0: # check if numerator = 0
        return 0
    if num%den == 0: # check if numbers are evenly divisible
        return str(num/den)
    negative = False
    if num < 0 or den < 0: # check if one of numerator/denominator is negative
        negative = True
        
    numerator = abs(num) # in case negative
    denominator = abs(den)
        
    num_q = [] # initialise list for numerator quotient pairs
    length = 0 # initialise length of recurring aspect
    while True:
        rem = numerator%denominator # find remainder
        
        if rem == 0: # if there is no remainder, we are finished
            break
        
        numerator = rem * 10 # new numerator is remainder * 10
        q = numerator // denominator # find quotient with new numerator
        
        if [numerator,q] not in num_q:
            num_q.append([numerator,q])
        elif [numerator,q] in num_q: # we have found a repeating pattern
            index = num_q.index([numerator,q]) # we need the index where recurring pattern starts
            length = len(num_q) - index
            break
            
    return length

max_length = 0
denominator = 2
for d in range(2,1000):
    length = len_recurring_cycles(1,d)
    if length > max_length:
        max_length = length
        denominator = d
print("Max length of recurring decimal cycle is: {} for denominator: {}".format(max_length,denominator))