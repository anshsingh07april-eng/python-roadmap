#Q1. Unique numbers. Given [4, 7, 4, 9, 7, 1], print the unique numbers and how many there are.
numbers = [4, 7, 4, 9, 7, 1]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
print("Count of unique numbers:", len(unique_numbers))