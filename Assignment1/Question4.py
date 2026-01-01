#Write a program to find the greater of two numbers.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1>number2:
    print(number1,"is greater than",number2)
elif number2>number1:
    print(number2,"is greater than",number1)
else:
    print("Both",number1,"and",number2,"are same")