class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
	def fly(self):
		pass

class Dodo(Bird):
	def fly(self):
		print("The dodo is extinct and cannot fly.")

class Penguin(Bird):
	def fly(self):
		print("The penguin cannot fly.")

	def slide(self):
		print("The penguin is sliding on its belly!")

	def swim(self):
		print("The penguin is swimming in the water!")

class Eagle(Bird):
	def fly(self):
		print("The eagle is soaring through the sky!")

class Sparrow(Bird):
	def fly(self):
		print("The sparrow is fluttering its wings!")

# Client code.
bird1 = Eagle("Eagle")
bird1.fly()

bird2 = Dodo("Dodo")
bird2.fly()

"""
The eagle is soaring through the sky!
The dodo is extinct and cannot fly.
"""

class Pigeon(Bird):
	def make_cooing_sound(self):
		print("The pigeon is making a cooing sound.")
	
	def fly(self):
		print("The pigeon is fluttering its wings!")

bird3 = Pigeon("Pigeon")
bird3.fly()

"""
The pigeon is fluttering its wings!
"""