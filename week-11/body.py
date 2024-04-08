class Head:
    def __init__(self) -> None:
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg) -> None:
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm:
    def __init__(self, hand) -> None:
        self.hand = hand

class Hand:
    def __init__(self) -> None:
        pass

class Leg:
    def __init__(self, feet) -> None:
        self.feet = feet

class Feet:
    def __init__(self) -> None:
        pass

class Human:
    def __init__(self, torso) -> None:
        self.torso = torso


def main():
    human = Human(
        Torso(
            Head(),
            Arm(
                Hand()
            ),
            Arm(
                Hand()
            ),
            Leg(
                Feet()
            ),
            Leg(
                Feet()
            )
        )
    )

if __name__=='__main__':
    main()