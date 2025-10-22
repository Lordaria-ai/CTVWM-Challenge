print("---------WELCOME TO LORDISH BANKING SYSTEM----------")
print("ACCOUNT CREATION")
username = input("Choose a username: ")
password = input("Enter a password: ")
if len(password) < 7:
    print("Password must be seven(7) charaters long!")
    account_creation = False
else:
    confirm_password = input("Confirm your password: ")
if password != confirm_password:
    print("Password does not match.")
    account_creation = False
else:
    print("Account created successfully!!")


    #LOGIN PAGE

print("--------LOGIN PAGE-------")
login_username = input("Enter your username: ")
login_password = input("Enter your password: ")
if login_username == username and login_password == password:
    print(f"CONGRATULATION....... {username}!!!. You have sucessfully logged in.")
elif login_username != username:
    print("Username not found!")
elif login_password != password:
    print("Incorrect password!")
else:
    print("Username not found and password incorrect")
