from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Product Classes
class Dog(Animal):
    def speak(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def speak(self):
        print("Meow Meow!!")

# Creator Abstract Class
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creator Classes
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Client code
dog_factory = DogFactory()
dog = dog_factory.create_animal()
dog.speak()
cat_factory = CatFactory()
cat = cat_factory.create_animal()
cat.speak()

        


"""
Bhow Bhow!!
Meow Meow!!
"""
