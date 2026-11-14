#Q5. Add at the end. Write add_last(head, value). If the list is empty, the new node becomes the head. Otherwise walk to the last node (the one whose next is None) and attach the new node there. Return the head.
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def add_last(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    cur = head
    while cur.next is not None:
        cur = cur.next

    cur.next = new_node
    return head


def main():
    head = None
    head = add_last(head, 10)
    head = add_last(head, 20)
    head = add_last(head, 30)
    print(to_list(head))


if __name__ == "__main__":
    main()      