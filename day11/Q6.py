#Q6. All three bracket types. Extend Q5 to (), [] and {}. Test with "{[()]}" (True), "([)]" (False) and "a(b)c[d]" (True). This is a very common interview question.
def is_balanced(text):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:

        if char in "([{":
            stack.append(char)

        elif char in ")]}":

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0

print("{[()]}", is_balanced("{[()]}"))
print("([)]", is_balanced("([)]"))
print("a(b)c[d]", is_balanced("a(b)c[d]"))