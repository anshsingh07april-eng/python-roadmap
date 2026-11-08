#Q11. Simple expense tracker. Ask for an item name and an amount (a number, validated with try and except). Save each expense on its own line in expenses.txt in the form item,amount. Add an option to view all expenses and print the total amount spent.

def get_amount():
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Invalid amount! Please enter a valid number.")


def add_expense():
    item = input("Enter item name: ").strip()

    if not item or "," in item:
        print("Please enter a valid item name without commas.")
        return

    amount = get_amount()

    with open("expenses.txt", "a") as file:
        file.write(f"{item},{amount}\n")

    print("Expense successfully saved!")


def view_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found!")
            return

        print("\n------ ALL EXPENSES ------")

        for index, line in enumerate(expenses, start=1):
            item, amount = line.strip().split(",")
            amount = float(amount)

            print(f"{index}. {item}: ₹{amount:.2f}")
            total += amount

        print("--------------------------")
        print(f"Total amount spent: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expense records found!")


def main():
    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Exit")

        choice = get_int("Enter your choice: ")

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Select between 1 and 3.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Enter a whole number.")


main()