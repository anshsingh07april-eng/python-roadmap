#Q9. Queue with deque. Using deque, add 4 names, remove the first one (dequeue), print who is at the front, and print the size.
from collections import deque

queue = deque()

queue.append("Ansh")
queue.append("Rahul")
queue.append("Aman")
queue.append("Rohit")

print("Original Queue:", queue)

removed = queue.popleft()
print("Dequeued:", removed)

print("Front of Queue:", queue[0])

print("Queue Size:", len(queue))
