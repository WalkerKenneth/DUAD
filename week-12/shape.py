from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side_size) -> None:
        self.side_size = side_size

    def calculate_perimeter(self):
        return self.side_size * 4
    
    def calculate_area(self):
        return self.side_size ** 2


class Rectangle(Shape):
    def __init__(self, base, hight) -> None:
        self.base = base
        self.hight = hight

    def calculate_perimeter(self):
        return (self.base * 2) + (self.hight * 2)
    
    def calculate_area(self, base, height):
        return base * height