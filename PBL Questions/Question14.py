votes = ["A", "B", "A", "C", "A", "B"]
count = {}

for v in votes:
    count[v] = count.get(v, 0) + 1

winner = ""
max_votes = 0

for k, v in count.items():
    if v > max_votes:
        max_votes = v
        winner = k

print("Winner:", winner)