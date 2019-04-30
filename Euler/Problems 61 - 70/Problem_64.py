def odd_period_square_roots():
    result = 4
    for n in range(13, 10001):
        a = largest_square(n)


def largest_square(x):
    # finds the largest number such that its square is less than x
    i = 1
    while (i + 1) ** 2 < x: i += 1
    return i


if __name__ == '__main__':
    print(odd_period_square_roots())
