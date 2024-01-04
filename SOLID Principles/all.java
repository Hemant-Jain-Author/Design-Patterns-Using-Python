class Bird:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    
    def fly(self):
        print(f"{self.name} is flying!")
    

class Penguin(Bird):
    def fly(self):
        print(f"{self.name} cannot fly!")
    
    def slide(self):
        print(f"{self.name} is sliding on its belly!")

    def swim(self):
        print(f"{self.name} is swimming!")

class Dodo(Bird):
    def fly(self):
        print(f"{self.name} is extinct and cannot fly!")

    