global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()


def isSafe(board, row, col):
    for i in range(row):
        # Check the current row if already some queen placed or not
        if board[i][col] == 1:
            return False
    # check the diagonals '\'
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # (i, j) = (row, col)
    # while i >= 0 and j >= 0:
    #     if board[i][j] == '1':
    #         return False
    #     i = i - 1
    #     j = j - 1

    # Check the diagonal '/'
    for i, j in zip(range(row, 0, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False
    # (i, j) = (row, col)
    # while i >= 0 and j < N:
    #     if board[i][j] == '1':
    #         return False
    #     i = i - 1
    #     j = j + 1

    return True


def solveNQUtil(board, row):
    # base condition if we reached to the last row that means all queens are placed
    if row >= N:
        return True

    # Consider this row and try to place this queen in column one by one.
    for col in range(N):
        if isSafe(board, row, col):
            # place the queen in this position
            board[row][col] = 1
            # recursively solve to place rest of queens
            if solveNQUtil(board, row + 1) == True:
                return True
            # otherwise don't place the queen in that position
            board[row][col] = 0
    return False


def solveNQ():
    board1 = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
             ]
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solveNQ()


