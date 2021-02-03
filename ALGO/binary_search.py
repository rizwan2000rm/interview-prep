def binarySearch(array, key):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = array[mid]

        # Guess => low
        if guess < key:
            start = mid + 1
        # Guess => High
        elif guess > key:
            end = mid - 1
        else:
            return mid

    return None


print(binarySearch([2, 5, 3, 15, 64], 64))
