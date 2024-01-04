
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    

class Bird(Animal):   
    def make_sound(self):
        print(f"{self.name} is making a chirp sound.")


class ICanFly:   
    def fly(self):
        pass


class ICanSwim:   
    def swim(self):
        pass

class ICanWalk :
    def walk(self):
        pass

class Dodo(Bird, ICanWalk):
    def walk(self):
        print("The dodo is extinct and can just walk.")

class Penguin(Bird, ICanSwim):
    def swim(self):
        print("The penguin is swimming!")

class Eagle(Bird, ICanFly):
    def fly(self):
        print("The eagle is soaring through the sky!")



bird1 = Eagle("Eagle")
bird1.fly()

bird2 = Penguin("Penguin")
bird2.swim()

bird3 = Dodo("Dodo")
bird3.walk()
