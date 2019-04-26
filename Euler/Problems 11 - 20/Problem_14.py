import math

def Problem_14():
    results = {}
    for i in range(1, 1000000):
        value = i
        steps = 0
        while value != 1:
            if value in results.keys():
                steps += results[value]
                value = 1
                continue
            elif (i & (i - 1)) == 0:
                ## above is the fastest log2(x) check
                steps += int(math.log2(i))
                value = 1
                continue
            elif value % 2 == 0: value /= 2
            else: value = (3 * value) + 1
            steps += 1
        else: results[i] = steps
        print(len(results.keys()))
    max_result = max(results.values())
    for test, result in results.items():
        if result == max_result: return test