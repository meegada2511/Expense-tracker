import csv
from datetime import datetime
import matplotlib.pyplot as plt  

CSV_FILE = 'expenses.csv'
HEADERS = ['Date', 'Category', 'Description', 'Amount']

def initialize_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
    except FileExistsError:
        pass  # File already exists, do nothing

def add_expense(category, description, amount):
    """Adds a new expense to the CSV file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, category, description, amount])
    print("Expense added successfully.")

def view_expenses():
    """Displays all recorded expenses."""
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)  
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Description: {row[2]}, Amount: ${float(row[3]):.2f}")
    except FileNotFoundError:
        print("No expenses found. The file 'expenses.csv' does not exist yet.")

def get_summary():
    """Calculates and displays a summary of expenses by category and shows a graph."""
    summary = {}
    total_expenses = 0
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header
            for row in reader:
                category = row[1]
                amount = float(row[3])
                total_expenses += amount
                summary[category] = summary.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses found to summarize.")
        return

    print("\n--- Expense Summary ---")
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")
    print(f"\nTotal Expenses: ${total_expenses:.2f}")

  
    if summary:
        plt.figure(figsize=(6, 6))
        plt.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%', startangle=90)
        plt.title("Expense Distribution by Category")
        plt.show()

def main():
    initialize_csv()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Get a summary of expenses (with graph)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                category = input("Enter expense category (e.g., Food, Transport): ")
                description = input("Enter a brief description: ")
                amount = float(input("Enter the amount: "))
                add_expense(category, description, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == '2':
            view_expenses()

        elif choice == '3':
            get_summary()

        elif choice == '4':
            print("Exiting the expense tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
