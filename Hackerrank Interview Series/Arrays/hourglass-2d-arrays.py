def hourglassSum(arr):
    # [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    hourglassesSum = []
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hourglassesSum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                                  arr[i + 1][j + 1] + arr[i + 2][j] +
                                  arr[i + 2][j + 1] + arr[i + 2][j + 2])
    return max(hourglassesSum)