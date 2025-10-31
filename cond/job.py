
age = int(input("Enter your age: "))
experience = input("Do you have experience? (yes/no): ")


if age > 18:
    
    if experience.lower() == "yes":
        print("You are eligible for the job.")
    else:
        print("You must have experience to be eligible for the job.")
else:
    print("You must be above 18 years old to apply for the job.")
