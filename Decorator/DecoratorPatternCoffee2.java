from abc import ABC, abstractmethod

class ICoffee (ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def get_ingredients(self):
        pass

class SimpleCoffee(ICoffee):
    def get_cost(self):
        return 10

    def get_ingredients(self):
        return "Coffee"

class CoffeeDecorator(ICoffee):
    def __init__(self, component, name = "", cost = 0):
        self._component = component
        self._cost = cost
        self._name = name

    def get_cost(self):
        return self._component.get_cost() + self._cost
    
    def get_ingredients(self):
        return self._component.get_ingredients() + ", " + self._name

class MilkDecorator(CoffeeDecorator):
    def __init__(self, component):
        super().__init__(component, "Milk", 4)

class EspressoDecorator (CoffeeDecorator):
    def __init__(self, component):
        super().__init__(component, "Espresso", 5)

# Client code
component = SimpleCoffee()
decorator1 = MilkDecorator(component)
decorator2 = EspressoDecorator(decorator1)
print("Coffee cost is :: %s" %decorator2.get_cost())
print("Coffee ingredients are :: %s" %decorator2.get_ingredients())


latte = MilkDecorator(MilkDecorator(SimpleCoffee()))
print("Coffee cost is :: %s" %latte.get_cost())
print("Coffee ingredients are :: %s" %latte.get_ingredients())