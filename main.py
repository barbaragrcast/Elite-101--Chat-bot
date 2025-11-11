Account_List = {}


def information():
    while True:
        print("\n__________________________________")
        print("\n        ACCOUNT INFORMATION")
        print("__________________________________\n") 
        print("There are 4 main types of bank accounts.")
        print("1. Savings Account")
        print("2. Checking Account")
        print("3. Money Market Account")
        print("4. Certificate of Deposit (CD) Account")
        print("5. Exit Account Information Menu")
        accountChoice = input("\nSelect an option (1-5) to learn more:\n") 

        if accountChoice == "1":
            print("\n__________________________________\n")
            print("A savings account is a type of bank account where you store money safely and earn interst over time.")
            print("You can deposit money into it whenever you want and withdraw it when you need it,\nbut it’s mainly meant for saving, not daily spending")

        elif accountChoice == "2":
            print("\n__________________________________\n")
            print("You use it to pay bills, buy things, or get cash.\nThe money in it is easy to access anytime using a debit card, checks, or online payments.")
        elif accountChoice =="3":
            print("\n__________________________________\n")
            print("A money market account is a mix between a savings account and a checking account.\nIt usually gives you higher interest (so your money grows faster than in a regular savings account),\nbut it might also have limits on how often you can take money out.")

        elif accountChoice == "4":
            print("\n__________________________________\n")
            print("a type of savings account where you agree to leave your money in the bank for a set amount of time\n(like 6 months, 1 year, or more)")

        elif accountChoice =="5":
            break 
        else:
            print("Please enter a valid number from 1-5")


def create_account():
    print("\n__________________________________")
    print("\n        ACCOUNT SELECTION")
    print("__________________________________")
    print("Please choose the type of account you want to open:\n")
    print("1. Savings Account")
    print("2. Checking Account")
    print("3. Money Market Account")
    print("4. Certificate of Deposit (CD) Account")

    accounts = {    
        "1": "Savings account",
        "2": "Checking account",
        "3": "Money Market account",
        "4": "Certificates of Deposit account"
    }

    choice = input("\nEnter the number of your chosen account: ")

    if choice in accounts:
        print(f"You have chosen a {accounts[choice].lower()}\n")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    print("Lets start with the username")
    user_name = input("Please enter an username: ")
    while True:
        password = input("Enter password: ")
        length = len(password)
        def speacial_characters(password):
            for char in password:
                 if char.isdigit() or not char.isalnum():
                    return True
            return False
        if length < 8:
            print("Your password must be at leat 8 characters long")
        elif speacial_characters(password) == False:
            print("Please use a speacial character, or a number in your password")
        elif password == password.lower():
            print("Please add captial letters")
        else:
            Account_List[user_name] = {
                "password": password,
                "account_type": accounts[choice]
            }
            print(f"You have created your account successfully. Welcome, {user_name}!")
            break

def view_account():
    user_name = input("Enter username: ")
    if user_name in Account_List:
        user_info = Account_List[user_name]
        while True:
            password = input("Enter password: ")
            if password == user_info['password']:
                print("\n__________________________________")
                print("\n         ACCOUNT INFORMATION")
                print("__________________________________\n")   
                print(f"Username: {user_name}")
                print(f"Account Type: {user_info['account_type']}")
                print(f"Password: {user_info['password']}\n")
                break
            else:
                print("Incorrect password, please try again:")

    else:
        print("No account found with that username.")


print("Welcome to Bank of America")
print("As a new user, we are here to help setting up your first account")
name = input("Please enter your name: ")
while True:
    age = input(f"\nHello {name}, please enter your age: ")
    try:
        age = int(age)
        break
    except ValueError:
        print("Please enter a valid number")

if age <= 18:
    print("Sorry, you are to young to acess this service")
    exit()


while True:
    print("\n__________________________________")
    print("\n            MAIN MENU")
    print("__________________________________\n")   
    print("1. Learn about account types")
    print("2. Create a new account")
    print("3. View existing account")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        information()
    elif choice == "2":
        create_account()
    elif choice == "3":
        view_account()
    elif choice == "4":
        print("You have exited")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")