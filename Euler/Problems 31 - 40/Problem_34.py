def fun():
    factorials = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    num_length = 2
    result = 0
    while num_length < 6:
        for x in range(10 ** (num_length - 1), 10 ** num_length):
            fact_digits = [factorials[y] for y in [int(z) for z in str(x)]]
            if all(j > (10 ** num_length) for j in fact_digits):
                num_length += 1
                break
            elif sum(fact_digits) == x: result += sum(fact_digits)
    return result


if __name__ == '__main__':
    print(fun())
