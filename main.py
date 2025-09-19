print("Welcome to our amusement Park!")
name = input("Please enter your name: ")
age = input(f"Hello {name}, please enter your age: ")

while True:
    print("\nEnter your choice")
    print("1. Option One (placeholder)")
    print("2. Option Two (placeholder)")
    print("3. Option Three (placeholder)")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("You picked Option 1")
    elif choice == "2":
        print("You picked Option 2")
    elif choice == "3":
        print("You picked Option 3")
    elif choice == "4":
        print("You have exited")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")