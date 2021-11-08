def foo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(type(args))
    print(type(kwargs))
    for arg in args:
        print(arg)

    for kwg in kwargs.items():
        print(kwg)


foo(1, 2, 5, 6, 7, 8, 9, c=7, d=8, k=9)
