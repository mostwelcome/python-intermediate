import functools


def start_end(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


@start_end
def add(x):
    return x + 5


# print(add(5))
print(help(add))
print(add.__name__)
