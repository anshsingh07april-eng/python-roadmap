#Q12. Next greater element. For every number in a list, find the next number to its right that is bigger, or -1 if none. For [2, 1, 2, 4, 3] the answer is [4, 2, 4, -1, -1]. First write the slow way with two loops, then try a stack.

def next_greater_brute(nums):

    result = []

    for i in range(len(nums)):

        greater = -1

        for j in range(i + 1, len(nums)):

            if nums[j] > nums[i]:
                greater = nums[j]
                break

        result.append(greater)

    return result


nums = [2, 1, 2, 4, 3]

print("Original:", nums)
print("Next Greater:", next_greater_brute(nums))