
expenses = []


def add_expense():
    print("\n--- Add New Expense ---")

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

    except ValueError:
        print("Please enter a valid amount!")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found!")
        return

    for e in expenses:
        print(e["date"], "|", e["category"],
              "|", e["description"], "| Rs.", e["amount"])


def total_spending():
    total = 0

    for e in expenses:
        total += e["amount"]

    print("\nTotal Spending: Rs.", total)


def category_summary():
    summary = {}

    for e in expenses:
        category = e["category"]
        summary[category] = summary.get(category, 0) + e["amount"]

    print("\n--- Category-wise Summary ---")

    for category, amount in summary.items():
        print(category, ": Rs.", amount)


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    total = 0

    print("\n--- Monthly Report ---")

    for e in expenses:
        if e["date"].startswith(month):
            print(e["date"], e["category"], "Rs.", e["amount"])
            total += e["amount"]

    print("Monthly Total: Rs.", total)


def main():
    while True:
        print("\n===== SIMPLE EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category-wise Summary")
        print("5. Monthly Spending Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


main()
