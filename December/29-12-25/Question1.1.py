#Weather given number is prime or not using while

number = int(input("Enter a number: "))
i = 2
while i < number:
    if (number % i) == 0:
        print(number, "is not a prime number")
        break
    i += 1
else:
    print(number, "is a prime number")