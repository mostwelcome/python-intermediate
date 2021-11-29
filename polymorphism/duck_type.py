class Laptop:
    def code(self, ide):
        ide.execute()


class Pycharm:
    def execute(self):
        print('Execute')
        print('Prints output')


class MyEditor:
    def execute(self):
        print('Checks spelling')
        print('Checks convention')
        print('Execute')
        print('Prints output')


ide = Pycharm()

laptop = Laptop()
laptop.code(ide)

ide2 = MyEditor()
laptop.code(ide2)