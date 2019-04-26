from eulerlib import *

def ProblemFive():
    # LCM(x,y) = (x * y) / GCD(x, y)
    Result = 1
    for i in range(1, 21):
        Result = int((Result * i) / GCD(Result, i))
    return Result