def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum


print(add(1, 2, 4, 4))


def calculate(**kwargs):
    print(kwargs['add'])
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)


calculate(add=5, multiply=5)
