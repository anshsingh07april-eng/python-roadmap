#Q4. Any common item? Write has_common(list1, list2) that returns True if the two lists share at least one item. Test it with two examples.
def has_common(list1, list2):
    return bool(set(list1) & set(list2))

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]
c = [8, 9, 10]
d = [10, 11, 12]

print(has_common(a, b))  
print(has_common(c, d))  
print(has_common(a, c))  