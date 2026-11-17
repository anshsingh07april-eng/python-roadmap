#Q4. Undo. Build a small text editor simulation: the user types words one at a time, and typing undo removes the last word. Typing show prints the text so far, and quit ends the program. Use a stack.
stack = []

while True:

    command = input("\nEnter a word or command (undo/show/quit): ")

    if command == "quit":
        print("Exiting text editor...")
        break

    elif command == "undo":
        if stack:
            removed = stack.pop()
            print("Undo:", removed, "removed.")
        else:
            print("Nothing to undo! Stack is empty.")

    elif command == "show":
        if stack:
            print("Current text:", " ".join(stack))
        else:
            print("Text is empty.")

    else:
        stack.append(command)
        print("Added:", command)
