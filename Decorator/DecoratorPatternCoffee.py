from abc import ABC, abstractmethod

class Coffee (ABC):
    @abstractmethod
    def getCost(self):
        pass
    
    @abstractmethod
    def getIngredients(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 10

    def getIngredients(self):
        return "Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def getCost(self):
        pass

    @abstractmethod
    def getIngredients(self):
        pass

class MilkDecorator(CoffeeDecorator):
    def getCost(self):
        return self._component.getCost() + 4

    def getIngredients(self):
        return self._component.getIngredients() +", Milk"

class EspressoDecorator (CoffeeDecorator):
    def getCost(self):
        return self._component.getCost() + 5

    def getIngredients(self):
        return self._component.getIngredients() +", Espresso "

component = SimpleCoffee()
decorator1 = MilkDecorator(component)
decorator2 = EspressoDecorator(decorator1)
print("Coffee cost is :: %s" %decorator2.getCost())
print("Coffee ingredients are :: %s" %decorator2.getIngredients())


latte = MilkDecorator(MilkDecorator(SimpleCoffee()))
print("Coffee cost is :: %s" %latte.getCost())
print("Coffee ingredients are :: %s" %latte.getIngredients())