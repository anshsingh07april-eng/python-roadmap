#Q13. Subsets. Print all subsets of [1, 2, 3] (there are 8). For each item you either take it or skip it.
def print_subsets(nums, index, current_subset):
    if index == len(nums):
        print(current_subset)
        return

    print_subsets(nums, index + 1, current_subset)

    print_subsets(nums, index + 1, current_subset + [nums[index]])

prompt = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, prompt.split()))
print("All subsets of the list are:")
print_subsets(numbers, 0, [])
print(f"The original list is: {numbers}")