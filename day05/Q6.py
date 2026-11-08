#Q6. Read a file. Read notes.txt and print each line with its line number, like 1: first line.
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print("Contents of notes.txt:")
    for index, line in enumerate(lines, start=1):
        print(f"{index}: {line.strip()}")