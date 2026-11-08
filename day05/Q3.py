#Q3. Guess the error. Run each line below (one at a time) and write in a comment the error name and what caused it. Then wrap each one in try and except so it prints a friendly message instead:
#• int("abc")
try:
    number = int("abc")
except ValueError:
    print("ValueError: Please enter a valid number.")

#• [1, 2, 3][5]
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("IndexError: List index is out of range.")

#• {"a": 1}["b"]
try:
    data = {"a": 1}
    print(data["b"])
except KeyError:
    print("KeyError: Dictionary key was not found.")

#• 10 / 0
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

#• open("missing.txt")
try:
    with open("missing.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found!")
