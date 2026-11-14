#Q2. to_list. Write to_list(head) that returns all values as a normal Python list, like [10, 20, 30]. Test with a head of None (it should return []).
def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result
node1 = None
print(to_list(node1))