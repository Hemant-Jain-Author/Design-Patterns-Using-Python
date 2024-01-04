from abc import ABC, abstractmethod

# Abstract ProductA
class ProductA(ABC):
    @abstractmethod
    def operationA(self):
        pass

# Concrete ProductA1
class ProductA1(ProductA):
    def operationA(self):
        print("ProductA1 operationA")

# Concrete ProductA2
class ProductA2(ProductA):
    def operationA(self):
        print("ProductA2 operationA")

# Abstract ProductB
class ProductB(ABC):
    @abstractmethod
    def operationB(self):
        pass

# Concrete ProductB1
class ProductB1(ProductB):
    def operationB(self):
        print("ProductB1 operationB")

# Concrete ProductB2
class ProductB2(ProductB):
    def operationB(self):
        print("ProductB2 operationB")

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_productA(self):
        pass
    
    @abstractmethod
    def create_productB(self):
        pass

# Concrete Factory1
class ConcreteFactory1(AbstractFactory):
    def create_productA(self):
        return ProductA1()
    
    def create_productB(self):
        return ProductB1()

# Concrete Factory2
class ConcreteFactory2(AbstractFactory):
    def create_productA(self):
        return ProductA2()
    
    def create_productB(self):
        return ProductB2()

# Client code
factory1 = ConcreteFactory1()
productA1 = factory1.create_productA()
productB1 = factory1.create_productB()
productA1.operationA()
productB1.operationB()

factory2 = ConcreteFactory2()
productA2 = factory2.create_productA()
productB2 = factory2.create_productB()
productA2.operationA()
productB2.operationB()

"""
ProductA1 operationA
ProductB1 operationB
ProductA2 operationA
ProductB2 operationB
"""