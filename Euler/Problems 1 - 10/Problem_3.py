from eulerlib import *

def ProblemThree():
    number = 600851475143
    prime = 2
    primes = []
    while not isPrime(number):
        if (number % prime) == 0:
            primes.append(int(prime))
            number /= prime
            prime = FindNextPrime(prime)
        else:
            prime = FindNextPrime(prime)
    primes.append(int(number))
    return max(primes)