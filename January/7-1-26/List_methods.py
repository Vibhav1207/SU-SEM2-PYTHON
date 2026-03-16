l1 = list()
print(l1)  # Output: [] prints a empty list

print("--------------------------------------")

l1 = list("sanjivani")
print(l1)

print("--------------------------------------")

l1 = list((10, 20, 30, 40, 50))
print(l1)

print("--------------------------------------")

l11 = [1 ,2 ,3]
l22 = [2 , 3,1]
l33 = [1 , 2, 3, 4, 5]
l44 = [1 , 2, 3]

print(l11 == l22)
print(l11 > l22)
print(l22 == l33)
print(l11 == l44)

print("--------------------------------------")

l13 = [1 ,2 ,3]
l23 = [2 , 3,1]
l43 = [1 , 2, 3]

l33 = l13 + l23
print(l33)

print("--------------------------------------")

l14 = [1 ,2 ,3]
l24 = [2 , 3,1]
l44 = [1 , 2, 3]

 # * is not a multiplaction operator here it is a repetition operator
print([2,4] * 2)

print("--------------------------------------")

l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(l1[2][2])

print("--------------------------------------")

l1 = [1,2,3,4]
l1.append(5)
print(l1)
l1.insert(2, 30)
print(l1)
l1.remove(3)
print(l1)
l1.pop()
print(l1)
l1.pop(2)
print(l1)

l3 = l1.pop(1)
print(l3)
# how to return a remeoved element by pop
