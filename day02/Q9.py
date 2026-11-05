#Q9. Triangle checker. Take three side lengths. First check whether they can form a triangle (sum of any two sides must be greater than the third). If valid, print whether it is equilateral, isosceles or scalene.
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The given side lengths cannot form a triangle.")