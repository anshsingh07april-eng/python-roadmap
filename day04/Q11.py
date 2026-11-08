#Q11. Simple contact book. Use a dictionary that maps a name to a phone number. Write functions add_contact, search_contact and show_all, and a menu with a while loop that runs until the user chooses Exit. If the name is not found, print a friendly message.
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name, "Contact not found.")

def show_all():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        print(search_contact(name))
    elif choice == "3":
        show_all()
    elif choice == "4":
        break
    else:
        print("Invalid option.")