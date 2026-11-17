#Q2. Reverse a string. Reverse "python" by pushing every letter onto a stack and then popping them all.
text = "python"
stack = []

for char in text:
    stack.append(char)

print("Stack:", stack)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

print("Original string:", text)
print("Reversed string:", reversed_text)