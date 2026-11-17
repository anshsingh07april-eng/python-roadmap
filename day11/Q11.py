#Q11. Ticket counter. Simulate a counter: customers arrive (enter names, type done to stop), then serve them in order, printing Serving Riya and how many are still waiting after each one.
from collections import deque

queue = deque()

print("=== Ticket Counter ===")

while True:

    name = input("Enter customer name (or 'done' to stop): ")

    if name.lower() == "done":
        break

    if name.strip() == "":
        print("Please enter a valid name.")
        continue

    queue.append(name)
    print(name, "added to queue.")

print("\n=== Serving Customers ===")

if not queue:
    print("No customers waiting.")

while queue:

    customer = queue.popleft()

    print("Serving", customer)
    print("Customers still waiting:", len(queue))

print("\nAll customers have been served!")