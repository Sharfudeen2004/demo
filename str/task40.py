s = "abc123xyz"
numbers = ''.join(ch for ch in s if ch.isdigit())
print(numbers)
