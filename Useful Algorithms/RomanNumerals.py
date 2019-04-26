import math

def convertmain(n):
    converted = ''
    count = 1
    while n > 0:
        converted = ''.join((convert(n % math.pow(10, count)), converted))
        n -= n % math.pow(10, count)
        count += 1
    return converted

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
                result += symbols(i)
                n -= i
                break
    return result

def combinations(n):
    for m in values:
        for i in values:
            if m + i == n: return symbols(m) + symbols(i)
    for i in range(len(values) - 1, 1, -1):
        if values[i - 1] - values[i] == n: return symbols(values[i]) + symbols(values[i - 1])
        if values[i - 2] - values[i] == n: return symbols(values[i]) + symbols(values[i - 2])
    return ''

def multiples(n):
    for i in [1, 2, 3]:
        if (n / i) in values: return symbols(n / i) * i
    return ''

values = [1000, 500, 100, 50, 10, 5, 1]
symbollist = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

def symbols(val):
    if val == 1: return 'I'
    if val == 5: return 'V'
    if val == 10: return 'X'
    if val == 50: return 'L'
    if val == 100: return 'C'
    if val == 500: return 'D'
    if val == 1000: return 'M'

print(convertmain(1666))