"""
2. ATM Withdrawal System (Conditional Statements)
A bank ATM must decide whether a withdrawal request should be allowed.
Scenario:
A user enters their account balance and the withdrawal amount. The ATM must check whether the withdrawal can be processed.
Task:
•	If the withdrawal amount is less than or equal to the balance, allow withdrawal.
•	Otherwise display “Insufficient Balance”.
Question:
Write a Python program that simulates this ATM decision using if-else statements.

"""

bal = float(input("Enter your account balance: "))
withdraw = float(input("Enter the withdrawal amount:"))

print("------------------------------")

print("Your current balance is :",bal)
print("The amount you want to withdraw is: ",withdraw)

print("------------------------------")
if withdraw <= bal:
    bal = bal - withdraw
    print("Withdrawal successful!")
    print("Your balance after witdrawal is : ", bal)

else:
    print("Insufficient Balance")