#Q1. Safe number input. Write a function get_int(prompt) that keeps asking until the user types a valid whole number, then returns it. Use it to ask for the user's age and print it.
def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number
            else:
                print("Invalid age! Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


age = get_int("Please enter your age: ")
print(f"Your age is: {age}")


