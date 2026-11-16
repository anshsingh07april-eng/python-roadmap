#Q11. Recursive binary search. Write binary_search(nums, target, low, high) that returns the index of target in a sorted list, or -1. Each call looks at the middle and searches only one half.
def binary_search(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search(nums, target, low, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, high)
prompt = input("Enter a sorted list of numbers separated by spaces: ")
numbers = list(map(int, prompt.split()))
prompt_target = int(input("Enter the target number to search for: "))
result = binary_search(numbers, prompt_target, 0, len(numbers) - 1)
print(f"The index of {prompt_target} in the list is: {result}")
print(f"The list is: {numbers}")