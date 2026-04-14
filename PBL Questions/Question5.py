data = [(1, 15), (2, 30), (3, 25)]
warning = []
bonus = []

for emp, days in data:
    if days < 20:
        warning.append(emp)
    elif days == 30:
        bonus.append(emp)

print("Warning:", warning)
print("Bonus:", bonus)