def print_parameters(func):
    def wrapper(parameters):
        for element in parameters:
            print(element)
        func(parameters)
    return wrapper


def only_numbers(func):
    def wrapper(parameters):
        try:
            for element in parameters:
                if not isinstance(element, int):
                    raise(TypeError)
        except(TypeError):
            print('One of the parameters is not a number')
        func(parameters)
    return wrapper


@print_parameters
@only_numbers
def test_function(a):
    pass


test_function([1,'2',4])

