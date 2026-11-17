#Q3. Stack class. Write a class Stack with methods push(item), pop(), peek(), is_empty() and size(). If pop() or peek() is called on an empty stack, print a friendly message (or raise an error) instead of crashing.
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Top element:", s.peek())
print("Stack size:", s.size())

print("Popped:", s.pop())
print("Popped:", s.pop())

print("Stack size:", s.size())
print("Is stack empty?", s.is_empty())