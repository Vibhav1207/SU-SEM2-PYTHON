steps = [12000, 15000, 8000, 11000, 13000]
streak = 0
max_streak = 0

for s in steps:
    if s >= 10000:
        streak += 1
        max_streak = max(max_streak, streak)
    else:
        streak = 0

print("Max streak:", max_streak)