students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

rank = 1
for name, marks in sorted_students:
    print("Rank", rank, ":", name, "-", marks)
    rank += 1