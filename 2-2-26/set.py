#SET

s1 = {10,20,30,40}
print(type(s1))
print(s1) # set is unordered collection of unique items
print("--------------------------------------------")
s2 = {10,20,30,40,10,20}
print(s2) # set will not allow duplicate items
print("--------------------------------------------")
s1 = {}
print(type(s1)) # this is dictionary not set
print("--------------------------------------------")
s1 = set()
print(type(s1))
print("--------------------------------------------")
s1 = set({10,20,30})
print(s1)
print("--------------------------------------------")
s1 = set("Vibahv")
print(s1)
print("--------------------------------------------")
