#Q8. Second smallest. Find the second smallest number in a list of at least 2 different numbers, using one loop (no sorting).
numbers = [15, 8, 22, 4, 19]
smallest = float('inf')
second_smallest = float('inf')

for n in numbers:
    if n < smallest:
        second_smallest = smallest
        smallest = n
    elif n < second_smallest and n != smallest:
        second_smallest = n

print("The second smallest number is:", second_smallest)