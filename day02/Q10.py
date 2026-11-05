#Q10. Password strength checker. Take a password and check these rules: at least 8 characters, has an uppercase letter, has a lowercase letter, has a digit, has a special character (anything not a letter or digit). Print which rules passed and which failed, and give a final verdict: Weak (0 to 2 rules), Medium (3 to 4), Strong (all 5).
password = input("Enter a password: ")

rules = {
    "at least 8 characters": len(password) >= 8,
    "has an uppercase letter": any(c.isupper() for c in password),
    "has a lowercase letter": any(c.islower() for c in password),
    "has a digit": any(c.isdigit() for c in password),
    "has a special character": any(not c.isalnum() for c in password)
}

passed = [rule for rule, passed in rules.items() if passed]
failed = [rule for rule, passed in rules.items() if not passed]

print("Rules passed:")
for rule in passed:
    print(f" - {rule}")

print("Rules failed:")
for rule in failed:
    print(f" - {rule}")

if len(passed) == 5:
    print("Final verdict: Strong")
elif len(passed) >= 3:
    print("Final verdict: Medium")
else:
    print("Final verdict: Weak")