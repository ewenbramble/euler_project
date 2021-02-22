# Project Euler
# Problem 18 & 67
# Solution by Ewen Bramble

# Find the maximum total from top to bottom of the triangle given (text file)

# Working bottom to top, calculate maximum sum of adjacent numbers between lowest two rows
# Replace these rows with a new row containing maximum adjacent sums, and continue upward
# When only one row remains, this will be the maximum sum

# Read in triangle from text file
def triangle_to_list(text_file):
    '''Takes a txt file containing numbers separated by spaces, returns list of lists, one for each triangle row'''
    triangle_list = []
    with open(text_file, 'r') as file:
        for line in file:
            line_list = line.split()
            map_object = map(int,line_list) # strings to integers
            triangle_list.append(list(map_object))
    return triangle_list

def best_sum(last_row, second_last_row):
    '''Takes two lists, the first being one item longer than the 2nd (consecutive rows in a triangle).
    Returns a single list with the max sum of adjacent numbers between these two lists (triangle rows)'''
    sum_list = []
    for i in range(len(second_last_row)):
        max_sum = second_last_row[i]+last_row[i] #initialise max_sum as numbers with same index
        if second_last_row[i]+last_row[i+1] > max_sum: #check if other adjacent number results in greater sum
            max_sum = second_last_row[i]+last_row[i+1]
        sum_list.append(max_sum)
    return sum_list

# Main function
def triangle_max_path_sum(text_file):
    '''Computes the maximum total working from top to bottom of a triangle'''
    
    tri_list = triangle_to_list(text_file) # grab text file of triangle numbers   
    
    while len(tri_list) > 1:
        last_row = len(tri_list)-1 # index of bottom row of triangle in triangle list
        second_last_row = last_row - 1 # index of second bottom row in triangle list
        new_bottom_row = best_sum(tri_list[last_row], tri_list[second_last_row]) # new base of triangle computed
        tri_list = tri_list[:(len(tri_list)-2)] # remove bottom two rows now that maximum sum calculated
        tri_list.append(new_bottom_row) # add new bottom row being the maximum sum of adjacent numbers
            
    print("The maximum adjacent path sum is: {}".format(tri_list[0][0]))