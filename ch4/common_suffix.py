def common_suffix(arr):
    suffix = ''
    count = 0
    while True:
        for i in range(0, len(arr)-1):
            if arr[i][len(arr[i])-1-count] == arr[i+1][len(arr[i+1])-1-count]:
                continue
            elif arr[i][len(arr[i])-1-count] != arr[i+1][len(arr[i+1])-1-count] and count == 0:
                return ''
            elif arr[i][len(arr[i])-1-count] != arr[i+1][len(arr[i+1])-1-count]:
                return suffix[::-1]             # reverse string
        suffix += arr[0][len(arr[0])-1-count]
        count += 1
    return

example = common_suffix(['st', 'rest', 'chest'])
print example
