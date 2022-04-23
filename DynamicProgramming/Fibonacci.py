def fibonacci(n):
    f = []
    f = [0, 1]
    for i in range(2, n+1):
        res = f[i - 1] + f[i - 2]
        f.append(res)
    return f[n]


# Fibonacci using memoization
def fibMemoization(n, lookup):
    # Add the base case for 0 and 1 i.e lookup[0]=0 and lookup[1]=1
    if n <= 1:
        lookup[n] = n
    # Check the lookup array if the computed value is already there or not
    if lookup[n] is None:
        lookup[n] = fibMemoization(n - 1, lookup) + fibMemoization(n - 2, lookup)
    # return the fibonacci of the number
    return lookup[n]


num = int(input("Enter the number for fibonacci:\n"))
value = fibonacci(num)
print("Fibonacci of number", num, "is:", value)
# for Memoization
lookup = [None]*100
fib = fibMemoization(num, lookup)
print("Fibonacci of number", num, "using Memoization is:", fib)
