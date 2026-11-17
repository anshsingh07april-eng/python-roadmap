#Q5. Balanced round brackets. Check whether a string like "(()())" has matching ( and ). Test with "(()", "())" and "".
def is_balanced(text):

    stack = []

    for char in text:

        if char == "(":
            stack.append(char)

        elif char == ")":

            if not stack:
                return False

            stack.pop()

    return len(stack) == 0

print("(()()) :", is_balanced("(()())"))
print("(()    :", is_balanced("(()"))
print("())    :", is_balanced("())"))
print("Empty  :", is_balanced(""))