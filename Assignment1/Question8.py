#Write a program to display grade based on marks obtained by a student

marks = float(input("Enter marks obtained: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'

print(f"Marks: {marks}")
print(f"Grade: {grade}")
