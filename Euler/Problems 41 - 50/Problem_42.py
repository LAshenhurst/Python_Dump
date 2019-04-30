def fun():
    result = 0
    words = [x.replace('"', '') for x in
             open("//home//liam//Desktop//Python//Euler//Data files//Problem42_words.txt", "r").read().split(',')]
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for word in words:
        value = sum([alphabet.index(y) + 1 for y in word])
        if (((value * 8) + 1) ** 0.5) % 1.0 == 0: result += 1
    return result


if __name__ == '__main__':
    print(fun())
