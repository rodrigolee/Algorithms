def sigma(number):
    sum = 0
    for i in range(0, number+1):
        sum += i
    return sum

example = sigma(5)
print example
