def to_postfix(infix):
    split = list(infix)
    while '(' in split:
        index = split.index('(')
        expression = ''.join(split[index + 1: split.index(')')])
        del split[split.index('('): split.index(')') + 1]
        split.insert(index, brackets(expression))
    for x in ['^', '*', '/', '+', '-']:
        while x in split:
            index = split.index(x)
            expression = split[index - 1: index + 2]
            del split[index - 1: index + 2]
            split.insert(index - 1, expr_eval(expression))
    return ''.join(split)

def brackets(terms):
    return to_postfix(terms)

def expr_eval(expression):
    return expression[0] + expression[2] + expression[1]