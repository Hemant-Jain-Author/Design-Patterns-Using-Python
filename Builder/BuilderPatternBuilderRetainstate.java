from abc import ABC, abstractmethod

class Product(object):
    def __init__(self, A = "A default", B = "B default"):
        self.partA = A
        self.partB = B
        
    def __str__(self):
        return ("Product : (%s, %s)"%(self.partA,self.partB))

class Builder(ABC):
    @abstractmethod
    def set_PartA(self, A):
        pass

    @abstractmethod
    def set_PartB(self, B):
        pass

    @abstractmethod
    def get_Product(self):
        pass

class ConcreteBuilder(Builder):
    def set_PartA(self, A):
        self.partA = A
        return self  # returning self helps in chaining calls.

    def set_PartB(self, B):
        self.partB = B
        return self

    def get_Product(self):
        return Product(self.partA, self.partB)

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        return self._builder.set_PartA("A1").set_PartB("B1").get_Product() # chining calls

    def construct2(self):
        self._builder.set_PartA("A2")
        self._builder.set_PartB("B2")
        return  self._builder.get_Product()

# Client code.
builder = ConcreteBuilder()
director = Director(builder)
product = director.construct()
print(product)
product2 = director.construct2()
print(product2)

"""
Product : (A1, B1)
Product : (A2, B2)
"""