#Q15. Queue using two stacks. Build a queue using only two lists as stacks.
class QueueUsingStacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        print(item, "added to queue")

    def dequeue(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("Queue is empty")
            return None

        return self.stack2.pop()

    def front(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("Queue is empty")
            return None

        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

q = QueueUsingStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("\nFront:", q.front())

print("Removed:", q.dequeue())
print("Removed:", q.dequeue())

print("Front:", q.front())
print("Queue size:", q.size())

print("Removed:", q.dequeue())
print("Removed:", q.dequeue())

print("Is empty:", q.is_empty())
