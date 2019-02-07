from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def draw(self):
        pass

class SimpleWindow(Window):
    def draw(self):
        print("SimpleWindow draw.")

class Decorator(Window):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def draw(self):
        pass

class VerticalScrollBarDecorator(Decorator):
    def draw(self):
        self._component.draw()
        print("VerticalScrollBarDecorator draw")

class HorizontalScrollBarDecorator (Decorator):
    def draw(self):
        self._component.draw()
        print("HorizontalScrollBarDecorator draw")

component = SimpleWindow()
decorator1 = VerticalScrollBarDecorator(component)
decorator2 = HorizontalScrollBarDecorator(decorator1)
decorator2.draw()