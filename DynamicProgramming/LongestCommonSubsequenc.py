def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # Using tabulation here creating a table for all entries.
    # L = [[0]*(n+1) for i in range(m+1)]
    L = [[-1] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            # if last character of string matches
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            # if not matches take this
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


X = 'AGGTAB'
Y = 'GXTXAYB'

# length = lcs(X, Y)
# print("Length of common subsequence in string", X, 'and in string', Y, 'is:', length)


# A Naive recursive Python implementation of LCS problem


def LCS(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + LCS(X, Y, m - 1, n - 1)
    else:
        return max(LCS(X, Y, m, n - 1), LCS(X, Y, m - 1, n))


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCS(X, Y, len(X), len(Y)))
