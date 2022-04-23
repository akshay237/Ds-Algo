def knapsack(W, wt, val, n):
    k = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            # if capacity of bag is zero and we don't have any weight also
            if i == 0 or w == 0:
                k[i][w] = 0
            # suppose if capacity of bag is 1 than we can take that weight or we can leave it but we wan't maximum profit.
            # the weight we are picking is less than or equal to the bag's capacity.
            elif wt[i - 1] <= w:
                k[i][w] = max(k[i-1][w], val[i-1] + k[i-1][w-wt[i-1]])
            # if weight is more than we can't put that in the bag so take profit from above iteration
            else:
                k[i][w] = k[i-1][w]
    # return the last value of 2-D matrix that hae maximum profit.
    return k[n][W]


W = 10
wt = [1, 3, 4, 6]
val = [20, 30, 10, 50]
n = len(val)
profit = knapsack(W, wt, val, n)
print("The maximum profit earned by the thief is:", profit)