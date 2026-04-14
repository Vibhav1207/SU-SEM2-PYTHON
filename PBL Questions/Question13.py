calls = {"123": 5, "456": 15}
queue = []

for num, time in calls.items():
    if time > 10:
        queue.append(num)

print(queue)