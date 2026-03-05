"""
3. Attendance Monitoring System (Loops + Conditionals)
A college wants to identify students who are defaulters (attendance < 75%).
Scenario:
You are building a program where the user enters attendance percentages for 10 students.
Task:
•	Use a loop to process all students.
•	Print the students who have attendance below 75%.
Question:
Write a Python program using a loop and conditional statement to identify defaulter students.

"""
students = []
for i in range(10):
    attendance = float(input("Enter attendance percentage for student {}: " .format(i+1)))
    students.append(attendance)

print("------------------------------")
print(students)

print("------------------------------")
print("Students with attendance below 75%:")

for i in range(10):
    if students[i] < 75:
        print("Student {}: {}%".format(i+1, students[i]))