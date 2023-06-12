from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class Product1(Product):
    def operation(self):
        print("Product1 Operation!")

class Product2(Product):
    def operation(self):
        print("Product2 Operation!")

## factory defined
class Factory(ABC):
    @abstractmethod
    def get_object(self):
        pass

class ConcreteFactory1(Factory):
    def get_object(self):
        return Product1()

class ConcreteFactory2(Factory):
    def get_object(self):
        return Product2()


# Client code
f = ConcreteFactory1()
a = f.get_object()
a.operation()

f = ConcreteFactory2()
a = f.get_object()
a.operation()

""" Output:
Product1 Operation!
Product2 Operation!
"""
