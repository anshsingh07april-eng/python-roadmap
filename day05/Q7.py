#Q7. Append. Ask the user for a new line and add it to the end of notes.txt without deleting the old lines. Run the program twice and check that both lines are saved.
new_line = input("Enter a new line to add to notes.txt: ")
try:
    with open("notes.txt", "a") as file:
        file.write(new_line + "\n")
    print("Line added successfully!")
except OSError as e:
    print(f"File error: {e}")