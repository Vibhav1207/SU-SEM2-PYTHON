n = int(input("Enter value of N: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print(squares)