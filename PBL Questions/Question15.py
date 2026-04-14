passwords = ["abc12345", "short", "password"]

valid = []
invalid = []

for p in passwords:
    if len(p) > 8 and any(ch.isdigit() for ch in p):
        valid.append(p)
    else:
        invalid.append(p)

print("Valid:", valid)
print("Invalid:", invalid)