#Q2. Rectangle. Write a Rectangle class with length and width, and methods area(), perimeter() and is_square() that returns True or False. Test with a square and a non-square.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

square = Rectangle(5, 5)
print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}, Is Square: {square.is_square()}")

rectangle = Rectangle(5, 10)
print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}, Is Square: {rectangle.is_square()}")