prices = [500, 1500, 6000]
new_prices = []
savings = 0

for p in prices:
    if p > 5000:
        np = p * 0.8
    elif p > 1000:
        np = p * 0.9
    else:
        np = p

    new_prices.append(np)
    savings += (p - np)

print("Savings:", savings)