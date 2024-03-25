class Bus:
    def __init__(self) -> None:
        self.current_passengers = 0
        self.max_passengers = 20


    def add_passenger(self):
        if self.current_passengers < self.max_passengers:
            ++self.current_passengers
        else:
            print('Max capacity has been reached')


    def remove_passenger(self):
        if self.current_passengers > 0:
            --self.add_passenger
        else:
            print('There is no more passengers in the Bus')