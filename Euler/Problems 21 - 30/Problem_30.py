def fun():
    result = []
    for x in range(2, 999999):
        digits = [int(y) for y in list(str(x))]
        power_sum = sum([z**5 for z in digits])
        if power_sum == x: result.append(x)
    return sum(result)


if __name__ == '__main__':
    print(fun())
