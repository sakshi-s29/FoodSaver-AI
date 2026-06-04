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
        
def analytics_dashboard():
    try:
        with open("food_data.csv", "r") as file:
            reader = csv.reader(file)

            total = 0
            fresh = 0
            soon = 0
            immediate = 0

            today = datetime.today()

            for row in reader:
                total += 1

                expiry_date = datetime.strptime(row[2], "%Y-%m-%d")
                days_left = (expiry_date - today).days

                if days_left <= 1:
                    immediate += 1
                elif days_left <= 3:
                    soon += 1
                else:
                    fresh += 1

            print("\n===== Analytics Dashboard =====")
            print(f"Total Food Items: {total}")
            print(f"Fresh Items: {fresh}")
            print(f"Expiring Soon: {soon}")
            print(f"Use Immediately: {immediate}")

    except FileNotFoundError:
        print("No food data found.")

def search_food():
    search_name = input("Enter Food Name to Search: ")

    try:
        with open("food_data.csv", "r") as file:
            reader = csv.reader(file)

            found = False

            for row in reader:
                if row[0].lower() == search_name.lower():
                    print("\nFood Found!")
                    print(f"Food: {row[0]}")
                    print(f"Quantity: {row[1]}")
                    print(f"Expiry Date: {row[2]}")
                    found = True
                    break

            if not found:
                print("Food item not found.")

    except FileNotFoundError:
        print("No food data found.")

def waste_risk_report():
    try:
        with open("food_data.csv", "r") as file:
            reader = csv.reader(file)

            total = 0
            risky = 0

            print("\n===== Waste Risk Report =====")

            today = datetime.today()

            for row in reader:
                food = row[0]

                expiry_date = datetime.strptime(row[2], "%Y-%m-%d")
                days_left = (expiry_date - today).days

                total += 1

                if days_left <= 3:
                    print(f"{food} -> High Risk")
                    risky += 1
                else:
                    print(f"{food} -> Low Risk")

            if total > 0:
                risk_percent = (risky / total) * 100
                print(f"\nOverall Waste Risk: {risk_percent:.0f}%")

    except FileNotFoundError:
        print("No food data found.")

while True:
    print("\n===== FoodSaver AI =====")
    print("1. Add Food Item")
    print("2. View Food Items")
    print("3. Smart Recommendations")
    print("4. Analytics Dashboard")
    print("5. Search Food Item")
    print("6. waste Risk report")
    print("7. Exit")
    

    choice = input("Enter choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        view_food()

    elif choice == "3":
        recommend_food()

    elif choice == "4":
        analytics_dashboard()

    elif choice == "5":
        search_food()
    

    elif choice == "6":
        waste_risk_report()

    elif choice == "7":
        break
        
    else:
        print("Invalid Choice")