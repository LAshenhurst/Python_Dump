def generate_poly(n, i, j):

    def tri(x): return (x * (x + 1)) // 2

    def square(x): return x ** 2

    def pent(x): return (x * ((3 * x) - 1)) // 2

    def hex(x): return x * ((2 * x) - 1)

    def hept(x): return (x * ((5 * x) - 3)) // 2

    def oct(x): return x * ((3 * x) - 2)

    generators = {3: tri, 4: square, 5: pent, 6: hex, 7: hept, 8: oct}

    def fun_generate(k):
        result = []
        index = 2
        while not result or result[-1] < j:
            value = generators[k](index)
            if value > i: result.append(value)
            index += 1
        return result

    if isinstance(n, int): return fun_generate(n)
    elif isinstance(n, list): return [fun_generate(x) for x in n]
    else: return False


def cyclic_match(x, polys):
    return [y for y in polys if y in range(x * 100, (x + 1) * 100)]


def fun():
    polygonal_numbers = generate_poly([3, 4, 5, 6, 7, 8], 1000, 10000)
    polygonal_numbers[0] = [[i] for i in polygonal_numbers[0]]
    for i in range(1, 6):
        index = 0
        while index < len(polygonal_numbers[0]):
            if isinstance(polygonal_numbers[0][index][-1], int):
                cyclic_i = cyclic_match(polygonal_numbers[0][index][-1] % 100, polygonal_numbers[i])
                if not cyclic_i:
                    polygonal_numbers[0].pop(index)
                    continue
                elif len(cyclic_i) == 1: polygonal_numbers[0][index].append(cyclic_i[0])
                else: polygonal_numbers[0][index].append(cyclic_i)
            else:
                secondary_index = 0
                while secondary_index < len(polygonal_numbers[0][index][-1]):
                    cyclic_i = cyclic_match(polygonal_numbers[0][index][-1][secondary_index] % 100, polygonal_numbers[i])
                    if not cyclic_i:
                        polygonal_numbers[0][index][-1].pop(secondary_index)
                        continue
                    elif len(cyclic_i) == 1:
                        polygonal_numbers[0][index][-1][secondary_index] = [
                            polygonal_numbers[0][index][-1][secondary_index], cyclic_i[0]]
                    else:
                        polygonal_numbers[0][index][-1][secondary_index] = [
                            polygonal_numbers[0][index][-1][secondary_index], cyclic_i]
                    secondary_index += 1
                if len(polygonal_numbers[0][index][-1]) == 1:
                    polygonal_numbers[0][index] += polygonal_numbers[0][index][-1][0]
                    polygonal_numbers[0][index].pop(1)
            index += 1
    return polygonal_numbers[0]


def is_tri(n): return (1 + (8 * n)) % 1.0 == 0 and (-1 + ((1 + (8 * n)) ** 0.5)) % 2 == 0


def is_square(n): return (n ** 0.5) % 1.0 == 0


def is_pent(n): return (1 + (24 * n)) % 1.0 == 0 and (1 + ((1 + (24 * n)) ** 0.5)) % 6 == 0


def is_hex(n): return (1 + (8 * n)) % 1.0 == 0 and (1 + ((1 + (8 * n)) ** 0.5)) % 4 == 0


def is_hept(n): return (9 + (40 * n)) % 1.0 == 0 and (3 + ((9 + (40 * n)) ** 0.5)) % 10 == 0


def is_oct(n): return (4 + (12 * n)) % 1.0 == 0 and (2 + ((4 + (12 * n)) ** 0.5)) % 2 == 0


if __name__ == '__main__':
    result = fun()
    for x in result:
        if not is_tri(x[0]): print(x, " -> tri failed.")
        elif not is_square(x[1]): print(x, "-> square failed.")
        elif not is_pent(x[2]): print(x, "-> pent failed.")
        elif not is_hex(x[3]): print(x, "-> hex failed.")
        elif not is_hept(x[4]): print(x, "-> hept failed.")
        elif not is_oct(x[5]): print(x, "-> oct failed.")
        else: print("answer:", x, "->", sum(x))