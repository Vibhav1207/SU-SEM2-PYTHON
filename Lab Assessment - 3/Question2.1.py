"""
Tomorrow’s Task:

Modify the ATM Withdrawal program to allow for three successive transactions. The first two transactions should be successful, while the third transaction should be declined. Utilize functions to achieve this functionality.
"""

bal = float(input("Enter your account balance: "))

def withdraw_amount(bal, amount, tra_num):
    if tra_num <= 2:
        if amount <= bal:
            bal -= amount
            print("Withdrawal successful!")
            print("Your balance after withdrawal is:", bal)
        else:
            print("Insufficient Balance")
            
        return bal
    elif tra_num == 3:
        print("Transaction declined! Only 2 transactions are allowed.")
        print("Your balance is:", bal)
        return bal

for i in range(1, 4):
    print(f"--- Transaction {i} ---")
    amount = float(input("Enter the amount to withdraw: "))
    bal = withdraw_amount(bal, amount, i)
    
