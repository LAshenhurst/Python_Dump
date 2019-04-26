# Uses Euler's recurrance formula: https://en.wikipedia.org/wiki/Partition_(number_theory)#Recurrence_formula
def exp_sum(n):
    known = [1, 1, 2, 3, 5]
    if n < 0: return 0
    if n <= 4: return known[n]
    for i in range(5, n + 1):
        known.append(known[-1] + known[-2] + diff_finder(known, i))
    return known[-1]

def diff_finder(found, n):
    result = 0
    k = 2
    done = False
    while done is False:
        pents = gen_pents(k)
        sign = (-1)**(k - 1)
        if n - pents[0] < 0: done = True
        else: result += sign * found[n - pents[0]]
        sign = (-1)**((k - 1) * - 1)
        if n - pents[1] < 0: done = True
        else: result += sign * found[n - pents[1]]
        k += 1
    return int(result)

def gen_pents(n): return [int((3*(n**2) - n) / 2), int((3*((n*-1)**2)-(n*-1))/2)]

for x in range(0, 100): print(exp_sum(x))
