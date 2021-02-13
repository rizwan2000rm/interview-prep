def rotLeft(a, d):
    end = len(a) - 1
    reverse(a, 0, end)
    reverse(a, len(a) - d, end)
    reverse(a, 0, len(a) - d - 1)
    return a


def reverse(array, start, end):
    while (start < end):
        temp = array[end]
        array[end] = array[start]
        array[start] = temp
        start += 1
        end -= 1
    return array


# value = rotLeft([33, 47, 70, 37, 8, 53, 13,
#                  93, 71, 72, 51, 100, 60, 87, 97], 13)
# print(value)
# print(value == [87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60])
