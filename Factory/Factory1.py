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
class Factory(object):
    def getObject(self, object_type):
        if object_type == "Product1":
            return Product1()
        elif object_type == "Product2":
            return Product2()
f = Factory()
a = f.getObject("Product1")
a.operation()

a = f.getObject("Product2")
a.operation()

""" Output:
Product1 Operation!
Product2 Operation!
"""
