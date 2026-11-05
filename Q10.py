#Q10. Balanced brackets. Write is_balanced(s) that checks a string containing (), [] and {} and returns True or False, using a list as a stack. Test with: "{[()]}" (True), "([)]" (False), "((" (False), "" (True), "a(b)c[d]" (True). This is a very common interview question.

def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return not stack

# Test cases
print(is_balanced("{[()]}"))  # True
print(is_balanced("([)]"))    # False
print(is_balanced("(("))      # False
print(is_balanced(""))        # True
print(is_balanced("a(b)c[d]")) # True