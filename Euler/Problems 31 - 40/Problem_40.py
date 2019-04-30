def fun():
    champernownes = ''
    index = 1
    while len(champernownes) < 1000000:
        champernownes += str(index)
        index += 1
    result = [champernownes[0], champernownes[9], champernownes[99], champernownes[999], champernownes[9999],
              champernownes[99999], champernownes[999999]]
    prod = 1
    for x in result: prod *= int(x)
    return prod


if __name__ == '__main__':
    print(fun())
