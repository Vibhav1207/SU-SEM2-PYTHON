messages = ["need refund", "hello", "manager needed", "ok"]
urgent = []

for msg in messages:
    if "broken" in msg or "refund" in msg or "manager" in msg:
        urgent.append(msg)

print(urgent)
