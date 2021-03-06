from eulerlib import sieve_of_eratosthenes

def goldbach(even_number):
    primes = sieve_of_eratosthenes(even_number)
    result = ''
    for x in range(0, len(primes)):
        for y in range(x, len(primes)):
            if primes[x] + primes[y] == even_number:
                result = (primes[x], primes[y])
    return result

if __name__ == "__main__":
    print(goldbach(222))