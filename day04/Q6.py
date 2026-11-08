#Q6. Sets. Given a = [1, 2, 3, 4, 5, 3] and b = [4, 5, 6, 7], use sets to print: all unique numbers from both lists, the numbers common to both, and the numbers only in a.
a = [1, 2, 3, 4, 5, 3]
b = [4, 5, 6, 7]

set_a = set(a)
set_b = set(b)

print("All unique numbers:", set_a | set_b)

print("Common numbers:", set_a & set_b)

print("Numbers only in a:", set_a - set_b)