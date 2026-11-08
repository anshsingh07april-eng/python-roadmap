#Q8. File statistics. Read notes.txt and print the number of lines, the number of words and the number of characters.

with open("notes.txt", "r") as file:
    content = file.read()

    lines = content.splitlines()
    print("Number of lines:", len(lines))

    words = content.split()
    print("Number of words:", len(words))

    characters = len(content)
    print("Number of characters:", characters)