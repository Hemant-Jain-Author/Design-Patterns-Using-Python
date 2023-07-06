
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
    def __init__(self):
        self.flight_height = 0
    
    def fly(self):
        pass


class Dodo(Bird):
    def walk(self):
        print("The dodo is extinct and can just walk.")


class Eagle(Bird, ICanFly):
    def fly(self):
        print("The eagle is soaring through the sky!")
        self.flight_height = 1000

class Pigeon(Bird, ICanFly):
    def fly(self):
        print("The pigeon is fluttering its wings!")
        self.flight_height = 100


def test(flying_animal: ICanFly):
    flying_animal.fly()
    assert flying_animal.flight_height > 0, 
    "Error: Animal is still at a zero height."
    print("Animal is flying at a positive height.")

bird1 = Eagle("Eagle")
test(bird1)

bird2 = Pigeon("Eagle")
test(bird2)

bird3 = Dodo("Dodo")
test(bird3)
