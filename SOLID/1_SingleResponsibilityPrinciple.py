class Animal:
	def __init__(self, name):
		self.name = name

	def eat(self):
		print(f"{self.name} is eating.")

	def sleep(self):
		print(f"{self.name} is sleeping.")

	def make_sound(self):
		print(f"{self.name} is making a sound.")

class Mammal(Animal):
	def give_birth(self):
		print(f"{self.name} is giving birth to live young.")

class Reptile(Animal):
	def lay_eggs(self):
		print(f"{self.name} is laying eggs.")

class Bird(Animal):
	def fly(self):
		print(f"{self.name} is flying.")

	def lay_eggs(self):
		print(f"{self.name} is laying eggs.")

# Client code.
animal1 = Mammal("Cat")
animal1.give_birth()
animal1.make_sound()

animal2 = Reptile("Snake")
animal2.lay_eggs()
animal2.eat()

animal3 = Bird("Eagle")
animal3.fly()
animal3.lay_eggs()

"""
Cat is giving birth to live young.
Cat is making a sound.
Snake is laying eggs.
Snake is eating.
Eagle is flying.
Eagle is laying eggs.
"""