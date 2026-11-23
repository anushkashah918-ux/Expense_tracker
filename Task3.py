
import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    print("\n--- Add New Expense ---")

    title = input("Enter expense name: ").strip()
    if not title:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ").strip()
    if not category:
        category = "Other"

    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"Amount: ₹{expense['amount']:.2f} | "
            f"Category: {expense['category']} | "
            f"Date: {expense['date']}"
        )


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Expenses ---")
    print(f"Total spending: ₹{total:.2f}")


def category_summary():
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses available.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses()
            print(f"{removed['title']} deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expenses")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


expenses = load_expenses()

if __name__ == "__main__":
    main()
