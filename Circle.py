import math


class Circle:
    def __init__(self) -> None:
        self.radius = 0

    def get_area(self):
        return math.pi * (self.radius ** 2)
    

class Bus:
    def __init__(self) -> None:
        self.current_passengers = 0
        self.max_passengers = 20

    def add_passenger(self):
        if self.current_passengers < self.max_passengers:
            ++self.current_passengers
        else:
            print('Max capacity has been reached')