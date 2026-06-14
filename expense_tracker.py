expensesList = []

print("Welcome to Expense Tracker!")

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expensesList.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expensesList) == 0:
            print("No expenses found.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expensesList, start=1):
                print(f"{i}. {expense['name']} - ₹{expense['amount']}")

    elif choice == "3":
        if len(expensesList) == 0:
            print("No expenses to delete.")
        else:
            for i, expense in enumerate(expensesList, start=1):
                print(f"{i}. {expense['name']} - ₹{expense['amount']}")

            index = int(input("Enter expense number to delete: "))

            if 1 <= index <= len(expensesList):
                deleted = expensesList.pop(index - 1)
                print(f"{deleted['name']} deleted successfully!")
            else:
                print("Invalid expense number.")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
