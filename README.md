# expense-tracker-python

# Expense Tracker Project

expensesList = []  # List of expenses in the form of dictionaries

print("Welcome to Expense Tracker!")

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))

    # Add Expense
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter the expense category (Food, Travel, Makeup, Books): ")
        description = input("Enter a description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nExpense added successfully.")

    # View All Expenses
    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses found.")
        else:
            print("\n===== All Expenses =====")

            count = 1
            for eachExpense in expensesList:
                print(
                    f"Expense {count} -> "
                    f"Date: {eachExpense['date']}, "
                    f"Category: {eachExpense['category']}, "
                    f"Description: {eachExpense['description']}, "
                    f"Amount: ₹{eachExpense['amount']}"
                )
                count += 1

    # View Total Spending
    elif choice == 3:
        total = 0

        for eachExpense in expensesList:
            total += eachExpense["amount"]

        print(f"\nTotal Spending = ₹{total}")

    # Exit
    elif choice == 4:
        print("Thank you for using Expense Tracker.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please try again.")
