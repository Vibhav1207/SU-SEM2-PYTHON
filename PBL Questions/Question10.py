expected = (10, 20, 30)
actual = (8, 20, 25)

loss = {}

for i in range(len(expected)):
    if actual[i] < expected[i]:
        loss[i] = expected[i] - actual[i]

print(loss)