#Q2. Default argument. Write greet(name, greeting="Hello") that returns a greeting like Hello, Ansh!. Call it once with only a name, and once with a custom greeting like "Namaste".
#Hint: A default value is written in the function line: def greet(name, greeting="Hello"):.

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

name = input("Enter your name: ")
# Call greet with only a name   
print(greet(name))
if __name__ == "__main__":
    custom_greeting = input("Enter a custom greeting: ")
    print(greet(name, custom_greeting))
else:
    custom_greeting = input("Enter a custom greeting: ")
    print(greet(name, custom_greeting))