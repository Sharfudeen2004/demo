x = ['a', 'b', 'c', 'd']

for i in range(len(x)):
    for j in range(i + 1):
        print(x[i], end=" ")
    print()
