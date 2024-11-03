import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage:
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print(f"Circle: Area = {circle.area():.2f}, Perimeter = {circle.perimeter():.2f}")
print(f"Square: Area = {square.area():.2f}, Perimeter = {square.perimeter():.2f}")
print(f"Triangle: Area = {triangle.area():.2f}, Perimeter = {triangle.perimeter():.2f}")

# Output:
# Circle: Area = 78.54, Perimeter = 31.42
# Square: Area = 16.00, Perimeter = 16.00
# Triangle: Area = 6.00, Perimeter = 12.00
