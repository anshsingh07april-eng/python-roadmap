#Q7. Get at index. Write get_at(head, index) that returns the value at that position (0 is the head), or None if the index is too big.
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def get_at(head, index):
    for _ in range(index):
        if head is None:
            return None
        head = head.next
    return head.val if head is not None else None
print(get_at(None, 0))          # None
print(get_at(Node(10), 0))      # 10
print(get_at(Node(10), 1))      # None