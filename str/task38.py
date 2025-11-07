s = "PyTh0n123 i5 Aw3some!"
result = ''.join(ch for ch in s if not ch.isdigit())
print(result)
