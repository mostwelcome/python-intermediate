from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def to_JSON(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)

    def to_JSON(self):
        return f"{{ \"square\": {str(self.calc_area())} }}"


c = Circle(10)
print(c.calc_area())
print(c.to_JSON())
