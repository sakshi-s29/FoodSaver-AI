import csv

def add_food():
    food_name = input("Enter Food Name: ")
    quantity = input("Enter Quantity: ")
    expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ")

    with open("food_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([food_name, quantity, expiry_date])

    print("Food Item Added Successfully!")

while True:
    print("\n===== FoodSaver AI =====")
    print("1. Add Food Item")
    print("2. View Food Items")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        print("View Food Items")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")