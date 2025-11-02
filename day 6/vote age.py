
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print("You are not eligible to vote.")
    print("You have to wait", years_left, "more year(s) to become eligible.")
