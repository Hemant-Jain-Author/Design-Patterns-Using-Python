from abc import ABC, abstractmethod

# Define the Product class with two parts
class Product(object):
    def __init__(self, A = "A default", B = "B default"):
        self.partA = A
        self.partB = B
        
    def __str__(self):
        return ("Product : (%s, %s)"%(self.partA,self.partB))

# Define an abstract class called Builder
class Builder(ABC):
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def set_PartA(self, A):
        pass

    @abstractmethod
    def set_PartB(self, B):
        pass

    def get_product(self):
        temp = self.product
        self.product = Product() # assign new product.
        return temp

# Define a ConcreteBuilder class that extends Builder
class ConcreteBuilder(Builder):
    def set_PartA(self, A):
        self.product.partA = A
        return self

    def set_PartB(self, B):
        self.product.partB = B
        return self

# Define a Director class that takes a builder object as a parameter
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        return self._builder.set_PartA("A1").set_PartB("B1").get_product()

    def construct2(self):
        self._builder.set_PartA("A2")
        self._builder.set_PartB("B2")
        return  self._builder.get_product()

    def construct3(self):
        return self._builder.set_PartA("A3").get_product()

# Client code.
builder = ConcreteBuilder()
director = Director(builder)
product = director.construct()
print(product)

product2 = director.construct2()
print(product2)

product3 = director.construct3()
print(product3)

"""
Product : (A1, B1)
Product : (A2, B2)
Product : (A3, B default)
"""