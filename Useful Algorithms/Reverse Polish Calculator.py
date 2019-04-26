def calc(expr):
    if len(expr) == 0: return 0
    operations = ['+', '-', '*', '/']
    result = 0
    parts = [k if k in operations else int(k) for k in expr.split()]
    if not any(i in parts for i in operations): return max(parts)
    index = 0
    while index < len(parts):
        if parts[index] in operations and index - 2 >= 0:
            if isinstance(parts[index - 2], int) or parts[index - 2].isdigit():
                eval_string = 'result + (' + str(parts[index - 2]) + ' ' + parts[index] + ' ' + str(parts[index - 1]) + ')'
                result = eval(eval_string)
            else:
                eval_string = 'result ' + parts[index] + ' ' + str(parts[index - 1])
                result = eval(eval_string)
        index += 1
    return int(result)

print(calc('4 2 13'))