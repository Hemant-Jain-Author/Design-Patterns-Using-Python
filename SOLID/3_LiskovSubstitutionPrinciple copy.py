from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.flight_height = 0

    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("The sparrow is fluttering its wings.")
        self.flight_height = 100

class Penguin(Bird):
    def fly(self):
        print("The penguin cannot fly.")

    def slide(self):
        print("The penguin is sliding on its belly!")

    def swim(self):
        print("The penguin is swimming in the water!")

class Dodo(Bird):
    def fly(self):
        print("The dodo is extinct and cannot fly.")

def test(bird):
    bird.fly()
    if bird.flight_height > 0:
        print("Bird is flying at a positive height.")
    else:
        print("Error: fly() method called; flight height is still zero.")

# Client code.
sparrow = Sparrow("Sparrow")
test(sparrow)

penguin = Penguin("Penguin")
test(penguin)
penguin.slide()
penguin.swim()

dodo = Dodo("Dodo")
test(dodo)

"""
The sparrow is fluttering its wings.
Bird is flying at a positive height.
The penguin cannot fly.
Error: fly() method called; flight height is still zero.
The penguin is sliding on its belly!
The penguin is swimming in the water!
The dodo is extinct and cannot fly.
Error: fly() method called; flight height is still zero.
"""