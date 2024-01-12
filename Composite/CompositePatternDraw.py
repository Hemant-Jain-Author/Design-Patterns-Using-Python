from abc import ABC, abstractmethod

class IShape:
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod    
    def draw(self):
        pass

class Rectangle(IShape):
    def __init__(self, x, y, l, b):
        self.x = x
        self.y = y
        self.l = l
        self.b = b

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print("Draw a Rectangle at (%s, %s)."%(self.x, self.y))
        return "<Rectangle>"

class Circle(IShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print("Draw a Circle of radius %s at (%s, %s) ."%(self.radius, self.x, self.y))
        return "<Circle>"

class CompoundShape(IShape):
    def __init__(self):
        self.children = set()
    
    def add(self, child):
        self.children.add(child)

    def remove(self, child):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        st = "Shapes("
        for child in self.children:
            st += child.draw()
        st += ")"
        return st

# Client code.      
all =  CompoundShape()
all.add( Rectangle(1, 2, 1, 2))
all.add( Circle(5, 3, 10))
group = CompoundShape()
group.add(Rectangle(5, 7, 1, 2))
group.add(Circle(2, 1, 2))
all.add(group)
print(all.draw())

"""
Draw a Rectangle at (1, 2).
Draw a Circle of radius 2 at (2, 1) .
Draw a Rectangle at (5, 7).
Draw a Circle of radius 10 at (5, 3) .
Shapes(<Rectangle>Shapes(<Circle><Rectangle>)<Circle>)
"""