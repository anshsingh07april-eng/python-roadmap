#Q8. Sum of a list. Write sum_list(nums) that adds all numbers in a list. Do not use sum() or a loop.
def sum_list(nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum_list(nums[1:])
prompt = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, prompt.split()))
print(f"The sum of the numbers in the list is: {sum_list(numbers)}")