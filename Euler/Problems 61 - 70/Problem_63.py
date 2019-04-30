# 10 ^ x will always have x + 1 digits
# 9 ^ x will always have x digits, up to x = 21, after which it has less than x digits


def powerful_digit():
    return sum(1 for i in range(1, 10) for j in range(1, 22) if len(str(i ** j)) == j)


if __name__ == '__main__':
    print(powerful_digit())
