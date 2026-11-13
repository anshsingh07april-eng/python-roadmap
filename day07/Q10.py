#Q10. Two Sum. Given nums = [2, 7, 11, 15] and target = 9, find the two numbers that add up to the target and print their positions (answer: 0 and 1). First write the slow way with two loops. Then write a one-loop version using a dictionary that remembers the numbers you have already seen.
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Positions: {i}, {j}")
            break

seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        print(f"Positions: {seen[complement]}, {i}")
        break
    seen[num] = i
print("Seen dictionary:", seen)