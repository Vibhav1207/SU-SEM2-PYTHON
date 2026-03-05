"""
4. Shopping Cart System (Lists)
An online shopping system needs to manage items in a user's cart.
Scenario:
A customer adds items to a cart, and the system must display the cart contents.
Task:
1.	Create a list of items.
2.	Allow the user to add new items.
3.	Display the updated cart.
Question:
Write a Python program that:
•	Creates a list of shopping items
•	Adds a new item using append ()
•	Prints all items in the cart.

"""

cart = ["Laptop", "Smartphone", "Headphones"]

print("Current items in the cart:")
print(cart)

print("--------------------")

iteamadd = int(input("How many items do you want to add: "))

for i in range(iteamadd):
    item = input("Enter item name {} : " .format(i+1))
    cart.append(item)

print("\nUpdated cart items:")
for item in cart:
    print(item)