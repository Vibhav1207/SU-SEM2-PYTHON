#Write a program to take subject input of 2 students and only give output of common subjects using .intersection() method of set

student1 = set(input("Enter the subjects of Student 1: ").split(","))
student2 = set(input("Enter the subjects of Student 2: ").split(","))

common = student1.intersection(student2)
print("Common Subjects: ", common)