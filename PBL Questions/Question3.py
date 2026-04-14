emails = ["free offer", "meeting update", "urgent reply", "hello"]
spam = set()
inbox = set()

for mail in emails:
    if "free" in mail or "lottery" in mail or "urgent" in mail:
        spam.add(mail)
    else:
        inbox.add(mail)

print("Spam:", spam)
print("Inbox:", inbox)