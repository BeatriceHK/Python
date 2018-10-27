#%% Maximum height of the staircase problem 
T = int(input()) # number of test cases

for i in range(T):
    N = int(input()) # number of blocks
    k = 1
    sum = 1
    height = 0
    while(sum <= N):
        k += 1
        sum += k
        height += 1
    print(height)
