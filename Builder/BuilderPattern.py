from abc import ABC, abstractmethod

class Product(object):
    def __init__(self, A = "A default", B = "B default"):
        self.partA = A
        self.partB = B
        
    def display(self):
        print("Product : (%s,%s)"%(self.partA,self.partB))

class Builder(ABC):
    def __init__(self):
        self.product = Product()

    @abstractmethod
    def setPartA(self, A):
        pass

    @abstractmethod
    def setPartB(self, B):
        pass

    def getProduct(self):
        temp = self.product
        self.product = Product() # assign new product.
        return temp

class ConcreteBuilder(Builder):
    def setPartA(self, A):
        self.product.partA = A
        return self

    def setPartB(self, B):
        self.product.partB = B
        return self

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        return self._builder.setPartA("A value").setPartB("B value").getProduct()

    def construct2(self):
        self._builder.setPartA("A value")
        self._builder.setPartB("B value")
        return  self._builder.getProduct()

    def construct3(self):
        return self._builder.setPartA("A value").getProduct()


builder = ConcreteBuilder()
director = Director(builder)
product = director.construct()
product2 = director.construct2()
product3 = director.construct3()
print(product, product2, product3)
product.display()
product2.display()
product3.display()