def get_exponent(n, p):
    result = 1
    if p == 1: return None
    while True:
        if ((p ** result) / n) % 1.0 == 0: return result
        if p ** result > abs(n): return None
        result += 1

print(get_exponent(-250, 5))