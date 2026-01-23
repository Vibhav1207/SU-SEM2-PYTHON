# Python Programming – Section D (Arithmetic Problems)

Short arithmetic-focused programs.

### D1. Program to calculate the area of a circle
```python
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area of circle =", area)
```

### D2. Program to calculate simple interest
```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)
```

### D3. Program to calculate the average of three numbers
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

avg = (a + b + c) / 3
print("Average =", avg)
```

### D4. Program to convert Celsius to Fahrenheit
```python
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)
```

### D5. Program to find quotient and remainder
```python
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

print("Quotient =", a // b)
print("Remainder =", a % b)
```
