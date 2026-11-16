#Q4. Sum of digits. Write sum_digits(n) that returns the sum of the digits of a number (for example 1234 gives 10) without a loop.
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)
input_number = int(input("Enter a number to calculate sum of digits: "))
print(f"The sum of digits of {input_number} is: {sum_digits(input_number)}")