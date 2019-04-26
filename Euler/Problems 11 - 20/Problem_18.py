def Problem_18():
    numbers = [[int(y) for y in x.replace('\n', '').split(' ')] for x in open("C:\\Users\\lmat\\Desktop\\Euler\\Data files\\Problem18_Triangle.txt", 'r')]
    for x in range(len(numbers) - 2, -1, -1):
        for k in range(0, len(numbers[x])): numbers[x][k] += max(numbers[x + 1][k], numbers[x + 1][k + 1])
        del numbers[x + 1]
    return numbers[0][0]

print(Problem_18())