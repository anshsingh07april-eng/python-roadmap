#Q10. Notes app. Build a menu program with these options: 1. Add note, 2. View all notes, 3. Count notes, 4. Exit. Save the notes in a file so they are still there when you run the program again. Use get_int from Q1 for the menu choice, so a wrong input never crashes the program.

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Add a new note
def add_note():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note successfully added!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes found!")
        else:
            print("\n------ YOUR NOTES ------")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.strip()}")

    except FileNotFoundError:
        print("No notes found!")


def count_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        print(f"Total notes: {len(notes)}")

    except FileNotFoundError:
        print("Total notes: 0")


def main():
    while True:
        print("\n====== NOTES APP ======")
        print("1. Add note")
        print("2. View all notes")
        print("3. Count notes")
        print("4. Exit")

        choice = get_int("Enter your choice: ")

        if choice == 1:
            add_note()

        elif choice == 2:
            view_notes()

        elif choice == 3:
            count_notes()

        elif choice == 4:
            print("Thank you for using Notes App!")
            break

        else:
            print("Invalid choice! Select between 1 and 4.")


main()