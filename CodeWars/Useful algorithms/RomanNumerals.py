import math

def convertto(n):
    converted = ''
    count = 1
    while n > 0:
        converted = ''.join((convert(int(n % math.pow(10, count))), converted))
        n -= n % math.pow(10, count)
        count += 1
    return converted

def convertfrom(n): return None


def convert(n):
    if n == 0: return ''
    result = multiples(n)
    if result is not '': return result
    result = combinations(n)
    if result is not '': return result
    while n > 0:
        if combinations(n) is not '':
            result += combinations(n)
            n = 0
            break
        for i in values:
            if n - i >= 0:
                result += symbols[i]
                n -= i
                break
    return result

def combinations(n):
    for m in values:
        for i in values:
            if m + i == n: return symbols[m] + symbols[i]
    for i in range(len(values) - 1, 1, -1):
        if values[i - 1] - values[i] == n: return symbols[values[i]] + symbols[values[i - 1]]
        if values[i - 2] - values[i] == n: return symbols[values[i]] + symbols[values[i - 2]]
    return ''

def multiples(n):
    for i in [1, 2, 3]:
        if (n / i) in values: return symbols[n / i] * i
    return ''

values = [1000, 500, 100, 50, 10, 5, 1]
symbollist = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
symbols = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

print(convertto(1666))
# print(convertfrom(convertto(1666)))
