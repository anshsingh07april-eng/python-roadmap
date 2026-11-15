#Q7. Shapes. Write a parent class Shape with a method area() that returns 0. Write Circle (radius), Rectangle (length, width) and Triangle (base, height) that each override area(). Put several shapes in one list and print each area with two decimals, then print the shape with the largest area.
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")

largest_shape = max(shapes, key=lambda shape: shape.area())
print(f"Shape with largest area: {largest_shape.__class__.__name__}")
print(f"Largest area: {largest_shape.area():.2f}")
print("All shapes have been processed!")