#Q7. Sum of 1 to N. Ask for N and print the sum of all numbers from 1 to N using a loop.
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print(f"The sum of numbers from 1 to {N} is {sum}.")
