print("---------WELCOME TO LORDISH BANKING SYSTEM----------")
print("ACCOUNT CREATION")
username = input("Choose a username: ")
password = getpass("Enter a password: ")
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