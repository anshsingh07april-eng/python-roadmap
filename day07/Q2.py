#Q2. Common and different. Given a = [1, 2, 3, 4, 5] and b = [4, 5, 6, 7], print the numbers in both lists, the numbers only in a, and all numbers from both lists without repeats.
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

common = list(set(a) & set(b))
print("Numbers in both lists:", common)

only_in_a = list(set(a) - set(b))
print("Numbers only in a:", only_in_a)

all_numbers = list(set(a + b))
print("All numbers from both lists without repeats:", all_numbers)