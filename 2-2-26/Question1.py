#write a py script to remove duplicate values form  list

l = [ 10,20,30,40,50,10,60,90,90]
print("Original list:",l)
s = set(l) # set() can pass iterable sequence
print(s)
l2 = list(s)
print("List after removing duplicate values:",l2)

print("--------------------------------------------") #second method
l = [ 10,20,30,40,50,10,60,90,90]
l1 = list(set(l))
print(l1)