#print l1 = [10,20,30,40,50,60,70,80,90,100] using for and while loop
l1 = [10,20,30,40,50,60,70,80,90,100]
print("Using for loop:")
for item in l1:
    print(item, end=" ")
print("\nUsing while loop:")
i = 0
while i < len(l1):
    print(l1[i], end=" ")
    i += 1