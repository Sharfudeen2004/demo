s = input("Enter a sentence: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""

for ch in s:
    if ch not in punctuations:
        result += ch

print(result)
