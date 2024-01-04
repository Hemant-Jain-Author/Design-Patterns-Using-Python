from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):   # Final method
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

class ConcreteClass1(AbstractClass):
    def operation1(self):
        print("Concrete Class 1 : Operation 1")

    def operation2(self):
        print("Concrete Class 1 : Operation 2")

class ConcreteClass2(AbstractClass):
    def operation1(self):
        print("Concrete Class 2 : Operation 1")

    def operation2(self):
        print("Concrete Class 2 : Operation 2")


# Client Code
concrete_class = ConcreteClass1()
concrete_class.template_method()

"""
Concrete Class 1 : Operation 1
Concrete Class 1 : Operation 2
"""
