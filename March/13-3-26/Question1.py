"""
CREATE A dictionary of students - wherein you are getting name, [marks], total, average and the result. and attach the screenshot of code and output with your name and PRN - submit here -> 
Passing critera 35 which should be outside the disctinary

take input for multiple students and stroe evertying total and all in dictinonary show the reuslt if pass or fail do not directly quit

"""
students = {}
passing_criteria = 35
while True:
    name = input("Enter student name : ")
    marks = list(input("Enter 3 subject marks of the student seprated by comma : "))
    try:
        marks_list = list(map(float, marks(',')))
        total = sum(marks_list)
        average = total / len(marks_list)
        result = "Pass" if average >= passing_criteria else "Fail"
        students[name] = {
            'marks': marks_list,
            'total': total,
            'average': average,
            'result': result
        }
    except ValueError:
        print("Invalid marks input. Please enter numbers separated by commas.")
        continue
    more = input("Do you want to add another student? (yes/no): ")
    if more.lower() != 'yes':
        break
student_name = input("Enter the name of the student to view details: ")
try:
    student_info = students[student_name]
    print(f"Name: {student_name}")
    print(f"Marks: {student_info['marks']}")
    print(f"Total: {student_info['total']}")
    print(f"Average: {student_info['average']}")
    print(f"Result: {student_info['result']}")
except KeyError:
    print("Student not found. Please check the name and try again.")
