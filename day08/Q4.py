#Q4. Add at the start. Write add_first(head, value) that creates a new node, points it to the old head, and returns the new head. Add 5 to the front of 10 -> 20 -> 30.
class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def add_first(head, value):
    return Node(value, head)   

def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

head = build([10, 20, 30])      
head = add_first(head, 5)       
print(to_list(head))
print(to_list(add_first(None, 7)))   