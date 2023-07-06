from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        print("Concrete Product1 Operation!")

class ConcreteProduct2(Product):
    def operation(self):
        print("Concrete Product2 Operation!")

       
# Creator abstract class
class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

# Concrete Creator classes
class ConcreteFactory1(Factory):
    def create_product(self):
        return ConcreteProduct1()

class ConcreteFactory2(Factory):
    def create_product(self):
        return ConcreteProduct2()

# Client code
f = ConcreteFactory1()
a = f.create_product()
a.operation()

f = ConcreteFactory2()
a = f.create_product()
a.operation()

""" Output:
Concrete Product1 Operation!
Concrete Product2 Operation!
"""
