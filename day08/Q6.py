#Q6. Contains. Write contains(head, target) that returns True or False.
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt
        
def contains(head, target):
    while head is not None:
        if head.val == target:
            return True
        head = head.next
    return False
print(contains(None, 10))          # False
print(contains(Node(10), 10))      # True