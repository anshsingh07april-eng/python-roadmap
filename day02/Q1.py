#Q1. Safe calculator. Take two numbers and print their sum, difference, product, division, floor division and remainder. If the second number is zero, print a friendly message instead of crashing for division, floor division and remainder.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

total = a + b
difference = a - b
product = a * b

if b != 0:
    division = a / b
    floor_division = a // b
    remainder = a % b  
else:
    division = "undefined (division by zero)"
    floor_division = "undefined (floor division by zero)"
    remainder = "undefined (remainder by zero)"

print(f"Sum: {total}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")  
print(f"Remainder: {remainder}")