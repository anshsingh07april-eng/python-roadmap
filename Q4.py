#Biggest of three. Ask for three numbers and print the largest one using if / elif / else (do not use max()).
a = int(input("Enter number 01: "))
b = int(input("Enter number 02: "))
c = int(input("Enter number 03: "))
if a > b and a > c:
    print(f"{a} is the largest number.")
elif b > a and b > c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")    