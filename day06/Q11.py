#Q11. Move zeros. Given [0, 1, 0, 3, 12], move all zeros to the end while keeping the order of the other numbers: [1, 3, 12, 0, 0]. Try to do it in one pass.
numbers = [0, 1, 0, 3, 12]
write_index = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[write_index] = numbers[i]
        write_index += 1

while write_index < len(numbers):
    numbers[write_index] = 0
    write_index += 1

print(numbers)