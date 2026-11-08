#Q3. Return two values. Write circle_info(radius) that returns both the area and the perimeter (use 3.14 for pi). Call it and unpack the result into two variables, then print both with two decimal places.
#Hint: return area, perimeter and then a, p = circle_info(5). For two decimals use {a:.2f} in the f-string.

def circle_info(radius):
    pi = 3.14
    area = pi * radius ** 2
    perimeter = 2 * pi * radius
    return area, perimeter

c = float(input("Enter the radius of the circle: "))

if c > 0:
    a, p = circle_info(c)
    print(f"Area: {a:.2f}")
    print(f"Perimeter: {p:.2f}")
else:
    print("Enter a valid positive radius.")
