def Problem_13():
    numbers = [int(x[:-1]) for x in open("C:\\Users\\lmat\\Desktop\\PyCharmTest\\Problem13_numbers.txt", 'r')]
    result = str(sum(numbers))
    return result[:9]