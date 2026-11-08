#Q1. Square and cube. Write square(n) and cube(n) that return the result. Then loop over the list [1, 2, 3, 4, 5] and print each number with its square and cube.

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print("Number:", num, "Square:", square(num), "Cube:", cube(num))
