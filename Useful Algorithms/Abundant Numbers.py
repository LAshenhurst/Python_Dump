from eulerlib import *

def abundant(h):
    result = []
    if h < 12: return []
    for x in range(12, h + 1):
        proper_list = FactorsList(x)
        proper_list.remove(x)
        if sum(proper_list) > x: result.append((x, sum(proper_list)))
    return result

if __name__ == "__main__":
    print(abundant(200))