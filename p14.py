# Project Euler
# Problem 14
# Solution by Ewen Bramble

# Which starting number, under one million, produces the longest Collatz Sequence chain?

max_chain_len = 0
max_num = 1

n = 2 # starting number
while n < 1000000:
    chain = [n]
    while chain[-1] != 1:   
        if chain[-1]%2 == 0: #check if even
            chain.append(int(chain[-1]/2))
        else:
            chain.append(int(3*chain[-1]+1))
        
        # check if current chain is longest
        if len(chain) > max_chain_len:
            max_chain_len = len(chain)
            max_num = n
        
    n+=1
print(max_num)