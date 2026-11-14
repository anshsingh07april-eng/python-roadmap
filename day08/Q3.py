#Q3. Length. Write length(head) that counts the nodes. Do not use to_list.
def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
a = None
print(length(a))