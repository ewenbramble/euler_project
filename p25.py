# Project Euler
# Problem 25
# Solution by Ewen Bramble

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from collections import deque
def fib_seq_gen2(limit):
    '''Generates a Fibonacci Sequence until number is of specified length'''
    count = 2 # Index counter starting at index 2 as we initialise the sequence with the first 2 elements
    seq = deque([1,1])
    
    while True:
        new_num = (seq[-1]+seq[-2])
        
        count += 1
        seq.popleft()
        seq.append(new_num)
        last_num = seq[-1]
        
        if len(str(last_num)) == limit: # End when reach num of specified length
            break
    print('First {}-length number in Fibonacci sequence is: {}'.format(limit, last_num))
    print('Index of this number: {}'.format(count))

if __name__ == '__main__':
    print(fib_seq_gen2(1000))