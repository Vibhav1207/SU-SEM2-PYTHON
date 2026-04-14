data = {101: 20, 102: 10, 103: 18}
fines = []

for sid, days in data.items():
    if days > 14:
        fine = (days - 14) * 10
        fines.append((sid, fine))

print(fines)