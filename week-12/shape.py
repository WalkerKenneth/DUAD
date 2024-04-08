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

    def calculate_perimeter(self, radius):
        return 2 * math.pi * radius
    
    def calculate_area(self, radius):
        return math.pi * (radius ** 2)


class Square(Shape):

    def calculate_perimeter(self, side):
        return side * 4
    
    def calculate_area(self, side):
        return side ** 2


class Rectangle(Shape):
    def calculate_perimeter(self, side_1, side_2, side_3):
        return side_1 + side_2 + side_3
    
    def calculate_area(self, base, height):
        return (base * height) / 2