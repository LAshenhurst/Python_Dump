from eulerlib import *

def next_palindrome(n):
    if not isPalindrome(n): return False
    digits = list(int(x) for x in str(n))
    if len(digits) % 2 == 0:
        digits[len(digits) // 2] += 1
        digits[(len(digits) // 2) - 1] += 1
        return int(''.join(str(x) for x in digits))
    else:
        if digits[(len(digits) // 2)] + 1 < 10:
            digits[(len(digits) // 2)] += 1
            return int(''.join(digits))
        else:
            digits = digits[0: (len(digits) // 2) + 1][:]
            for i in range(len(digits) - 1, 0, -1):
                if digits[i] + 1 == 10 and i >= 1:
                    digits[i] = 0
                    digits[i - 1] += 1
            return int(''.join(str(x) for x in digits + digits[::-1][1:]))

print(next_palindrome(1331))