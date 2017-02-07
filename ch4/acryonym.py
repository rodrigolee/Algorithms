def acronym(str):
    acro = ''
    for i in range(0, len(str)):
        if str[i] == ' ' and str[i+1] != ' ':
            acro += str[i+1]
        elif i == 0 and str[i] != ' ':
            acro += str[i]
    return acro.upper()
example = acronym(' hello world - a b c d')
print example
