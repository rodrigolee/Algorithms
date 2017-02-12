def leap_year(year):
    if year % 400 == 0:
        print str(year) + ' is a leap year'
    elif year % 4 == 0 and not year % 100 == 0:
        print str(year) + ' is a leap year'
    else:
        print str(year) + ' is not a leap year'

example = leap_year(400)
print example
