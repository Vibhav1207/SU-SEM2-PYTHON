students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

top_student = max(students, key=students.get)

print("Top Scoring Student:", top_student)
print("Marks:", students[top_student])