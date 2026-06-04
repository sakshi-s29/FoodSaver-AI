while True:
    print("\n===== FoodSaver AI =====")
    print("1. Add Food Item")
    print("2. View Food Items")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Add Food Item")
    elif choice == "2":
        print("View Food Items")
    elif choice == "3":
        break
    else:
        print("Invalid Choice")