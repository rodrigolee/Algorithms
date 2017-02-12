def print_low_return_high(arr):
    min = arr[0]
    max = arr[0]
    for i in range(0, len(arr)):
        if min > arr[i]:
            min = arr[i]
        elif max < arr[i]:
            max = arr[i]
    print 'The lowest value is', min
    return max

example = print_low_return_high([7, 15, 2, 9, 10, 3, 4])
print example
