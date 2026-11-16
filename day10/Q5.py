#Q5. Power. Write power(a, b) that returns a to the power b for whole numbers b >= 0, without using **.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

print(power(2, 3))
print(power(5, 2))
print(power(10, 0))