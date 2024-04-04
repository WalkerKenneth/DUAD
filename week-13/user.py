from datetime import date

class User:
    def __init__(self, user_date_of_birth) -> None:
        self.date_of_birth = date.fromisoformat(user_date_of_birth)

    @property
    def age(self):    
        user_age = date.today().year - self.date_of_birth.year
        if date.today().month < self.date_of_birth.month:
            user_age -= 1
        elif date.today().month == self.date_of_birth.month:
            if date.today().day < self.date_of_birth.day:
                user_age -= 1
        return user_age


def adult_user(func):
    def wrapper(user):
        try:
            if user.age < 18:
                raise(ValueError)
        except(ValueError):
            print('The user is not of legal age')
        func(user)
    return wrapper


@adult_user
def driving_test(user):
    pass

user = User('2020-04-05')
driving_test(user)