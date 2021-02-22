# Project Euler
# Problem 22
# Solution by Ewen Bramble

# Name scores (alphabetic value of name multiplied by its sorted position in name list)
# What is the total of the name scores in the given file (comma-separated names)

def alpha_value(string):
    '''Takes a string and returns its alphabetic value'''
    value = 0
    for char in string:
        if char.isalpha(): # check character is alphabetic
            value += ord(char.lower())-96 # use lower-case for ordinal function so that both a and A = 1
        else:
            pass
    return value
        
# Make list of names from text file
with open('p022_names.txt', 'r') as file:
    for line in file:
        name_list = line.split(',')

# Remove " characters from each name
clean_names = [name.replace('"','') for name in name_list]

# Sort list alphabetically
clean_names.sort()

# Iterate over list of names, call alphabetic value function on each name, multiply by list index+1
# and add to score
name_score = 0
for i in range(len(clean_names)):
    name_score += (alpha_value(clean_names[i]) * (i+1))
print("The name score of this list of names is: {}".format(name_score))