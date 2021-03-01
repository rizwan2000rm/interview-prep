# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        num = arr[i]
        if i != num - 1:
            arr[i] = arr[num - 1]
            arr[num - 1] = num
            swaps += 1
            continue
        i += 1
    return swaps