spots = [0, 1, 1, 0, 1]

i = 0
found = False

while i < len(spots):
    if spots[i] == 0:
        spots[i] = 1
        print("Assigned spot:", i)
        found = True
        break
    i += 1

if not found:
    print("Parking Full")