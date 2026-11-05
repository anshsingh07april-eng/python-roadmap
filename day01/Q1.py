#Q1. Greeting. Ask for the user's name and print a greeting using an f-string.
def greet_user():
    a = input("Enter your name: ").strip().lower()
    if a == "ansh":
        print("Nameste,ansh!") 
    else:
        print(f"Hello, {a}!")

greet_user() 