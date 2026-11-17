#Q16. Min stack. Build a stack that also returns the smallest item in O(1) time with get_min().

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):

        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):

        if not self.stack:
            print("Stack is empty")
            return None

        removed = self.stack.pop()

        if removed == self.min_stack[-1]:
            self.min_stack.pop()

        return removed

    def peek(self):

        if not self.stack:
            return None

        return self.stack[-1]

    def get_min(self):

        if not self.min_stack:
            return None

        return self.min_stack[-1]


s = MinStack()

s.push(10)
s.push(5)
s.push(20)
s.push(2)
s.push(8)

print("Stack:", s.stack)
print("Minimum:", s.get_min())

print("Removed:", s.pop())
print("Minimum:", s.get_min())

print("Removed:", s.pop())
print("Minimum:", s.get_min())

print("Top element:", s.peek())
