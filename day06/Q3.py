#Q3. Smallest number. Find the smallest number in a list using a loop (no min()). Print its value and its index.
numbers = [15, 8, 22, 4, 19]
smallest = numbers[0]
smallest_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
        smallest_index = i

print("The smallest number is:", smallest)
print("Its index is:", smallest_index)