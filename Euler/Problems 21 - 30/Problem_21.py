from eulerlib import *

def problem_21():
    result = 0
    for i in range(1, 10000):
        prop_divisors = sum(FactorsList(i)) - i
        if prop_divisors <= i: continue
        prop_divisors_divisors = sum(FactorsList(prop_divisors)) - prop_divisors
        if prop_divisors_divisors == i: result += (i + prop_divisors)
    return result

print(problem_21())