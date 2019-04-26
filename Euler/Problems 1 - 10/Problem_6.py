def ProblemSix():
    SumSquared = 0
    SquaredSum = 0
    for i in range(1, 101):
        SumSquared += (i * i)
        SquaredSum += i
    return (SquaredSum * SquaredSum) - SumSquared