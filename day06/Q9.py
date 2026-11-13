#Q9. Merge two sorted lists. Given two lists already sorted from small to large, build one sorted list using two index variables (no sort()). Example: [1, 4, 7] and [2, 3, 9] gives [1, 2, 3, 4, 7, 9].
def merge_sorted(list1, list2):
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

list1 = [1, 4, 7]
list2 = [2, 3, 9]
print(merge_sorted(list1, list2))  