for i in range(0,6):
    for j in range(0,i+1):
        if j==0 or j==i or i==6 or i==6-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
