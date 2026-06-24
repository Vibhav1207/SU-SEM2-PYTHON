dept1 = {}
n1 = int(input("Enter number of employees in Department 1: "))

for i in range(n1):
    key = input("Enter employee ID: ")
    value = input("Enter employee name: ")
    dept1[key] = value

dept2 = {}
n2 = int(input("Enter number of employees in Department 2: "))

for i in range(n2):
    key = input("Enter employee ID: ")
    value = input("Enter employee name: ")
    dept2[key] = value

merged = dept1.copy()
merged.update(dept2)

print("Merged Employee Database:")
print(merged)