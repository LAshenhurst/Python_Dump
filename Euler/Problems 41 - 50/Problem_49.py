def is_prime(n):
    if n <= 1: return False
    index = 2
    while index * index <= n:
        if n % index == 0: return False
        index += 1
    return True


def is_permutation(x, y):
    return ''.join(sorted(str(x))) == ''.join(sorted(str(y)))


def fun():
    index = 1489
    while True:
        val_one = index + 3330
        val_two = index + 6660
        if not (is_permutation(index, val_one) and is_permutation(index, val_two)):
            index += 2
            continue
        elif not (is_prime(index) and is_prime(val_one) and is_prime(val_two)):
            index += 2
            continue
        else: break
    return str(index) + str(val_one) + str(val_two)


if __name__ == '__main__':
    print(fun())