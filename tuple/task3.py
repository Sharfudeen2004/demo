a=('A','b','c','C')
b=list(a)
b.sort()
print(b)
b.sort(key=len)
print(b)
b.reverse()
print(b)
b.sort(reverse=True)
print(b)


