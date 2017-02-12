def parens_valid(string):
    opened = 0
    closed = 0
    for i in range(0, len(string)):
        if string[i] == ')' and opened == 0:
            return False
        elif opened < closed:
            return False
        elif string[i] == '(':
            opened += 1
        elif string[i] == ')':
            closed += 1
    if opened == closed:
        return True

example = parens_valid('()this is  (a tes)t (string)')
print example
