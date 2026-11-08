#Q5. Write a file. Write 5 lines of your choice into a file called notes.txt using with open(...). Check that the file appears in your folder.

from pathlib import Path

notes = [
    "I am learning Python.",
    "My goal is to become a Python master.",
    "I practice coding every day.",
    "I am learning exception handling.",
    "I will build real-world projects."
]

try:
    with open("notes.txt", "w") as file:
        for line in notes:
            file.write(line + "\n")

    if Path("notes.txt").exists():

        with open("notes.txt", "r") as file:
            content = file.readlines()

        if len(content) == 5:
            print("Items successfully added!")
        else:
            print("File created, but all items were not added.")

    else:
        print("File was not created.")

except OSError as e:
    print(f"File error: {e}")
