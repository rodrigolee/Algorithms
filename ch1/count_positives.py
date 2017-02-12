def count_positives(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr

example = count_positives([-1, 1, 1, 1])
print example
