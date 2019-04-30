def fun():
    result = 0
    fraction = [3, 2]
    for i in range(1, 1001):
        fraction = [fraction[0] + (2 * fraction[-1]), fraction[0] + fraction[1]]
        if len(str(fraction[0])) > len(str(fraction[-1])): result += 1
    return result


if __name__ == '__main__':
    print(fun())
