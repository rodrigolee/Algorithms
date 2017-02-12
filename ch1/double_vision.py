def double_vision(arr):
    new_arr = []
    for i in range(0, len(arr)):
        new_arr.append(arr[i]*2)
    return new_arr

example = double_vision([1, 2, 3])
print example
