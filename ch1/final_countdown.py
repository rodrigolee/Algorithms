def final_countdown(param1, param2, param3, param4):
    while (param2 <= param3):
        if param2 % param1 == 0 and param2 != param4:
            print param2
        param2 += 1

example = final_countdown(3, 5, 17, 9)
print example
