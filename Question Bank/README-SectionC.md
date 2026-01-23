# Python Programming – Section C (Programming Questions)

Exam-ready Python programs (about 5 marks each).

## Section C – Programming Questions

### C1. Accept two numbers and print sum, difference, product, and division
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Division =", a / b)
```

### C2. Check whether a number is even or odd
```python
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### C3. Find the largest of three numbers using elif
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("First number is largest")
elif b > c:
    print("Second number is largest")
else:
    print("Third number is largest")
```

### C4. Print numbers from 1 to 10 using while loop
```python
i = 1
while i <= 10:
    print(i)
    i += 1
```

### C5. Program to demonstrate the use of break statement
```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

### C6. Program to demonstrate the use of continue statement
```python
for i in range(1, 11):
    if i == 6:
        continue
    print(i)
```
