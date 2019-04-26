def permutations(string):
    result = []
    stringlist = list(string)
    if not stringlist: return result
    elif len(stringlist) == 1: result.append(stringlist[0])
    elif len(stringlist) == 2:
        result.append(stringlist[0] + stringlist[1])
        result.append(stringlist[1] + stringlist[0])
    else:
        for x in range(0, len(stringlist)):
            recursionlist = stringlist[:]
            recursionlist.pop(x)
            recursivepermutations = [stringlist[x] + k for k in permutations(''.join(recursionlist))]
            result += recursivepermutations
    return list(set(result))