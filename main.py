import csv
from datetime import datetime

def add_food():
    food_name = input("Enter Food Name: ")
    quantity = input("Enter Quantity: ")
    expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ")

    with open("food_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([food_name, quantity, expiry_date])

    print("Food Item Added Successfully!")

def view_food():
    try:
        with open("food_data.csv", "r") as file:
            reader = csv.reader(file)

            print("\nFood Items:")
            print("---------------------------")

            for row in reader:
                print(f"Food: {row[0]}")
                print(f"Quantity: {row[1]}")
                print(f"Expiry Date: {row[2]}")
                print("---------------------------")

    except FileNotFoundError:
        print("No food items found.")

def recommend_food():
    try:
        with open("food_data.csv", "r") as file:
            reader = csv.reader(file)

            print("\nSmart Recommendations")
            print("---------------------------")

            for row in reader:
                food = row[0]
                expiry = row[2]

                expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
                today = datetime.today()

                days_left = (expiry_date - today).days

                if days_left <= 1:
                    recommendation = "Use Immediately"
                elif days_left <= 3:
                    recommendation = "Consume Soon"
                else:
                    recommendation = "Fresh"

                print(f"{food} -> {recommendation}")

    except FileNotFoundError:
        print("No food data found.")

while True:
    print("\n===== FoodSaver AI =====")
    print("1. Add Food Item")
    print("2. View Food Items")
    print("3. Smart Recommendations")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        view_food()

    elif choice == "3":
        recommend_food()

    elif choice == "4":
        break
        
    else:
        print("Invalid Choice")