#Q6. Multiplication table. Ask for a number and print its table up to 10, for example 5 x 3 = 15.
a = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")
    