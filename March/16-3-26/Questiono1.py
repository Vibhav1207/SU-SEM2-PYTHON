"""
Create a dict with name studnets take student name input and  marks  input  in form of list of multiple students then ask user to give a inut of a partiulaur student and then display the students avg marks 
try the error blocks if the student name does not exit then throw/handle the error

"""
students = {}
while True:
    name = input("Enter student name : ")
    marks = input("Enter marks separated by commas: ")
    try:
        marks_list = list(map(float, marks.split(',')))
        total = sum(marks_list)
        average = total / len(marks_list)
        students[name] = {
            'marks': marks_list,
            'total': total,
            'average': average
        }
    except ValueError:
        print("Invalid marks input. Please enter numbers separated by commas.")
        continue
    more = input("Do you want to add another student? (yes/no): ")
    if more.lower() != 'yes':
        break
    