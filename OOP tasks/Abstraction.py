"""
Abstraction. Create the abstract class. Demonstrate how it can be used, and why is it useful.
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * self.width

    def calculate_area(self):
        return 2 * self.height + 2 * self.width


square = Square(10)
rectangle = Rectangle(6, 12)

print("Square Perimeter:", square.calculate_perimeter())
print("Square Area:", square.calculate_area())

print("Rectangle Perimeter:", rectangle.calculate_perimeter())
print("Rectangle Area:", rectangle.calculate_area())
