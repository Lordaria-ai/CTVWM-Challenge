# Welcome message
print("---------WELCOME TO LORDISH BANKING SYSTEM----------")

# -------------------- ACCOUNT CREATION --------------------

account_creation= True
while True:
    print("------------ACCOUNT CREATION-----------")
    username = input("Choose a username: ").title()
    password = input("Enter a password: ")

    # Password validation
    if len(password) < 5:
        print("Password must be at least 5 charaters long!")
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

    # -------------------- LOGIN SECTION --------------------
if account_creation:
    while True:
        print("\n\n--------LOGIN PAGE-------")
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


balance = float(100000) #Default account balance
attempts = 3 #PIN login attempts

# -------------------- PIN CREATION --------------------

while True:
    print("\n\n=====PIN CREATION======")
    #For more security
    create_pin = input("\n\nCreate a 4-digit PIN: ")
    
    if len(create_pin) != 4 or not create_pin.isdigit():
        print("PIN must be exactly 4-digits long. TRY AGAIN!!!")
        pin_creation = False
    else:
        print("PIN created successfully!\n")
        break
# -------------------- PIN LOGIN --------------------
# Ask user to log in with pin with 3 attempts.
while attempts > 0:
    pin = input("Enter your PIN to log in: ")
    if pin == create_pin:
        print("PIN accepted!! Access granted\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.\n")
else:
    print("Too many incorrect attempts.Your account has been locked. ")
    exit() # Ends program when the pin is entered wrongly 3 times.

# -------------------- BANKING MENU --------------------
while True:
    print("Select an option to proceed:")
    print("A. Check Balance")
    print("B. Deposit Money")
    print("C. Withdraw Money")
    print("D. Loggout")

    choice = input("\nEnter your choice: ").title()
    if choice == "A":
        print(f"Your account balance is: ${balance}.")
    elif choice == "B":
        amount = float(input("Enter amount to deposit into your account: "))
        balance += amount
        print(f"${amount} deposited succesfully. New balance: ${balance}")
    elif choice == "C":
        amount = float(input("Enter amount your want to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"${amount} withdrawn successfully. New balance: ${balance}")
    elif choice == "D":
        confirm = input("Are you sure you want to logout? (yes/no): ").lower()
        if confirm == "yes":
            print("\n======== SESSION SUMMARY ========")
            print(f"Account Holder: {username}")
            print(f"Final Balance: ${balance}")
            print("Transaction session ended successfully.")
            print("Thank you for using Lordish Bank! HAVE A NICE DAY!!\n")
            exit()
        else:
            print("Returning to main menu...")
    else:
        print("Invalid choice. Please try again.")
       