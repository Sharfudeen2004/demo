

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
else:
    if age >= 13 and age <= 19:
        print("Teen")
    else:
        if age >= 20 and age <= 59:
            print("Adult")
        else:
            print("Senior Citizen")
