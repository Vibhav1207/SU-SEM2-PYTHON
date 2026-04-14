data = {"A": 1, "B": 3, "C": 2}

for zone in [1, 2, 3]:
    for name, z in data.items():
        if z == zone:
            print("Boarding:", name)