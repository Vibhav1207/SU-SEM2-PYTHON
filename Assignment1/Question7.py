#Write a program to check whether a character is a vowel or consonant.

char = input("Enter a character: ").lower()

if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")
else:
    print("Please enter a single alphabetic character")
