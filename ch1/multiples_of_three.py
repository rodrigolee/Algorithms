def multiples_of_three():
    for i in range(-300, 1, 3):
        if i == -3 or i == -6:
            continue
        else:
            print i

example = multiples_of_three()
print example
