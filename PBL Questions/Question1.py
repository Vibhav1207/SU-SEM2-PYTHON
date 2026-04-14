dur = { 25,30,45,60,78,90,32,46}
result = {}

for i,d in enumerate(dur):
    if d < 30:
        result[i] = "Fast"
    elif 30 <= d <=60:
        result[i] = "Normal"
    else:
        result[i] = "Extended"

print(result)