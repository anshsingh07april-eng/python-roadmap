#Q10. Find the middle. Return the value of the middle node using two pointers: slow moves 1 step, fast moves 2 steps. When fast reaches the end, slow is in the middle. Test with 5 nodes and with 6 nodes.
class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val if slow else None

print(find_middle(None))                                    
print(find_middle(Node(10)))                               
print(find_middle(Node(10, Node(20, Node(30, Node(40, Node(50))))))) 
print(find_middle(Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))))  