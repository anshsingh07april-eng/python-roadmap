#Q7. Insert and delete. Start with [10, 20, 30, 40]. Insert 25 between 20 and 30, remove 10, and pop the last item. Print the list after each step.
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

numbers.insert(2, 25)
print("After inserting 25:", numbers)

numbers.remove(10)
print("After removing 10:", numbers)

numbers.pop()
print("After popping the last item:", numbers)