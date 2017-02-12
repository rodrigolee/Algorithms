def remove_blanks(string):
    new_string = ''
    for i in range(0, len(string)):
        if string[i] == ' ':
            continue
        else:
            new_string += string[i]
    return new_string

example = remove_blanks(' Pl      ayTha    tF  u    nkyM   u s i    c   ')
print example
