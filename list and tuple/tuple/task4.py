n=('a','b','f','f','f')
count=0
for i in n:
    if n.count(i)>1:
        count+=1
print(count)
