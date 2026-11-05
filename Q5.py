#Q5. Two-sum. Given a list of integers and a target, return the indices of the two numbers that add up to the target. First write the slow version with two nested loops. Then write a one-pass version using a dictionary. In a comment, state the time complexity of both in Big-O terms.

# Time complexity: O(n^2) for the slow version and O(n) for the fast version.
def two_sum_slow(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

def two_sum_fast(numbers, target):
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

list_of_numbers = [2, 7, 11, 15]
target_value = 9

print("Slow version:", two_sum_slow(list_of_numbers, target_value))
print("Fast version:", two_sum_fast(list_of_numbers, target_value))
 