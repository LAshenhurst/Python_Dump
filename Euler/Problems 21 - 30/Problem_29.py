from time import time


def problem_29():
    return len(set([a ** b for a in range(2, 101) for b in range(2, 101)]))


start = time()
print(str(problem_29()) + ' in ' + str(round(time() - start, 2)) + ' seconds.')