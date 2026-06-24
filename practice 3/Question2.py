student1 = input("Enter subjects for Student 1 (space separated): ")
student2 = input("Enter subjects for Student 2 (space separated): ")
set1 = set(student1.split())
set2 = set(student2.split())

common_subjects = set1.intersection(set2)
unique_subjects = set1.symmetric_difference(set2)
all_subjects = set1.union(set2)

print("\nSubjects taken by both students:", common_subjects)
print("Subjects taken by only one student:", unique_subjects)
print("All subjects taken by both students:", all_subjects)