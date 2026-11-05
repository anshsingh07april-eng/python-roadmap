#Q9. Rotate a list. Write rotate(lst, k) that rotates a list to the right by k positions. k can be larger than the list length and can be negative. First solve it with slicing. Then solve it in place using the three-reversals method (reverse the whole list, then reverse the first k items, then reverse the rest). Test with at least 5 cases.

def rotate_with_slicing(lst, k):
    k = k % len(lst)  # Handle cases where k is larger than the list length
    return lst[-k:] + lst[:-k]

def rotate_in_place(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is larger than the list length
    # Reverse the whole list
    lst.reverse()
    # Reverse the first k items
    lst[:k] = reversed(lst[:k])
    # Reverse the remaining items
    lst[k:] = reversed(lst[k:])

# Test cases
test_list = [1, 2, 3, 4, 5]
print("Original list:", test_list)

# Test case 1: Rotate right by 2 positions
print("Rotate right by 2:", rotate_with_slicing(test_list.copy(), 2))

# Test case 2: Rotate right by 7 positions (larger than list length)
print("Rotate right by 7:", rotate_with_slicing(test_list.copy(), 7))

# Test case 3: Rotate left by 2 positions (negative k)
print("Rotate left by 2:", rotate_with_slicing(test_list.copy(), -2))

# Test case 4: Rotate right by 0 positions
print("Rotate right by 0:", rotate_with_slicing(test_list.copy(), 0))

# Test case 5: Rotate right by the length of the list
print("Rotate right by length:", rotate_with_slicing(test_list.copy(), len(test_list)))