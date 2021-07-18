import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(4)
        function()

    return wrapper_function


# syntactic sugar
@delay_decorator
def say_hello():
    print('hello')


def say_bye():
    print('bye')


say_bye()
say_hello()
