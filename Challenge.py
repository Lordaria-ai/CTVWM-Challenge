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
