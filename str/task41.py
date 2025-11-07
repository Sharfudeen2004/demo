s = "Python is a Programming Language Developed by Guido van Rossum"
words = s.split()

for word in words:
    if word[0].isupper():
        print(word)
