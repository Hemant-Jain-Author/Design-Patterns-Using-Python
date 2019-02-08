from abc import ABC, abstractmethod

class ICoffee (ABC):
    @abstractmethod
    def getCost(self):
        pass
    
    @abstractmethod
    def getIngredients(self):
        pass

class SimpleCoffee(ICoffee):
    def getCost(self):
        return 10

    def getIngredients(self):
        return "Coffee"

class CoffeeDecorator(ICoffee):
    def __init__(self, component, name = "", cost = 0):
        self._component = component
        self._cost = cost
        self._name = name

    def getCost(self):
        return self._component.getCost() + self._cost
    
    def getIngredients(self):
        return self._component.getIngredients() + ", " + self._name

class MilkDecorator(CoffeeDecorator):
    def __init__(self, component):
        super().__init__(component, "Milk", 4)

class EspressoDecorator (CoffeeDecorator):
    def __init__(self, component):
        super().__init__(component, "Espresso", 5)

component = SimpleCoffee()
decorator1 = MilkDecorator(component)
decorator2 = EspressoDecorator(decorator1)
print("Coffee cost is :: %s" %decorator2.getCost())
print("Coffee ingredients are :: %s" %decorator2.getIngredients())


latte = MilkDecorator(MilkDecorator(SimpleCoffee()))
print("Coffee cost is :: %s" %latte.getCost())
print("Coffee ingredients are :: %s" %latte.getIngredients())