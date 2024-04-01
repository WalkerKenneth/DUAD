import math


class Circle:
    def __init__(self) -> None:
        self.radius = 0

    def get_area(self):
        return math.pi * (self.radius ** 2)
    


class Person:
    def __init__(self) -> None:
        pass


class Bus:
    def __init__(self) -> None:
        self.passengers = []
        self.max_passengers = 20


    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print('Max capacity has been reached')


    def remove_passenger(self):
        if self.current_passengers > 0:
            self.passengers.pop()
        else:
            print('There is no more passengers in the Bus')