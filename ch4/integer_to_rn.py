def integer_to_rn(integer):
    roman_numerals = [
            {'rn': 'M', 'value': 1000},
            {'rn': 'CM', 'value': 900},
            {'rn': 'D', 'value': 500},
            {'rn': 'CD', 'value': 400},
            {'rn': 'C', 'value': 100},
            {'rn': 'XC', 'value': 90},
            {'rn': 'L', 'value': 50},
            {'rn': 'XL', 'value': 40},
            {'rn': 'X', 'value': 10},
            {'rn': 'IX', 'value': 9},
            {'rn': 'V', 'value': 5},
            {'rn': 'IV', 'value': 4},
            {'rn': 'I', 'value': 1}
            ]
    rn_str = ''
    for data in roman_numerals:
        while integer >= data['value']:
            rn_str += data['rn']
            integer -= data['value']
    return rn_str

example = integer_to_rn(2017)
print example
