#Q8. Decimal to binary. Convert a number like 10 to binary (1010) by dividing by 2 and pushing the remainders onto a stack, then popping them to build the answer.

number = int(input("Enter a decimal number: "))

stack = []

if number == 0:
    stack.append(0)

while number > 0:
    remainder = number % 2
    stack.append(remainder)

    number = number // 2  

binary = ""

while stack:
    binary += str(stack.pop())

print("Binary number:", binary)
