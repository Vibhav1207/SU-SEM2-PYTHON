#write program to print sum of first n natural numbers
number = int(input("Enter a number: "))
sum = 0
for i in range(1 , number+1):
    sum = sum + i
print("Sum of first",number,"natural numbers is:",sum)