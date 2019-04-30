def is_prime(x):
    if x <= 1: return False
    num = 2
    while num * num <= x:
        if x % num == 0:
            return False
        else:
            num += 1
    return True


def find_next_prime(x):
    if x % 2 == 0: x += 1
    else: x += 2
    while not is_prime(x): x += 2
    return x


def find_next_composite(x):
    if x % 2 == 0: x += 1
    else: x += 2
    while is_prime(x): x += 2
    return x


def fun():
    primes = [2, 3]
    composite = 33

    def conjecture_true(comp, prime):
        if prime > comp: return False
        remainder = comp - prime
        return ((remainder / 2) ** 0.5) % 1.0 == 0

    while True:
        composite = find_next_composite(composite)
        while primes[-1] < composite: primes.append(find_next_prime(primes[-1]))
        if all(not conjecture_true(composite, x) for x in primes): return composite


if __name__ == '__main__':
    print(fun())