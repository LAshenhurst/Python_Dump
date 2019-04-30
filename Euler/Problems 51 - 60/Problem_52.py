def fun():
    result = 1
    while True:
        values = [result * 2, result * 3, result * 4, result * 5, result * 6]
        if all(sorted(str(x)) == sorted(str(result)) for x in values):
            return result
        else: result += 1


if __name__ == '__main__':
    print(fun())