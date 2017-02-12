def flexible_countdown(low, high, mult):
    for i in range(high, low-1, -1):
        if i % mult == 0:
            print i

example = flexible_countdown(2, 9, 3)
print example
