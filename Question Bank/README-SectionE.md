# Python Programming – Section E (Logical and Practice Problems)

Practice-oriented logical programs.

### E1. Program to check whether a number is prime
```python
n = int(input("Enter a number: "))
flag = True

if n <= 1:
    flag = False
else:
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

if flag:
    print("Prime number")
else:
    print("Not a prime number")
```

### E2. Program to find factorial of a number using while loop
```python
n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact = fact * n
    n -= 1

print("Factorial =", fact)
```

### E3. Program to check whether a string is palindrome
```python
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")
```

### E4. Program to count vowels in a string
```python
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)
```

### E5. Program to display even numbers from a list
```python
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    if i % 2 == 0:
        print(i)
```
