def determinant(matrix):
    resultparts = []
    result = 0
    if len(matrix) == 1: 
	return matrix[0][0]
    if len(matrix) == 2: 
	return ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
    if len(matrix) >= 3:
        for i in range(0, len(matrix)):
            minormatrix = []
            for row in matrix: minormatrix.append(row[:])
            minormatrix.pop(0)
            for row in minormatrix: row.pop(i)
            resultparts.append(matrix[0][i] * determinant(minormatrix))
    for i in range(0, len(resultparts)):
        if i % 2 == 0: result += resultparts[i]
        else: result -= resultparts[i]
    return result