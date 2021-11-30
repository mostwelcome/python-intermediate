from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape, Area):
    def calculate_area(self):
        print('Calculating area of a circle')

    def draw(self):
        print('Drawing a circle')


class Rectangle(Shape, Area):
    def calculate_area(self):
        print('Calculating area of a rectangle')

    def draw(self):
        print('Drawing a rectangle')


class Triangle(Shape, Area):
    def calculate_area(self):
        print('Calculating area of a triangle')

    def draw(self):
        print('Drawing a triangle')


c = Circle()
c.draw()
c.calculate_area()

