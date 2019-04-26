from eulerlib import *

def relatively_prime(n, l):
    # takes in a number, and a list of numbers.
    # Find the distinct prime factors of n, and then see if any number in l is divisible by any of them
    nprimefactors = primefactors(n)
    result = [x for x in l if all(map(lambda y: x % y != 0, set(nprimefactors)))]
    return result