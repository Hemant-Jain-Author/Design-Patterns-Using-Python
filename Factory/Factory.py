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
class AnimalFactory(object):
    def getAnimal(self, object_type):
        if object_type == "Dog":
            return Dog()
        elif object_type == "Cat":
            return Cat()
        

f = AnimalFactory()
a = f.getAnimal("Dog")
a.voice()
a = f.getAnimal("Cat")
a.voice()

"""

Output:

Bhow Bhow!!
Meow Meow!!

"""
