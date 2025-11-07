sentence = input("Enter a sentence: ")
sentence = sentence.lower()
letter_count = {}
for ch in sentence:
    if ch.isalpha():
        if ch in letter_count:
            letter_count[ch] += 1
        else:
            letter_count[ch] = 1
for letter, count in letter_count.items():
    print(letter, ":", count)
