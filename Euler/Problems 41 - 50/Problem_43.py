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


def fun():
    result = 0
    pandigitals = permutations('0123456789')
    primes = [2, 3, 5, 7, 11, 13, 17]
    for x in pandigitals:
        split = [int(x[1] + x[2] + x[3]), int(x[2] + x[3] + x[4]), int(x[3] + x[4] + x[5]), int(x[4] + x[5] + x[6]),
                 int(x[5] + x[6] + x[7]), int(x[6] + x[7] + x[8]), int(x[7] + x[8] + x[9])]
        if all(y % primes[i] == 0 for i, y in enumerate(split)): result += int(x)
    return result


if __name__ == '__main__':
    print(fun())