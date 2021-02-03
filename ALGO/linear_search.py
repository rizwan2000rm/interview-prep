def linearSearch(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return None


print(linearSearch([2, 5, 3, 15, 64], 64))
