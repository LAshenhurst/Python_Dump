def is_prime(x):
    if x <= 1: return False
    num = 2
    while num * num <= x:
        if x % num == 0:
            return False
        else:
            num += 1
    return True


def find_next_prime(n):
    if n % 2 == 0: n += 1
    else: n += 2
    while not is_prime(n): n += 2
    return n


def fun():
    result = 0
    prime = 11
    count = 0
    while count != 11:
        trunc_right = [int(str(prime)[x:]) for x in range(1, len(str(prime)))]
        trunc_left = [int(str(prime)[:x]) for x in range(1, len(str(prime)))]
        trunc_vals = list(set(trunc_right + trunc_left))
        if all(is_prime(x) for x in trunc_vals):
            result += prime
            count += 1
        prime = find_next_prime(prime)
    return result


if __name__ == '__main__':
    print(fun())
