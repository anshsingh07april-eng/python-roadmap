#Q12. LinkedList class. Put your functions into a class LinkedList with self.head, and methods add_first, add_last, delete_value, show (prints like 10 -> 20 -> 30 -> None) and __len__.
class LinkedList:
    class Node:
        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt

    def __init__(self):
        self.head = None

    def add_first(self, value):
        self.head = self.Node(value, self.head)

    def add_last(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def delete_value(self, target):
        if self.head is None:
            return
        if self.head.val == target:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next is not None:
            if cur.next.val == target:
                cur.next = cur.next.next
                return
            cur = cur.next

    def show(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(out) + " -> None")

    def __len__(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count
print("Testing LinkedList class:")
ll = LinkedList()
ll.add_first(10)
ll.add_last(20)
ll.show()  # 10 -> 20 -> None
print(len(ll))  # 2
ll.delete_value(10)
ll.show()  # 20 -> None
print(len(ll))  # 1
ll.delete_value(30)  # value not in list
ll.show()  # 20 -> None
print(len(ll))  # 1