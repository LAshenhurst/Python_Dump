def fun():
    def is_palindrome(n): return str(n) == str(n)[::-1]
    return sum([x for x in range(1000000) if is_palindrome(x) and is_palindrome(bin(x)[2:])])


if __name__ == '__main__':
    print(fun())
