def tri(n):
    return int((n*(n + 1)) / 2)


def is_pent(n):
    if not isinstance(n, int) or n < 0: return False
    if ((24 * n + 1) ** 0.5) % 1.0 != 0: return False
    if not (((24 * n + 1) ** 0.5) + 1) % 6 == 0 or (((24 * n + 1) ** 0.5) - 1) % 6 == 0: return False
    return True


def is_hex(n):
    if not isinstance(n, int) or n < 0: return False
    if ((8 * n + 1) ** 0.5) % 1.0 != 0: return False
    if not (((8 * n + 1) ** 0.5) + 1) % 4 == 0 or (((8 * n + 1) ** 0.5) - 1) % 4 == 0: return False
    return True


def fun():
    n = 286
    while not (is_pent(tri(n)) and is_hex(tri(n))): n += 1
    return tri(n)


if __name__ == '__main__':
    print(fun())