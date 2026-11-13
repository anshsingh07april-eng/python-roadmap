#Q2. Sum without sum(). Take 5 numbers from the user into a list and print the total using a for loop.
numbers = []
for _ in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0
for n in numbers:
    total += n

print("The total is:", total)