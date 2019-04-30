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
    result = 0
    pandigits = '123456789'
    index = 0
    while result == 0:
        for x in permutations(pandigits[:9 - index]):
            if is_prime(int(x)) and int(x) > result:
                result = int(x)
        index += 1
    return result


if __name__ == '__main__':
    print(fun())
