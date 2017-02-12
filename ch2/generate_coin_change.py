def generate_coin_change(cents):
    currency = [
            {'cent': 'quarters', 'amount': 25},
            {'cent': 'dimes', 'amount': 10},
            {'cent': 'nickels', 'amount': 5},
            {'cent': 'pennies', 'amount': 1}
            ]
    coins = []
    for data in currency:
        coin_count = 0
        while cents >= data['amount']:
            cents -= data['amount']
            coin_count += 1
        coins.append(coin_count)
    return coins

print generate_coin_change(99)
