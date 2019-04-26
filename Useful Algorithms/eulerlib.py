import math

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)

def GCD(x, y):
    r = x % y
    if r == 0: return y
    else: return GCD(y, r)

def isPrime(x):
    if x <= 1: return False
    num = 2
    while num * num <= x:
        if x % num == 0: return False
        else: num += 1
    return True

def FindNextPrime(x):
    Test = x
    if Test % 2 == 0: Test += 1
    else: Test += 2
    while not isPrime(Test): Test += 2
    return Test

def isPalindrome(x):
    StringX = str(x)
    Chars = list(StringX)
    Chars.reverse()
    if StringX == "".join(Chars): return True
    else: return False

def TriangleNumber(x):
    return (x * (x + 1)) / 2

def PentagonalNumber(x):
    return (x * ((3 * x) - 1)) / 2

def HexagonalNumber(x):
    return x * ((2 * x) - 1)

def log2(x): return (x & (x - 1) == 0)

def FactorsList(x):
    Factors = [i for i in range(1, int(x ** 0.5) + 1) if x % i == 0]
    Factors += [int(x / i) for i in Factors if int(x / i) not in Factors]
    return sorted(Factors)

def primefactors(factors):
    return [x for x in factors is isPrime(x)]

def sieve_of_eratosthenes(n):
    numbers = [2] + list(range(3, n + 1, 2))
    primes = [2]
    count = 1
    while True:
        nonduplicates = []
        primemultiples = list(range(numbers[count] * 2, numbers[-1] + 1, numbers[count]))
        for x in primemultiples:
            if all(map(lambda y: x % y != 0, primes)): nonduplicates.append(x)
        if not nonduplicates: break
        primes.append(numbers[count])
        numbers = list(set(numbers) - set(nonduplicates))
        numbers.sort()
        count += 1
    return numbers