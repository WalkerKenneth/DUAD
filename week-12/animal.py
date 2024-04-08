class Herbivores:
    def __init__(self) -> None:
        self.food = 'leaves'
        super(Herbivores, self).__init__()


class Omnivores:
    def __init__(self) -> None:
        self.food = 'Various'
        super(Omnivores, self).__init__()


class Carnivores:
    def __init__(self) -> None:
        self.food = 'meat'
        super(Carnivores, self).__init__()


class Mammals:
    def __init__(self) -> None:
        self.type = 'Mammal'
        super(Mammals, self).__init__()


class Birds:
    def __init__(self) -> None:
        self.type = 'Bird'
        super(Birds, self).__init__()


class Reptiles:
    def __init__(self) -> None:
        self.type = 'Reptile'
        super(Reptiles, self).__init__()


class Eagle(Carnivores, Birds):
    def __init__(self) -> None:
        super(Eagle, self).__init__()


class Rabbit(Herbivores, Mammals):
    def __init__(self) -> None:
        super(Rabbit, self).__init__()


class Turtle(Omnivores, Reptiles):
    def __init__(self) -> None:
        super(Turtle, self).__init__()


def main():
    eagle = Eagle()
    rabbit = Rabbit()
    turtle = Turtle()
    print(f'''
        Eagle type is: {eagle.type} and his food is: {eagle.food}\n
        Rabbit type is: {rabbit.type} and his food is: {rabbit.food}\n
        Turtle type is: {turtle.type} and his food is: {turtle.food}
    ''')


if __name__ == '__main__':
    main()