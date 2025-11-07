s = "Python123 is fun 456"
result = ''.join([i for i in s if not i.isdigit()])
print(result)
