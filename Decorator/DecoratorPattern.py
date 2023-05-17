from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation.")

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operation(self):
        pass

class ConcreteDecorator1(Decorator):
    def operation(self):
        print("ConcreteDecorator1 operation start.")
        self._component.operation()
        print("ConcreteDecorator1 operation end.")

class ConcreteDecorator2(Decorator):
    def operation(self):
        print("ConcreteDecorator2 operation start.")
        self._component.operation()
        print("ConcreteDecorator2 operation end.")

#Client code.
component = ConcreteComponent()
decorator1 = ConcreteDecorator1(component)
decorator2 = ConcreteDecorator2(decorator1)
decorator2.operation()

"""
ConcreteDecorator2 operation start.
ConcreteDecorator1 operation start.
ConcreteComponent operation.
ConcreteDecorator1 operation end.
ConcreteDecorator2 operation end.
"""