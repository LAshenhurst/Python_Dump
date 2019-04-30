from itertools import count


def reciprocal_cycle_len(n):
    seen = {}
    x = 1
    for i in count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n


ans = max(range(1, 1000), key=reciprocal_cycle_len)
print(ans)
