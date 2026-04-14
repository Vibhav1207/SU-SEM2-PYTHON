expenses = {}

while True:
    cat = input("Enter category (DONE to stop): ")
    if cat == "DONE":
        break
    amt = int(input("Amount: "))

    if cat in expenses:
        expenses[cat] += amt
    else:
        expenses[cat] = amt

print(expenses)