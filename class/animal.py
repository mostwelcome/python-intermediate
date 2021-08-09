class Animal:
    def __init__(self,fur_color ) -> None:
        self.fur_color = fur_color

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("I eat food")
    
    def get_fur_color(self):
        print(self.fur_color)

class HouseCat(Animal):
    def speak(self):
        print("meawww")

    def eat(self):
        super().eat()
        print("I eat fish")

animal = Animal("black")


cat = HouseCat("white")
cat.speak()
cat.eat()
cat.get_fur_color()