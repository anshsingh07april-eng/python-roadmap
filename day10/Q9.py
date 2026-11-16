#Q9. Largest in a list. Write largest(nums) without using max() or a loop.
def largest(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        max_of_rest = largest(nums[1:])
        return nums[0] if nums[0] > max_of_rest else max_of_rest
prompt = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, prompt.split()))
print(f"The largest number in the list is: {largest(numbers)}")