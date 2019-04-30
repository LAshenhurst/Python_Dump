# Doesn't work


def fun():

    def is_pent(n):
        if not isinstance(n, int) or n < 0: return False
        root = ((24 * n) + 1)
        if (root ** 0.5) % 1.0 != 0: return False
        return ((root ** 0.5) + 1) % 6 == 0 or ((root * 0.5) - 1) % 6 == 0

    def next_pent(n):
        return int((n * (3 * n - 1)) / 2)

    pents = [1, 5]
    while True:
        index = len(pents) - 1
        for i in range(index):
            if is_pent(pents[i] + pents[index]) and is_pent(pents[i] - pents[index]): return pents[i], pents[index]
        pents.append(next_pent(index + 2))


if __name__ == '__main__':
    print(fun())