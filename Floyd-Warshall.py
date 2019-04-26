def fwalgorithm(n):
    # Floyd-Warshall algorithm to find the most efficient route through a weighted graph
    # Example matrix at the bottom is from: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    print('start matrix: ')
    print(n)
    paths = []
    done = False
    while done is False:
        # idea here is to try a mid-point to see if there's a faster route
        # e.g. point 1 to point 6 is weight 14, but point 1 to point 3 is weight 9, and point 3 to point 6 is weight 2
        # e.g. so it's quicker to go 1, 3, 6 than 1, 6.
        # this is in a while loop because for more complex graphs multiple iterations are needed to remove inefficiency
        changes = 0
        for start in range(0, len(n)):
            for end in range(0, len(n)):
                if start == end: continue
                for mid in range(0, len(n)):
                    if mid == start or mid == end or n[start][mid] == float('inf'): continue
                    if n[mid][end] == 0 or n[mid][end] == float('inf'): continue
                    if (n[start][end] == float('inf') and isinstance((n[start][mid] + n[mid][end]), int)) or (
                                    n[start][mid] + n[mid][end] < n[start][end]):
                        n[start][end] = n[start][mid] + n[mid][end]
                        paths.append(str(start + 1) + ',' + str(mid + 1) + ',' + str(end + 1))
                        changes += 1
        if changes == 0: done = True
    # paths list takes in every change to the matrix, whether it's the most efficient, or just part of the process
    # so paths_eval takes the list and returns every most efficient route from one point to another.
    # paths_eval also takes number of vertices to determine number of final routes required
    paths = paths_eval(paths, len(n))
    print('unique routes: ')
    print(paths)
    return n

def paths_eval(p, n):
    # removes reverses of already found paths
    for x in p:
        if x[::-1] in p: p.remove(x[::-1])
    # this removes all inefficient routes that were calculated in the process.
    # e.g route 1,2,4 with weight 22 will be calculated and added to list, then 1,3,4 with weight 20 afterwards
    # e.g. must get rid of route 1,2,4 and leave the more efficient one
    index = len(p) - 1
    while index > 0:
        for j in range(index - 1, -1, -1):
            if list(p[index])[0] == list(p[j])[0] and list(p[index])[-1] == list(p[j])[-1]:
                p.pop(j)
                index -= 1
        index -= 1
    for i in range(0, len(p)):
        # this searches for routes that miss a step.
        # e.g 1,3,5 is optimal, but to do 3 -> 5 you need to go through 6. the below turns 1,3,5 into 1,3,6,5
        points = p[i].split(',')
        for j in range(0, len(p)):
            if i == j: continue
            index = 0
            while index < len(points):
                if index + 1 == len(points): break
                if list(p[j])[0] == points[index] and list(p[j])[-1] == points[index + 1]:
                    points.insert(index + 1, list(p[j])[2])
                    break
                else: index += 1
        p[i] = ','.join(points)
    for i in range(1, n + 1):
        # this adds in any unchanged routes that are optimal.
        # e.g 1 -> 2 is most optimal route, so no change was made, so it's not in the list. Must be added.
        endpointsfound = [list(x)[-1] for x in p if list(x)[0] == str(i)]
        for j in range(i + 1, n + 1):
            if str(j) not in endpointsfound: p.append(str(i) + ',' + str(j))
    index = 1
    while index <= n:
        # this sorts the list by start point, and end point.
        # e.g shows 1 -> 2, then 1 -> 3, then 1 -> 4 etc etc, regardless of complexity
        px = [x for x in p if list(x)[0] == str(index)]
        p = [x for x in p if x not in px]
        px.sort(key=lambda x: int(x[-1]))
        p += px
        index += 1
    return p

n1 = [0, 7, 9, float('inf'), float('inf'), 14]
n2 = [7, 0, 10, 15, float('inf'), float('inf')]
n3 = [9, 10, 0, 11, float('inf'), 2]
n4 = [float('inf'), 15, 11, 0, 6, float('inf')]
n5 = [float('inf'), float('inf'), float('inf'), 6, 0, 9]
n6 = [14, float('inf'), 2, float('inf'), 9, 0]

n = [n1, n2, n3, n4, n5, n6]
fw_n = fwalgorithm(n[:])
print('end matrix: ')
print(fw_n)
