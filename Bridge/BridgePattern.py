
from abc import ABC, abstractmethod

class Abstraction(ABC):
    def __init__(self, imp):
        self._imp = imp

    @abstractmethod
    def operation(self):
        pass

class ConcreteAbstraction(Abstraction):
    def operation(self):
        self._imp.operation()


class Implementor(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteImplementor1(Implementor):
    def operation(self):
        print("ConcreteImplementor1 operation")


class ConcreteImplementor2(Implementor):
    def operation(self):
        print("ConcreteImplementor2 operation")

c1 = ConcreteImplementor1()
abstraction = ConcreteAbstraction(c1)
abstraction.operation()