#Q2. Safe division. Ask for two numbers and divide them. Handle both problems separately: a letter instead of a number (ValueError) and division by zero (ZeroDivisionError). Each should print a different message.
def safe_division():
    while True:
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            result = numerator / denominator
            print(f"Result: {result:.2f}")
            break  

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
print("Welcome to the safe division program!")
safe_division()