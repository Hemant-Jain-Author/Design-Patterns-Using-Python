class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def fly(self):
        if self.name == "Dodo":
            print("The dodo is extinct and cannot fly.")
        elif self.name == "Penguin":
            print("The penguin cannot fly.")
        elif self.name == "Eagle":
            print("The eagle is soaring through the sky!")
        elif self.name == "Sparrow":
            print("The sparrow is fluttering its wings!")

# Client code.
bird1 = Bird("Eagle")
bird1.fly()

bird2 = Bird("Dodo")
bird2.fly()

"""
The eagle is soaring through the sky!
The dodo is extinct and cannot fly.
"""