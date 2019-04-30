def fib(length):
    x, y = 1, 1
    index = 2
    while len(str(y)) < length:
        x, y = y, x + y
        index += 1
    return index


print(fib(1000))
