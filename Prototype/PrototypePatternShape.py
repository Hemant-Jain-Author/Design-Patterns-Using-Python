
from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    def __init__(self):
        self._color = ""

    @abstractmethod
    def draw(self):
        print("shape")

    @abstractmethod
    def clone(self):
        print("clone")

class Rectangle(Shape):
    def clone(self):
        print("rectangle clone")
        return copy.deepcopy(self)

    def draw(self):
        print("rectangle draw")

class Circle(Shape):
    def clone(self):
        print("cirtcle clone")
        return copy.deepcopy(self)

    def draw(self):
        print("circle draw")

class ShapeFactory:
    _shapes = {}

    @staticmethod
    def addShape(key, value):
        if key not in ShapeFactory._shapes:
            ShapeFactory._shapes[key] = value
    
    @staticmethod
    def getShape(key):
        if key  in ShapeFactory._shapes:
            return ShapeFactory._shapes[key].clone()
        return None

    @staticmethod
    def load():
        ShapeFactory.addShape("circle", Circle())
        ShapeFactory.addShape("rectangle", Rectangle())

ShapeFactory.load()
c = ShapeFactory.getShape("circle")
c.draw()
c2 = ShapeFactory.getShape("circle")
c2.draw()
print(c, c2)