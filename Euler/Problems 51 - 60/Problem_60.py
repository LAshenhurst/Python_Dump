from itertools import combinations


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


def is_prime(x):
    if x <= 1: return False
    index = 2
    while index * index <= x:
        if x % index == 0: return False
        else: index += 1
    return True


def fun():
    result = 0
    primes = sieve_of_eratosthenes(100)
    combos = sorted(combinations(primes, 5), key=lambda x: sum(x))
    for set in combos:
        concats = [int(str(x) + str(y)) for x, y in combinations(set, 2)]
        if all(is_prime(x) for x in concats) and sum(set) < result: result = sum(set)
    return result


if __name__ == '__main__':
    print(fun())