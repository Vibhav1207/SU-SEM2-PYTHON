# Python Programming – Section B (Short Answer Questions)

Exam-oriented short answers and basic programs (about 5 marks each).

## Section B – Table of Questions

| Q.No | Question |
| ---- | -------- |
| 1 | Explain variables with an example |
| 2 | Explain different data types in Python |
| 3 | Write a program to add two numbers |
| 4 | Explain if–else statement with syntax |
| 5 | Difference between break and continue |
| 6 | Explain while loop with example |
| 7 | What is a list? Explain any two list operations |
| 8 | Explain string slicing with example |
| 9 | What is the use of import math? |
| 10 | Program to check whether a number is positive or negative |

---

## B1. Explain variables with an example.
A variable is a name given to a memory location used to store data values. Python is dynamically typed, so the data type is decided at runtime.

Example:
```python
age = 18
name = "Vibhav"
print(age)
print(name)
```

## B2. Explain different data types in Python.
Common data types:
- int – whole numbers (10, -5)
- float – decimal values (3.14, 2.5)
- str – text data ("Python")
- list – ordered, mutable collection ([1, 2, 3])
- tuple – ordered, immutable collection
- dict – key-value pairs

## B3. Write a program to add two numbers.
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum =", sum)
```

## B4. Explain if–else statement with syntax.
Use if–else for decision making. One block runs when the condition is true; the other runs when false.

Syntax:
```python
if condition:
    statements
else:
    statements
```

## B5. What is the difference between break and continue?
- break: terminates the loop completely and moves control outside the loop.
- continue: skips the current iteration and moves to the next iteration.

## B6. Explain while loop with example.
A while loop repeats while its condition stays true.

Example:
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

## B7. What is a list? Explain any two list operations.
A list is an ordered, mutable collection.

Two operations:
- append() adds an element to the end.
- remove() deletes the first matching element.

Example:
```python
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
```

## B8. Explain string slicing with example.
Slicing extracts a portion of a string using indexes.

Example:
```python
s = "Python"
print(s[1:4])  # yth
```

## B9. What is the use of import math?
import math loads Python's math module, giving access to sqrt, pow, factorial, sin, cos, etc.

Example:
```python
import math
print(math.sqrt(16))
```

## B10. Program to check whether a number is positive or negative.
```python
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive number")
else:
    print("Negative number")
```
