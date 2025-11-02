m1 = float(input("Enter mark for Subject 1: "))
m2 = float(input("Enter mark for Subject 2: "))
m3 = float(input("Enter mark for Subject 3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")
    avg = (m1 + m2 + m3) / 3
    if avg >= 90:
        print("Outstanding")
else:
    print("Fail")
