text = input("Enter a word: ").lower()

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in text:
    if char in vowels:
        vowels[char] += 1

print(vowels)