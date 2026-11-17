#Q1. Stack with a list. Using only a Python list, push 5 numbers, print the top without removing it (peek), pop two numbers, and print whether the stack is empty.

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print("stack:", stack)
print("top:", stack[-1])

stack.pop()
stack.pop()

print("After popping two elements:", stack)

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")