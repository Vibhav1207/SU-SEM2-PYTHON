s = {8,1,5,9,10}

print(s)
s.add(11)
print(s)
s.update({2, 3})
print(s)
s.discard(1)
print(s)

print("--------------------------------------------")

s = {8,1,5,9,10}
s.add((11,12))
print(s)
s.update({(2,3), (4,5)})
print(s)