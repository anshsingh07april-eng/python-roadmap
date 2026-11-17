#Q10. Queue class. Write a class Queue with enqueue(item), dequeue(), front(), is_empty() and size(). Handle the empty case with a friendly message.
from collections import deque

class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)
        print(item, "added to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None

        return self.items.popleft()

    def front(self):
        if self.is_empty():
            print("Queue is empty! Nothing at the front.")
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue("Ansh")
q.enqueue("Rahul")
q.enqueue("Aman")
q.enqueue("Rohit")

print("\nFront element:", q.front())
print("Queue size:", q.size())

print("\nDequeued:", q.dequeue())
print("Dequeued:", q.dequeue())

print("\nFront element:", q.front())
print("Queue size:", q.size())
print("Is queue empty?", q.is_empty())
