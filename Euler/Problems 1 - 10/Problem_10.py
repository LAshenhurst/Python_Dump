from eulerlib import *

def ProblemTen():
    Result = 0
    Prime = 2
    while Prime < 2000000:
        Result += Prime
        Prime = FindNextPrime(Prime)
    return Result