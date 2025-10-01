print("Welcome to American Bank")
print("As a new user, we are here to help setting up your first account")
name = input("Please enter your name: ")
age = int(input(f"Hello {name}, please enter your age: "))

if age <= 18:
    print("Sorry, you are to young to acess this service")


while True:
    print("Choose an option")
    print("1. Types of accounts")
    print("2. Create account")
    print("3. View account")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("There are 4 main types of bank accounts. ")
        print("1. Savings account ")
        print("2. Checking account ")
        print("3. Money Market account ")
        print("1. Certificates of Deposit account ")
        accountChoice = input("please chose one you will like to know more about:")
    elif choice == "2":
        print("You picked Option 2")
    elif choice == "3":
        print("You picked Option 3")
    elif choice == "4":
        print("You have exited")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")