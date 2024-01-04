from abc import ABC, abstractmethod

class Coffee (ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def get_ingredients(self):
        pass

class SimpleCoffee(Coffee):
    def get_cost(self):
        return 10

    def get_ingredients(self):
        return "Coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._component.get_cost() + 4

    def get_ingredients(self):
        return self._component.get_ingredients() +", Milk"

class EspressoDecorator (CoffeeDecorator):
    def get_cost(self):
        return self._component.get_cost() + 5

    def get_ingredients(self):
        return self._component.get_ingredients() +", Espresso "

# Client code
component = SimpleCoffee()
decorator1 = MilkDecorator(component)
decorator2 = EspressoDecorator(decorator1)
print("Coffee cost is :: %s" %decorator2.get_cost())
print("Coffee ingredients are :: %s" %decorator2.get_ingredients())


latte = MilkDecorator(MilkDecorator(SimpleCoffee()))
print("Coffee cost is :: %s" %latte.get_cost())
print("Coffee ingredients are :: %s" %latte.get_ingredients())

"""
Coffee cost is :: 19
Coffee ingredients are :: Coffee, Milk, Espresso 
Coffee cost is :: 18
Coffee ingredients are :: Coffee, Milk, Milk

"""
