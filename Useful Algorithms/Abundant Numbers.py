from eulerlib import *

def abundant(h):
    max_abund = 0
    excess = 0
    if h < 12: return [[0], [0]]
    for x in range(12, h + 1):
        proper_list = FactorsList(x)
        if sum(proper_list) > x:
            max_abund = x
            excess = sum(proper_list) - x
    return [[max_abund], [excess]]