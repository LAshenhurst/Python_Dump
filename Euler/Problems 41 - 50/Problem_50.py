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
        index += 1
    return True


def fun():
    result = 0
    return result


if __name__ == '__main__':
    print(fun())