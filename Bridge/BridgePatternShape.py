
from abc import ABC, abstractmethod

class Shape(ABC): # Abstraction
    def __init__(self, imp):
        self._imp = imp

    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle with color %s "%(self._imp.fill()))

class Circle(Shape):
    def draw(self):
        print("Drawing Circle with color %s "%(self._imp.fill()))

class Color(ABC): # Implementor
    @abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        return "Red"

class Green(Color):
    def fill(self):
        return "Green"

class Blue(Color):
    def fill(self):
        return "Blue"

# Client code.
c1 = Red()
abstraction = Circle(c1)
abstraction.draw()

c1 = Green()
abstraction = Rectangle(c1)
abstraction.draw()

"""
Drawing Circle with color Red 
Drawing Rectangle with color Green 
"""