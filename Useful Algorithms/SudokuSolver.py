def sudoku(startgrid):
    hori_vert_test, square_test = True, True
    while hori_vert_test and square_test is not False:
        hori_vert_test = horizontal_vertical_possibilities([a[:] for a in startgrid])
        if hori_vert_test is not False:
            square_test = three_by_three_possibilities([b[:] for b in hori_vert_test])
            if square_test is not False: startgrid = square_test
            else: startgrid = hori_vert_test
    return startgrid


def three_by_three_possibilities(to_reduce):
    n = [c[:] for c in to_reduce]
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            testcase = [[n[i][j], n[i][j + 1], n[i][j + 2]],
                        [n[i + 1][j], n[i + 1][j + 1], n[i + 1][j + 2]],
                        [n[i + 2][j], n[i + 2][j + 1], n[i + 2][j + 2]]]
            found_or_given = [f for z in range(0, 3) for f in testcase[z] if isinstance(f, int)]
            for x in range(0, 3):
                for y in range(0, 3):
                    if not isinstance(testcase[x][y], list): continue
                    else:
                        testcase[x][y] = [a for a in testcase[x][y] if a not in found_or_given]
                        if len(testcase[x][y]) > 1: n[i + x][j + y] = testcase[x][y]
                        elif len(testcase[x][y]) == 1: n[i + x][j + y] = testcase[x][y][0]
    changes = 0
    for x in range(9):
        for y in range(9):
            if n[x][y] != to_reduce[x][y]: changes += 1
    if changes != 0: return n
    else: return False


def horizontal_vertical_possibilities(to_reduce):
    n = [d[:] for d in to_reduce]
    for x in range(9):
        for y in range(9):
            if n[x][y] == 0:
                n[x][y] = [i for i in range(1, 10) if i not in n[x]]
                for i in range(9):
                    if i == x: continue
                    if n[i][y] in n[x][y]: n[x][y].remove(n[i][y])
            elif isinstance(n[x][y], list):
                intlist = [j for j in n[x] if isinstance(j, int)]
                n[x][y] = [k for k in n[x][y] if k not in intlist]
                for i in range(9):
                    if i == x: continue
                    if n[i][y] in n[x][y]: n[x][y].remove(n[i][y])
                if len(n[x][y]) == 1: n[x][y] = n[x][y][0]
    changes = 0
    for x in range(9):
        for y in range(9):
            if n[x][y] != to_reduce[x][y]: changes += 1
    if changes != 0: return n
    else: return False


puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
          [0, 8, 0, 0, 9, 0, 0, 3, 0],
          [2, 0, 0, 0, 0, 5, 4, 0, 0],
          [4, 0, 0, 0, 0, 1, 8, 0, 0],
          [0, 3, 0, 0, 7, 0, 0, 4, 0],
          [0, 0, 7, 9, 0, 0, 0, 0, 3],
          [0, 0, 8, 4, 0, 0, 0, 0, 6],
          [0, 2, 0, 0, 5, 0, 0, 8, 0],
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]

solution = [[3, 4, 6, 1, 2, 7, 9, 5, 8],
            [7, 8, 5, 6, 9, 4, 1, 3, 2],
            [2, 1, 9, 3, 8, 5, 4, 6, 7],
            [4, 6, 2, 5, 3, 1, 8, 7, 9],
            [9, 3, 1, 2, 7, 8, 6, 4, 5],
            [8, 5, 7, 9, 4, 6, 2, 1, 3],
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]]

if sudoku(puzzle) == solution:
    for x in solution: print(x)
else: print('Error.')
