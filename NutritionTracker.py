import csv
from datetime import datetime

# Data file to save food log
DATA_FILE = "nutrition_log.csv"

# Initialize food log
food_log = []

# Load existing log from file
def load_log():
    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['calories'] = float(row['calories'])
                row['protein'] = float(row['protein'])
                row['carbs'] = float(row['carbs'])
                row['fat'] = float(row['fat'])
                food_log.append(row)
    except FileNotFoundError:
        pass  # No file to load, continue

# Save log to file
def save_log():
    with open(DATA_FILE, mode="w", newline='') as file:
        fieldnames = ['date', 'food', 'calories', 'protein', 'carbs', 'fat']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in food_log:
            writer.writerow(item)

# Add a food item
def add_food():
    food = input("Enter food name: ")
    calories = float(input("Enter calories: "))
    protein = float(input("Enter protein (g): "))
    carbs = float(input("Enter carbs (g): "))
    fat = float(input("Enter fat (g): "))
    entry = {
        'date': datetime.now().strftime("%Y-%m-%d"),
        'food': food,
        'calories': calories,
        'protein': protein,
        'carbs': carbs,
        'fat': fat
    }
    food_log.append(entry)
    print(f"{food} added successfully.")

# View today's nutrition summary
def view_summary():
    today = datetime.now().strftime("%Y-%m-%d")
    daily_items = [item for item in food_log if item['date'] == today]

    total_cal = sum(item['calories'] for item in daily_items)
    total_protein = sum(item['protein'] for item in daily_items)
    total_carbs = sum(item['carbs'] for item in daily_items)
    total_fat = sum(item['fat'] for item in daily_items)

    print(f"\n--- Nutrition Summary for {today} ---")
    print(f"Calories: {total_cal:.2f} kcal")
    print(f"Protein: {total_protein:.2f} g")
    print(f"Carbs:   {total_carbs:.2f} g")
    print(f"Fat:     {total_fat:.2f} g")
    print("----------------------------------\n")

# Main menu loop
def main():
    load_log()
    while True:
        print("\nNutrition Tracker")
        print("1. Add Food Item")
        print("2. View Today's Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_food()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            save_log()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
