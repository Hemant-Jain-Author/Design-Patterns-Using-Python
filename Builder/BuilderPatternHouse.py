from abc import ABC, abstractmethod

# A class representing a house
class House(object):
    def __init__(self, wall="", roof=""):
        self.wall = wall
        self.roof = roof
        
    def display(self):
        print("House of %s and %s"%(self.wall,self.roof))

# An abstract builder class that specifies the interface for building a house
class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @abstractmethod
    def setWall(self):
        pass

    @abstractmethod
    def setRoof(self):
        pass

    def getHouse(self):
        temp = self.house
        self.house = House() # assign new house.
        return temp

# A builder class that builds a wooden house
class WoodenHouseBuilder(HouseBuilder):
    def setWall(self):
        self.house.wall = "Wooden Wall"
        return self

    def setRoof(self):
        self.house.roof = "Wooden Roof"
        return self

# A builder class that builds a concrete house
class ConcreteHouseBuilder(HouseBuilder):
    def setWall(self):
        self.house.wall = "Concrete Wall"
        return self

    def setRoof(self):
        self.house.roof = "Concrete Roof"
        return self

# A class that directs the building of a house
class HouseDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        return self._builder.setWall().setRoof().getHouse()

# Building a concrete house using a ConcreteHouseBuilder object
builder = ConcreteHouseBuilder()
director = HouseDirector(builder)
house = director.construct()
house.display()

# Building a wooden house using a WoodenHouseBuilder object
builder = WoodenHouseBuilder()
director = HouseDirector(builder)
house2 = director.construct()
house2.display()

print(house, house2)
