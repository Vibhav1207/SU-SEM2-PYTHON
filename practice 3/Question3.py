def count_word_frequency(feedback):
    words = feedback.lower().split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

feedback = input("Enter customer feedback: ")

result = count_word_frequency(feedback)

print("\nWord Frequency:")
for word, count in result.items():
    print(word, ":", count)