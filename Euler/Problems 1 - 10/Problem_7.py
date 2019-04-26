from eulerlib import *

def ProblemSeven():
    Result = 2
    for count in range(1, 10001): Result = FindNextPrime(Result)
    return Result