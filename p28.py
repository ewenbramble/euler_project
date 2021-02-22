# Project Euler
# Problem 28
# Solution by Ewen Bramble

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?

# Idea: write function to populate grid from middle outward. Function takes dimension(s)
# Grid full of zeros initially
# Turn right if zero in grid, else go straight
# While loop with total number of 'moves' being num squares in grid
# Keep track of index at end of each iteration, direction also

def make_zero_grid(size):
    '''Returns a square grid, size x size populated with zeros as a list of lists'''
    out_list = []
    for x in range(size):
        out_list.append([0 for x in range(size)])
    return out_list

grid_size = 1001
num_squares = (grid_size*grid_size) # size of grid
starting_square_index = int((grid_size-1)/2) # index of starting square, both outer/inner lists

index_row = starting_square_index # initialise row index
index_col = starting_square_index # initialise column index

grid = make_zero_grid(grid_size) # make grid of zeros
grid[starting_square_index][starting_square_index] = 1 # start with 1 in centre of grid
grid[starting_square_index][starting_square_index+1] = 2

index_col += 1 # first move to the right

n = 3 # keep track of moves
direction = 1 # keep track of direction, initially 'heading right'. 1 = R, 2 = Down, 3 = L, 4 = Up

while n <= num_squares:

    while direction == 1: # right
        if grid[index_row + 1][index_col] == 0: # checking if below square is 0 (can turn right)
            grid[index_row + 1][index_col] = n # write next number to square
            n += 1
            index_row += 1 # we are now one row lower
            direction = 2 # now heading down
        else: # can't turn right, so move straight and write to square
            try:
                grid[index_row][index_col + 1] = n
            except: # if out of range error
                break
            else:
                n += 1
                index_col += 1 

    while direction == 2: # down
        if grid[index_row][index_col-1] == 0: # checking if left square is 0 (can turn right)
            grid[index_row][index_col-1] = n # write next number to square
            n += 1
            index_col -= 1 # we are now one column left
            direction = 3 # now heading left
        else: # can't turn right, so move straight and write to square
            try:
                grid[index_row+1][index_col] = n
            except:
                break
            else:
                n += 1
                index_row += 1

    while direction == 3: # left
        if grid[index_row-1][index_col] == 0: # checking if above square is 0 (can turn right)
            grid[index_row-1][index_col] = n # write next number to square
            n += 1
            index_row -= 1 # we are now one row higher
            direction = 4 # now heading up
        else: # can't turn right, so move straight and write to square
            try:
                grid[index_row][index_col-1] = n
            except:
                break
            else:
                n += 1
                index_col -= 1

    while direction == 4: # up
        if grid[index_row][index_col+1] == 0: # checking if right square is 0 (can turn right)
            grid[index_row][index_col+1] = n # write next number to square
            n += 1
            index_col += 1 # we are now one column right
            direction = 1 # now heading right
        else: # can't turn right, so move straight and write to square
            try:
                grid[index_row-1][index_col] = n
            except:
                break
            else:
                n += 1
                index_row -= 1
            
# SUM DIAGONALS
# Plan: work inward from top to row above middle row, then work bottom up similarly. Add these to 1 (middle num)

def sum_diagonals(grid):
    '''Function returns sum of diagonal numbers in grid (list of lists)
    excluding centre square (1 in spiral grid)'''
    half_list_size = int((len(grid)-1)/2) # Need the number of rows in half the grid minus the middle row
    
    total = 0
    
    # Top half of grid
    # Indexes for each row to work inward from each side
    left_index = 0
    right_index = -1

    for i in range(half_list_size): # iterate row by row downward
        total += grid[i][left_index]
        total += grid[i][right_index]
        left_index += 1 # move inward for following row
        right_index -= 1
        
    # Bottom half of grid
    left_index = 0 # Reset indexes
    right_index = -1
    
    for i in range((len(grid)-1),(len(grid)-1)-half_list_size,-1): # iterate backward from bottom
        total += grid[i][left_index]
        total += grid[i][right_index]
        left_index += 1 # move inward for following row
        right_index -= 1
        
    total += 1 # add 1 for centre square
    return total

print("The sum of diagonals in 1001x1001 spiral grid is: {}".format(sum_diagonals(grid)))