from abc import ABC, abstractmethod

class Flyweight(ABC):
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state  # intrinsic state

    @abstractmethod
    def operation(self, extrinsic_state): # extrinsic state
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print("Operation inside concrete flyweight")

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight(key)
        return self._flyweights[key]
    
    def get_count(self):
        return len(self._flyweights)

# Client code.
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("key")
flyweight2 = factory.get_flyweight("key")
flyweight1.operation(None)
print(flyweight1, flyweight2)
print("Object count:", factory.get_count())

"""
Operation inside concrete flyweight
<__main__.ConcreteFlyweight object at 0x000002A12546BBB0> <__main__.ConcreteFlyweight object at 0x000002A12546BBB0>
Object count: 1
"""