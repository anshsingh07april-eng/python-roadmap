#Q11. Detect a cycle. Create a list where the last node points back to an earlier node. Use the same slow and fast idea: if they ever meet, there is a cycle.
class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test cases
print(has_cycle(None))  # False
print(has_cycle(Node(10)))  # False
print(has_cycle(Node(10, Node(20, Node(30)))))  # False