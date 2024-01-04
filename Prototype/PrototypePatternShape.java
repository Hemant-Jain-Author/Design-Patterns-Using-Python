
from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    def __init__(self):
        self._color = ""
    
    @abstractmethod
    def __str__(self):
        return "Shape"
    
    @abstractmethod
    def clone(self):
        pass

class Rectangle(Shape):
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Rectangle."

class Circle(Shape):
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Circle."

class ShapeRegistry:
    _shapes = {}

    @staticmethod
    def add_shape(key, value):
        if key not in ShapeRegistry._shapes:
            ShapeRegistry._shapes[key] = value
    
    @staticmethod
    def get_shape(key):
        if key  in ShapeRegistry._shapes:
            return ShapeRegistry._shapes[key].clone()
        return None

    @staticmethod
    def load():
        ShapeRegistry.add_shape("circle", Circle())
        ShapeRegistry.add_shape("rectangle", Rectangle())

# Client code
ShapeRegistry.load()
c = ShapeRegistry.get_shape("circle")
r = ShapeRegistry.get_shape("rectangle")
print(c, r)

"""
Circle. Rectangle.
"""