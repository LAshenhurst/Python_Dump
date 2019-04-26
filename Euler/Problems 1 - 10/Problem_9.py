def ProblemNine():
    Result = 0
    Done = False
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = ((a * a) + (b * b)) ** 0.5
            if a + b + c == 1000:
                Result = int(a * b * c)
                Done = True
            if Done: break
        if Done: break
    return Result