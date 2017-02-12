def remove_even_length_strings(arr):
    removed_strings = []
    for i in range(0, len(arr)):
        if len(arr[i]) % 2 == 0:
            removed_strings.append(arr[i])
    for j in range(0, len(removed_strings)):
        arr.remove(removed_strings[j])
    return arr

example = remove_even_length_strings(['hello', 'test', 'one', 'two', 'five', 'four'])
print example
