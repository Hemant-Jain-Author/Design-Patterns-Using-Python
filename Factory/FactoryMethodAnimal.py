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

DogFactory().getAnimal().voice()
CatFactory().getAnimal().voice()