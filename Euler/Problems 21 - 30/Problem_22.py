def problem_22():
    names = [x.replace('"', '') for x in open("C:\\Users\\lmat\\Desktop\\Euler\\Data files\\Problem22_names.txt", "r").read().split(',')]
    names.sort()
    return sum(sum((ord(x) - 64) for x in y) * (names.index(y) + 1) for y in names)

print(problem_22())