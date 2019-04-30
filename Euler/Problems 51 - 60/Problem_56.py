def power(digits, a):
    digits = [a * x for x in digits]
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] > 10:
            if i == 0:
                while digits[0] > 10:
                    digits.insert(0, digits[0] // 10)
                    digits[1] %= 10
            else:
                digits[i - 1] += digits[i] // 10
                digits[i] %= 10
    return digits


def fun():
    result = 0
    for a in range(2, 100):
        digits = [int(x) for x in str(a)]
        for b in range(1, 100):
            digits = power(digits, a)
            digit_sum = sum(digits)
            if digit_sum > result:
                result = digit_sum
    return result


if __name__ == '__main__':
    print(fun())
