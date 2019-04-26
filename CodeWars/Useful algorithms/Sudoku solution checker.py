def validSolution(board):
    for x in range(9):
        # Check the rows and columns
        if board[x].count(0) > 0: return False
        if sorted(board[x]) != list(range(1, 10)): return False
        testcolumn = [board[i][x] for i in range(9)]
        if sorted(testcolumn) != list(range(1, 10)): return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # Check the 3x3 boxes
            testcase = [[board[i][j], board[i][j + 1], board[i][j + 2]],
                        [board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2]],
                        [board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]]]
            testcase = [z for a in testcase for z in a]
            if sorted(testcase) != list(range(1, 10)): return False
    return True