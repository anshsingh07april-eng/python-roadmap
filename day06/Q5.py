#Q5. Linear search. Write find(nums, target) that returns the index of target, or -1 if it is not found. Do not use index() or in.
def find(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
print(find([4, 2, 7, 1, 9], 7))  # Output: 2
print(find([4, 2, 7, 1, 9], 5))  # Output: -1