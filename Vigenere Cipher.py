# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

class VigenereCipher (object):
    def __init__(self, key, abc):
        self.alphabet = abc
        self.key = key
        self.grid = [list(self.alphabet[i:] + self.alphabet[0:i]) for i in range(0, len(self.alphabet))]
        pass

    def encode(self, str):
        if not [x for x in self.key if x in self.alphabet]: return str
        chars = list(str)
        result = []
        for i, e in enumerate(chars):
            if e not in self.alphabet:
                result.append(e)
                continue
            # x is determined by the key, repeats when key not long enough. y is determined by the letter being encoded.
            # letter in password = a, letter to encode = c, so result = grid[0][2] = c
            x = self.alphabet.index(self.key[i % len(self.key)])
            y = self.alphabet.index(e)
            result.append(self.grid[x][y])
        return ''.join(result)

    def decode(self, str):
        if not [x for x in self.key if x in self.alphabet]: return str
        chars = list(str)
        result = []
        for i, e in enumerate(chars):
            if e not in self.alphabet:
                result.append(e)
                continue
            # decode by finding the encoded letter's place in the password letter's row in grid
            # letter in password = c, letter to decode = c, so result = grid[0][0] = a
            x = self.grid[self.alphabet.index(self.key[i % len(self.key)])].index(e)
            result.append(self.alphabet[x][0])
        return ''.join(result)

alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_key = 'password'

katakana = "アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー"
katakana_key = 'カタカナ'

d = VigenereCipher(alpha_key, alpha)
print('password => ' + d.encode('password'))
print(d.encode('password') + ' => ' + d.decode(d.encode('password')))

c = VigenereCipher(katakana_key, katakana)
print('カタカナ => ' + c.encode('カタカナ'))
print(c.encode('カタカナ') + ' => ' + c.decode(c.encode('カタカナ')))
