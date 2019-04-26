from eulerlib import *

def ProblemFour():
    Largest = 0
    for i in range(100, 999):
        for j in range(100, 999):
            if (isPalindrome(i * j)) and (i * j > Largest): Largest = i * j
    return Largest