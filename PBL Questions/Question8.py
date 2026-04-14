correct = {'Q1': 'A', 'Q2': 'C'}
student = {'Q1': 'A', 'Q2': 'B'}

score = 0

for q in correct:
    if student[q] == correct[q]:
        score += 2
    else:
        score -= 1

print("Score:", score)