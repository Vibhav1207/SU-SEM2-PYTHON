#Sum of first N natural numbers

number = int(input("Enter a number: "))
i =1
sum = 0
while i <= number:
    #sum = (number * (number + 1)) // 2
    sum = sum+i
    i += 1
print("The sum of first", number, "natural numbers is:", sum)