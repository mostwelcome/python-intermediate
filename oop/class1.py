class Test:
    def __init__(self, name):
        self.name = name

    def __init__(self, title, name=None):
        self.title = title
        self.name = name

    def __str__(self):
        return f'{self.name} {self.title}'


t1 = Test('swag')
t2 = Test('developer', 'swag')

print(t1)
print(t2)
