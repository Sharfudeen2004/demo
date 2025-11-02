

ch = input("Enter a single alphabet letter: ")

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(ch, "is a vowel.")
    else:
        print(ch, "is a consonant.")
else:
    print("Please enter a valid single alphabet letter.")
