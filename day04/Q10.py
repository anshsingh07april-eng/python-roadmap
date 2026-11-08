#Q10. Only even numbers. Write get_evens(numbers) that takes a list and returns a new list with only the even numbers. Test it with [1, 2, 3, 4, 5, 6] and with an empty list.
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

print(get_evens([1, 2, 3, 4, 5, 6]))  
print(get_evens([]))  