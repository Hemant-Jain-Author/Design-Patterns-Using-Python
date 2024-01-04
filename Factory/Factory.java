from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Product classes
class Dog(Animal):
    def speak(self):
        print("Woof!") 

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Creator abstract class
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creator classes
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
Woof!
Meow!
"""