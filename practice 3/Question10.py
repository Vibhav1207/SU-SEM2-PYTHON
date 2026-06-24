students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter 3 subject marks: ").split()))
    students[name] = marks

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(name, "Average Marks:", avg)