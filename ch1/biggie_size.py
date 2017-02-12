def biggie_size(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr

example = biggie_size([-1, 3, 5, -5])
print example
