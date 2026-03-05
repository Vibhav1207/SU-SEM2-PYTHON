"""
1. Student Marks Analyzer (Variables, Data Types, Operators)
A teacher wants to automatically calculate the average marks of a student and determine whether the student has passed or failed.
Scenario:
You are developing a small Python program for a school system. The program should take marks of 3 subjects as input and calculate the total and average.
Task:
1.	Store marks in variables.
2.	Calculate the total and average.
3.	Display the result.
Question:
Write a Python program that:
•	Takes three subject marks as input
•	Calculates the total and average
•	Prints the results

"""


sub1 = float(input("Enter marks obtained in first subject : "))
sub2 = float(input("Enter marks obtained in second subject : "))
sub3 = float(input("Enter marks obtained in third subject : "))

print("------------------------------")

total = sub1 + sub2 + sub3

avg = total / 3

if sub1 >= 10 and sub2 >= 10 and sub3 >= 10:
    print("Result: PASS")
else:
    print("Result: FAIL")