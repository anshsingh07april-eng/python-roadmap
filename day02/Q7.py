#Q7. Leap year. Take a year and print whether it is a leap year. Rule: divisible by 4, except century years, which must be divisible by 400. Test with 1900, 2000, 2024 and 2026.
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")