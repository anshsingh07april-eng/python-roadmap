#Q11. Challenge: Number tools. Take a positive integer and, using a while loop with % and // only (no string conversion), print the sum of its digits, the number of digits, the largest digit, and the reversed number. Then tell whether the number is a palindrome.
num = int(input("Enter a positive integer: "))

sum_of_digits = 0
num_of_digits = 0
largest_digit = 0
reversed_num = 0
original_num = num

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num_of_digits += 1
    if digit > largest_digit:
        largest_digit = digit
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Print the results
print(f"Sum of digits: {sum_of_digits}")
print(f"Number of digits: {num_of_digits}")
print(f"Largest digit: {largest_digit}")
print(f"Reversed number: {reversed_num}")

# Check if the number is a palindrome
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")