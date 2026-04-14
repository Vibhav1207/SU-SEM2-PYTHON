ages = [10, 25, 65]
total = 0
prices = []

for age in ages:
    price = 200
    if age < 12:
        price *= 0.5
    elif age > 60:
        price *= 0.7

    prices.append(price)
    total += price

print("Total:", total)