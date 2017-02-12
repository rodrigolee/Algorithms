def countdown(number):
    new_arr = []
    for i in reversed(xrange(number+1)):
        new_arr.append(i)
    print 'Array length is', len(new_arr)
    return new_arr

example = countdown(10)
print example
