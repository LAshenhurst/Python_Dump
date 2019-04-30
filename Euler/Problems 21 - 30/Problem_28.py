from time import time

def problem_28():
    upper_right = [1, 9, 25]
    upper_left = [1, 7, 21]
    lower_right = [1, 3, 13]
    lower_left = [1, 5, 17]

    for i in range(7, 1002, 2):
        upper_right.append(i ** 2)
        upper_left.append(((i - 2) * 7) + 8)
        lower_right.append(lower_right[-1] + (lower_right[-1] - lower_right[-2]) + 8)
        lower_left.append(lower_left[-1] + ((i - 2) * 4))
    return sum(upper_left) + sum(upper_right) + sum(lower_left) + sum(lower_right)


start = time()
print(str(problem_28()) + ' in ' + str(round(time() - start, 2)) + ' seconds.')