#Q7. Reverse the words. Use a stack to turn "I love Python" into "Python love I".
text = "I love Python"

stack = []

words = text.split()

for word in words:
    stack.append(word)

print("Stack:", stack)

reversed_words = []

while stack:
    reversed_words.append(stack.pop())

result = " ".join(reversed_words)

print("Original sentence:", text)
print("Reversed sentence:", result)
