from functools import wraps


def bold(func):
    '''Bold Decorator'''
    @wraps(func)
    def wrapper():
        result = '<b>' + func() + '<b>'
        return result
    return wrapper


def italics(func):
    @wraps(func)
    def wrapper():
        result = '<i>' + func() + '<i>'
        return result
    return wrapper


@bold
@italics
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'


print(printfib())
