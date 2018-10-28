T = int(input()) # number of test cases

for i in range(T):
    N = int(input()) # number of items
    W = int(input()) # the maximum capacity of the knapsack
    Vals = list(input()) # a list of item values
    Wei = list(input()) # a list of item weights



#%%
vals = [1,2,3,4]
type(vals[1])

W = 3.5
Vals = [1,2,3,4]
Wei = [1,1,1,1]
A = [[0]*(W+1)]

A[-1][1]

for i in range(len(Vals)):
    F = []
    for j in range(W+1):



def KS(n,W):
    # n: the pointer
    # W: the total capacity
    if n==0 or W==0:
        result = 0
    else if w[n]>W:
        result = KS(n-1,W)
    else:
        tmp1 = KS(n-1, W) # dont't put the nth item in the knapsack
        tmp2 = v[n] + KS(n-1, W-w[n]) # put the nth item in the knapsack
        result = max(tmp1,tmp2)
    return result
