from math import factorial


def c(n, r): return factorial(n) / (factorial(r) * factorial(n - r))


def fun():
    return sum([1 for i in range(1, 101) for j in range(1, i) if c(i, j) > 1000000])


if __name__ == '__main__':
    print(fun())