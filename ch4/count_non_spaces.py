def count_non_spaces(string):
    count = 0;
    for i in range(0, len(string)):
        if string[i] != ' ':
            count += 1
    return count

example = count_non_spaces('Honey pie, you are driving me crazy')
print example
