#Q2. Remove duplicates. Given a list such as [3, 1, 3, 2, 1, 5], produce a list without duplicates while keeping the original order. Do it two ways: with a loop and a helper list, and with dict.fromkeys(). In a comment, explain why list(set(...)) is not enough here.

def remove_duplicates_loop(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))

lst = [3, 1, 3, 2, 1, 5]
result_loop = remove_duplicates_loop(lst)
result_dict = remove_duplicates_dict(lst)
print(f"Original list: {lst}")
print(f"Without duplicates (loop): {result_loop}")
print(f"Without duplicates (dict): {result_dict}")
# list(set(lst)) is not enough because set() does not guarantee preserving the original order.