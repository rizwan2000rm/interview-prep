def quickSort(array, start, end):
    if start >= end:
        return
    index = partition(array, start, end)

    quickSort(array, start, index - 1)
    quickSort(array, index + 1, end)

    return array


def partition(array, start, end):
    pivot = array[end]
    partitionIndex = start

    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[partitionIndex] = array[partitionIndex], array[i]
            partitionIndex += 1

    array[partitionIndex], array[end] = array[end], array[partitionIndex]
    return partitionIndex


print(quickSort([3, 1, -1, 0, 2, 5], 0, 5))
