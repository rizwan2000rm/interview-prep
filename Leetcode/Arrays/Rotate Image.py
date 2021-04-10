def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrixLength = len(matrix)

    # Transpose of Matrix
    for i in range(matrixLength):
        for j in range(i, matrixLength):
            matrix[i][j], matrix[j][i] = matrix[j][i],  matrix[i][j]

    for i in range(matrixLength):
        for j in range(matrixLength//2):
            matrix[i][j], matrix[i][matrixLength - 1 -
                                    j] = matrix[i][matrixLength - 1 - j], matrix[i][j]
