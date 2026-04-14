temps = [10, 20, 35, 40, 38, 32]

cold, hot, moderate = [], [], []

for t in temps:
    if t < 15:
        cold.append(t)
    elif t > 30:
        hot.append(t)
    else:
        moderate.append(t)

# check consecutive hot days
count = 0
for t in temps:
    if t > 30:
        count += 1
        if count > 3:
            print("Warning: Too many hot days")
            break
    else:
        count = 0

print(cold, hot, moderate)