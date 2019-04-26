from eulerlib import *

def ProblemTwelve():
    count = 7
    Done = False
    while not Done:
        count += 1
        if len(FactorsList(TriangleNumber(count))) > 500: Done = True
    return TriangleNumber(count)