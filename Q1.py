#Q1. List statistics by hand. Take numbers from the user in one line, separated by spaces. Print the largest, smallest, second largest and the average. Do not use max(), min(), sum() or sorted(). Use loops only. Handle an empty input and a list with only one number.
numbers = input("Enter numbers separated by spaces: ").split()

if not numbers:
    print("No numbers entered.")
else:
    numbers = [int(x) for x in numbers]
    
    largest = numbers[0]
    smallest = numbers[0]
    total = numbers[0]
    
    for n in numbers:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
        total += n
    
    average = total / len(numbers)
    
    second_largest = smallest
    for n in numbers:
        if n < largest and n > second_largest:
            second_largest = n
    
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")
    print(f"Second Largest: {second_largest}")
    print(f"Average: {average}")