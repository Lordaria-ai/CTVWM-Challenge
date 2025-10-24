print("---------WELCOME TO LORDISH BANKING SYSTEM----------")
account_creation= True
while True:
    print("---------ACCOUNT CREATION---------")
    username = input("Choose a username: ").title()
    password = input("Enter a password: ")
    if len(password) < 7:
        print("Password must be at least seven(7) charaters long!")
        account_creation = False
    else:
        confirm_password = input("Confirm your password: ")
        if confirm_password != password:
                print("Password does not match. TRY AGAIN!!!!")
                account_creation = False
        else:
            print(f"Account for {username} created successfully!!")
            account_creation = True
            break

    #LOGIN PAGE
if account_creation:
    while True:
        print("\n\n\--------LOGIN PAGE-------")
        login_username = input("Enter your username: ").title()
        login_password = input("Enter your password: ")
        if login_username == username and login_password == password:
            print(f"CONGRATULATION....... {username}!!!. You have sucessfully logged in.")
            account_creation = True
            break
        elif login_username != username:
            print("Username not found!")
        elif login_password != password:
            print("Incorrect password!")
        else:
            print("Username not found and password incorrect.")
else:
        print("Account not logged in successfully.")        


balance = 100,000
attempts = 3
while True:
    print("\n\n=====PIN CREATION======")
    #For more security
    create_pin = input("\n\nCreate a 4-digit PIN: ")
    
    if len(create_pin) < 4 or len(create_pin) > 4:
        print("PIN must be exactly 4-digits long. TRY AGAIN!!!")
        pin_creation = False
    else:
        print("PIN created successfully!\n")
        break

# Ask user to log in with pin with 3 attempts.
while attempts > 0:
    pin = input("Enter your PIN to log in: ")
    if pin == create_pin:
        print("PIN accepted!!\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.\n")
else:
    print("Too many incorrect attempts.Your account has been locked. ")
    exit() # Ends program when the pin is entered wrongly 3 times.

#BANKING MENU
