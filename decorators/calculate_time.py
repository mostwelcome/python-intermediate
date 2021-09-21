from time import perf_counter


def time_it(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(func.__name__ + 'took ' + str((end - start) * 1000) + ' mil sec.')
        return result

    return wrapper


@time_it
def calculate_square(n):
    return n * n


@time_it
def calculate_cube(n):
    return n * n * n


print(calculate_square(500))
print(calculate_cube(500))
