def permutations(elements):
    if any(x // 10 > 0 for x in elements): return None
    if len(elements) <= 1: return None
    if len(elements) == 2: return [(elements[0] * 10) + elements[1], (elements[1] * 10) + elements[0]]
    result = list()
    for i in elements:
        sub_list = [x for x in elements if x != i]
        sublist_perms = permutations(sub_list)
        for j in sublist_perms:
            value = j + (i * (10 ** (len(elements) - 1)))
            result.append(value)
    return result


x = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1000000])
