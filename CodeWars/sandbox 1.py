def solution(N, S):
    if S == "": return 3 * N
    result = 0
    column_id = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
    column_ABC = [[True, True, True] for x in range(N)]
    column_DEFG = [[True, True, True, True] for x in range(N)]
    column_HJK = [[True, True, True] for x in range(N)]
    for x in S.split(" "):
        row = int(x[0]) - 1
        column = column_id[x[-1]]
        if column < 3: column_ABC[row][column] = False
        elif column < 7: column_DEFG[row][column - 3] = False
        elif column < 11: column_HJK[row][column - 8] = False
    result += sum(1 for x in column_ABC if all(y is True for y in x))
    for x in column_DEFG: 
        if x[1] == True and x[2] == True: result += 1
    result += sum(1 for x in column_HJK if all(y is True for y in x))
    return result


if __name__ == "__main__":
    print(solution(50, '24H 5I 45F 20I 11F 24I 9H 27J 10F 40B 44J 23E 2I 6D 47H 35D 17F 7H 43D 15I 8G 28C 11A 49F 12G 13E 23C 17D 29G 35C 37G 29E 41E 12A'))