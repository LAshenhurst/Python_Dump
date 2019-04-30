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


def permutations(n):
    if not isinstance(n, str) or len(n) <= 1: return [n]
    if len(n) == 2: return [n, n[::-1]]
    if len(n) > 2:
        result = []
        chars = list(n)
        for x in chars:
            recursive_chars = chars[:]
            recursive_chars.remove(x)
            result += [x + y for y in permutations(''.join(recursive_chars))]
        return list(set(result))


def is_prime(x):
    if x <= 1: return False
    num = 2
    while num * num <= x:
        if x % num == 0:
            return False
        else:
            num += 1
    return True


def fun():
    rotations = {x: list(set([int(y) for y in permutations(str(x))])) for x in sieve_of_eratosthenes(1000000)}
    count = 0
    for i, x in enumerate(rotations):
        if i % 100 == 0: print(str(i) + ' / ' + str(len(rotations)))
        if all(is_prime(z) for z in rotations[x]): count += 1
    return count


if __name__ == '__main__':
    print(fun())
