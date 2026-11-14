#Q8. Delete a value. Write delete_value(head, target) that removes the first node with that value and returns the head. Test three cases: deleting the head, deleting a middle node, and a value that is not in the list.
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

def delete_value(head, target):
    if head is None:
        return None

    if head.val == target:
        return head.next

    cur = head
    while cur.next is not None:
        if cur.next.val == target:
            cur.next = cur.next.next
            return head
        cur = cur.next

    return head
print(delete_value(None, 10))          # None
print(delete_value(Node(10), 10))      # None
print(delete_value(Node(10), 20))      # 10