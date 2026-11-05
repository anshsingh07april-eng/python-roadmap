#Q3. Interest calculator. Take principal, rate (per year) and time (years). Print the simple interest and the compound interest, both rounded to 2 decimal places using :.2f in the f-string.
principal = float(input("Enter the principal amount in ₹ : "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate / 100) ** time - principal

print(f"Simple Interest: ₹{simple_interest:.2f}")
print(f"Compound Interest: ₹{compound_interest:.2f}")