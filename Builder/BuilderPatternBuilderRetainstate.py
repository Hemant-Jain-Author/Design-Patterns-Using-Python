from abc import ABC, abstractmethod

class Product(object):
    def __init__(self, A = "A default", B = "B default"):
        self.partA = A
        self.partB = B
        
    def display(self):
        print("Product : (%s,%s)"%(self.partA,self.partB))

class Builder(ABC):
    @abstractmethod
    def setPartA(self, A):
        pass

    @abstractmethod
    def setPartB(self, B):
        pass

    @abstractmethod
    def getProduct(self):
        pass

class ConcreteBuilder(Builder):
    def setPartA(self, A):
        self.partA = A
        return self  # returning self helps in chaining calls.

    def setPartB(self, B):
        self.partB = B
        return self

    def getProduct(self):
        return Product(self.partA, self.partB)

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        return self._builder.setPartA("A value").setPartB("B value").getProduct() # chining calls

    def construct2(self):
        self._builder.setPartA("A value")
        self._builder.setPartB("B value")
        return  self._builder.getProduct()

builder = ConcreteBuilder()
director = Director(builder)
product = director.construct()
product2 = director.construct2()
print(product, product2)
product.display()
product2.display()