def setting_swapping(my_name):
    my_number = 42
    my_number, my_name = my_name, my_number
    print 'Name swapped to', my_number
    print 'Number swapped to', my_name

example = setting_swapping('Brian')
print example
