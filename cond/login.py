


correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")

if username == correct_username:
    password = input("Enter password: ")
   
    if password == correct_password:
        print("Login successful! Welcome.")
    else:
        print("Incorrect password. Try again.")
else:
    print("Invalid username.")
