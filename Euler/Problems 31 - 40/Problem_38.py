def is_pandigital(num, length):
    if not isinstance(num, str) or len(num) != length: return False
    return ''.join(sorted(num)) == ''.join(str(x) for x in range(1, length + 1))


def concat(num, max):
    return ''.join(str(num * x) for x in range(1, max + 1))


def fun():
    result = 0
    num = 1
    while True:
        concat_num = 2
        test = concat(num, concat_num)
        if len(test) > 9: break
        while len(test) < 9:
            concat_num += 1
            test = concat(num, concat_num)
        if len(test) > 9: num += 1
        elif len(test) == 9 and is_pandigital(test, 9):
            if int(test) > result: result = int(test)
        num += 1

    return result


if __name__ == '__main__':
    print(fun())
