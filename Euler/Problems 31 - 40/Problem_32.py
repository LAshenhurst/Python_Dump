def is_pandigital(n, required_len=None):
    if len(n) <= 1 or not isinstance(n, str): return False
    if required_len is not None:
        if len(n) < required_len: return False
    digits = list(n)
    digits.sort()
    for i, x in enumerate(digits):
        if int(x) != i + 1: return False
    return True


def fun():
    result = 0
    identities = []
    products = []
    for i in range(10000):
        for j in range(1, i):
            if i % j == 0 and i not in products:
                if is_pandigital(str(i) + str(j) + str(int(i/j)), 9):
                    result += i
                    products.append(i)
                    identities.append([i, j, int(i/j)])
    return result


if __name__ == '__main__':
    print(fun())
