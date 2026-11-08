#Q4. else and finally. Write a small program that asks for a number and prints its double. Use try, except, else (print the result only when no error happened) and finally (always print "Done"). Run it with a valid number and with a letter, and compare what prints.
try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"The double of {number} is {2 * number}.")
finally:
    print("Done.")