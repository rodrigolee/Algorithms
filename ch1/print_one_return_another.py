def print_one_return_another(arr):
    print arr[len(arr)-2]
    for i in range(0, len(arr)):
        if arr[i] % 2 != 0:
            return arr[i]

example = print_one_return_another([2, 2, 23, 2, 1, 3])
print example
