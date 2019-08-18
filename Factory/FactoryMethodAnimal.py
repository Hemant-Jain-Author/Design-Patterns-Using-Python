from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def voice(self):
        print("Meow Meow!!")

## Animal factory defined
class AnimalFactory(ABC):
    @abstractmethod
    def getAnimal(self):
        pass

class CatFactory(AnimalFactory):
    def getAnimal(self):
        return Cat()

class DogFactory(AnimalFactory):
    def getAnimal(self):
        return Dog()

#Client Code
def clientCode(creator):
    creator.getAnimal().voice()

clientCode(DogFactory())
clientCode(CatFactory())

#loose coupeling 
# single responsibility principle.
# open close principle.


# Future changes to include cow type of objects.
class Cow(Animal):
    def voice(self):
        print("Gooaa Gooaa!!")

class CowFactory(AnimalFactory):
    def getAnimal(self):
        return Cow()

clientCode(CowFactory())
