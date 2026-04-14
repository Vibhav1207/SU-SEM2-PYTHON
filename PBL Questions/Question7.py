feedback = [{'rating': 4, 'comment': 'Good'},
            {'rating': 2, 'comment': 'Bad service'}]

total = 0
complaints = []

for f in feedback:
    total += f['rating']
    if f['rating'] <= 2:
        complaints.append(f['comment'])

avg = total / len(feedback)

print("Average:", avg)
print("Complaints:", complaints)