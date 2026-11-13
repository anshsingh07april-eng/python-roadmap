#Q5. Phone book. Make a dictionary of 3 names and phone numbers. Add a new contact, update one number, delete one contact, and print every name with its number. Then ask the user for a name and print the number, or Not found.
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}

phone_book["David"] = "456-789-0123"

phone_book["Alice"] = "111-111-1111"

del phone_book["Charlie"]

for name, number in phone_book.items():
    print(f"{name}: {number}")

user_input = input("Enter a name: ")
if user_input in phone_book:
    print(f"{user_input}: {phone_book[user_input]}")
else:
    print("Not found")