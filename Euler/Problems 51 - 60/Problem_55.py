def is_palindrome(x): return str(x) == str(x)[::-1]


def fun():
    result = 0
    for i in range(1, 10000):
        iterations = 0
        while iterations < 50:
            i = i + int(str(i)[::-1])
            if is_palindrome(i): break
            else: iterations += 1
            if iterations == 50: result += 1
    return result


if __name__ == '__main__':
    print(fun())
