from eulerlib import *

def problem_23():
    abundants = [x for x in range(1, 28124) if (sum(FactorsList(x)) - x) > x]
    sums_of_abundants = [x + y for x in abundants for y in abundants]