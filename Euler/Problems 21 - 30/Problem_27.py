from time import time

def longest_consec():
    # f(n) = n^2 + an + b with |a| < 1000 and |b| <= 1000
    current_max = 0
    current_max_result = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if not isPrime(b): continue
            iter_result = consec_process(a, b)
            if iter_result > current_max:
                current_max = iter_result
                current_max_result = a * b

    return current_max_result


def consec_process(x, y):
    def f(n, a, b):
        return (n ** 2) + (a * n) + b
    index = 0
    while isPrime(f(index, x, y)): index += 1
    return index


def isPrime(x):
    if x <= 1: return False
    num = 2
    while num * num <= x:
        if x % num == 0: return False
        else: num += 1
    return True


start = time()
print(str(longest_consec()) + ' in ' + str(round(time() - start, 2)) + ' seconds.')
