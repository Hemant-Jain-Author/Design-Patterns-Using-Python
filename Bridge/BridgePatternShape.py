
from abc import ABC, abstractmethod

class ShapeAbstraction(ABC):
    def __init__(self, imp):
        self._imp = imp

    @abstractmethod
    def draw(self):
        pass

class RectangeAbstraction(ShapeAbstraction):
    def draw(self):
        print("Drawing Rectange with color %s "%(self._imp.fill()))

class CircleAbstraction(ShapeAbstraction):
    def draw(self):
        print("Drawing Circle with color %s "%(self._imp.fill()))

class ColorImplementor(ABC):
    @abstractmethod
    def fill(self):
        pass

class RedImplementor(ColorImplementor):
    def fill(self):
        return "Red"

class GreenImplementor(ColorImplementor):
    def fill(self):
        return "Green"

class BlueImplementor(ColorImplementor):
    def fill(self):
        return "Blue"

# Client code.
c1 = RedImplementor()
abstraction = CircleAbstraction(c1)
abstraction.draw()

c1 = GreenImplementor()
abstraction = RectangeAbstraction(c1)
abstraction.draw()

"""
Drawing Circle with color Red 
Drawing Rectange with color Green 
"""