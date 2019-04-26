def ProblemEight():
    Result = 1
    Lines = []
    for line in open("C:\\Users\\lmat\\PycharmProjects\\PyCharmTest\\Problem8_Numbers", "r"): Lines += list(line)
    Lines = [x for x in Lines if x != '\n']
    for i in range(0, len(Lines) - 13):
        Test = 1
        for j in range(0, 13): Test *= int(Lines[i + j])
        if Test > Result: Result = Test
    return Result