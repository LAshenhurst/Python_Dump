from eulerlib import *
import math

def prime_cube_partnership(n):
    primes = sieve_of_eratosthenes(n)
    count = 0
    for x in primes:
        index = 1
        while index < x:
            test = index ** 3 + ((index ** 2) * x)
            if math.pow(test, 1./3.) % 1.0 == 0:
                count += 1
                break
            else: index += 1
    return count

def prime_pair_connection():
    primes = sieve_of_eratosthenes(1000000)[2:]
    primes.append(FindNextPrime(primes[-1]))
    result = 0
    for x in range(0, len(primes) - 2):
        i = primes[x]
        j = primes[x + 1]
        test_value = 1
        s = int(str(test_value) + str(i))
        while s % j != 0:
            test_value += 1
            s = int(str(test_value) + str(i))
        else:
            result += test_value
    return result

print(prime_pair_connection())