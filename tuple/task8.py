a=tuple(input("enter the value:"))
print(a)
b=[]
count=0
for i in a:
    if a.count(i)>1 and i not in b:
        b.append(i)
        count+=1
print("count of value",count)
print("repeded of value",b)
