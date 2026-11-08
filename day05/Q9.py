#Q9. Missing file. Write a function read_file(name) that returns the file's text, or prints a friendly message and returns an empty string if the file does not exist. Test it with a real file name and a wrong one.
def read_file(name):
    try:
        with open(name, "r") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Sorry! The file '{name}' does not exist.")
        return ""
    
content = read_file("notes.txt")
print(content)

content = read_file("wrong.txt")
print(content)