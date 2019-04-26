def ProblemEleven():
    result = 1
    forward_test, down_test, diag_up_right_test, diag_up_left_test, diag_down_right_test, diag_down_left_test = 0,0,0,0,0,0
    lines = open("C:\\Users\\lmat\\Desktop\\Euler\\Data Files\\Problem11_Grid", "r").readlines()
    for i in range(0, len(lines)): lines[i] = [int(x) for x in lines[i][:-1].split() if x != '\n']
    for i in range(0, 19):
        for j in range(0, 19):
            if j + 3 < 20:
                forward_test = lines[i][j] * lines[i][j + 1] * lines[i][j + 2] * lines[i][j + 3]
            if i + 3 < 20:
                down_test = lines[i][j] * lines[i + 1][j] * lines[i + 2][j] * lines[i + 3][j]
            if i + 3 < 20 and j + 3 < 20:
                diag_down_right_test = lines[i][j] * lines[i + 1][j + 1] * lines[i + 2][j + 2] * lines[i + 3][j + 3]
            if i - 3 > 0 and j + 3 < 20:
                diag_up_right_test = lines[i][j] * lines[i - 1][j + 1] * lines[i - 2][j + 2] * lines[i - 3][j + 3]
            if i - 3 > 0 and j - 3 > 0:
                diag_up_left_test = lines[i][j] * lines[i - 1][j - 1] * lines[i - 2][j - 2] * lines[i - 3][j - 3]
            if i + 3 < 20 and j - 3 > 0:
                diag_down_left_test = lines[i][j] * lines[i + 1][j - 1] * lines[i + 2][j - 2] * lines[i + 3][j - 3]
            values = [forward_test, down_test, diag_down_left_test, diag_down_right_test, diag_up_left_test, diag_up_right_test]
            if max(values) > result: result = max(values)
    return result

print(ProblemEleven())