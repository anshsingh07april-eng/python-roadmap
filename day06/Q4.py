#Q4. Reverse in place. Reverse a list without slicing and without reverse(), by swapping the first and last items, then the second and second-last, and so on.
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) // 2):
    numbers[i], numbers[-(i + 1)] = numbers[-(i + 1)], numbers[i]
print("Reversed list:", numbers)