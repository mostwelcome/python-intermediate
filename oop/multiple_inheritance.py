# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"


# Here the order matters
class C(A, B):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.show_props()
