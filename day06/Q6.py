#Q6. Count occurrences. Write count(nums, target) that returns how many times target appears. Test it on [1, 2, 2, 3, 2] with target 2.
def count(nums, target):
    count = 0
    for n in nums:
        if n == target:
            count += 1
    return count

print(count([1, 2, 2, 3, 2], 2))  # Output: 3