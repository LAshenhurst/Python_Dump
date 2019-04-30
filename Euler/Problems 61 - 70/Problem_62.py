def permutations(n):
    if len(n) <= 1: return n
    if len(n) == 2: return [n, n[::-1]]
    if len(n) > 2:
        result = []
        for x in n:
            recursive_n = n[:]
            recursive_n.remove(x)
            result += [x + ''.join(y) for y in permutations(recursive_n)]
        return result


def cube_root(n):
    return (n ** (1. / 3)) % 1.0 == 0


def fun():
    index = 346
    while True:
        val = index ** 3
        perms = [int(x) for x in permutations(list(str(val))) if cube_root(int(x))]
        if len(perms) == 5: break
        else: index += 1
    return index


if __name__ == '__main__':
    print(fun())
