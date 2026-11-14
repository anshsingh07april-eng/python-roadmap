#Q9. Reverse a linked list. Reverse 10 -> 20 -> 30 into 30 -> 20 -> 10 by changing the pointers (do not build a new list). Draw it first!
class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

print(to_list(reverse_list(None)))                              # []
print(to_list(reverse_list(Node(10))))                          # [10]
print(to_list(reverse_list(Node(10, Node(20, Node(30))))))      # [30, 20, 10]