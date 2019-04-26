# https://www.codewars.com/kata/building-chains-using-the-arithmetic-derivative-of-a-number/train/python
from timeit import default_timer
from random import randint
from eulerlib import *

def chain_arith_deriv(start, k):
    result = [start]
    k -= 1
    if isPrime(start): return str(start) + ' is a prime number'
    while k > 0:
        if result[-1] == 1:
            result += [1] * k
            k = 0
            continue
        iter_total = 0
        factorization = primefactors(result[-1])
        factorization = [(x, factorization.count(x)) for x in set(factorization)]
        for x in range(0, len(factorization)):
            arith_deriv_finder = factorization[:]
            arith_deriv_finder[x] = (arith_deriv_finder[x][0], arith_deriv_finder[x][1] - 1)
            store = [y[0] ** y[1] for y in arith_deriv_finder]
            sub_total = 1
            for y in store: sub_total *= y
            sub_total *= factorization[x][1]
            iter_total += sub_total
        result.append(iter_total)
        k -= 1
    return result

total = 0
numbers = [randint(1000, 99000000) for x in range(0, 50)]
for i in numbers:
    start = default_timer()
    print(chain_arith_deriv(i, randint(3, 15)))
    duration = round(default_timer() - start, 2)
    total += duration

print(str(min(numbers)) + ' - ' + str(max(numbers)))
print(str(round(total, 6)) + ' seconds')