import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    
def total_area(shapes):
    area = 0
    for shape in shapes:
        if isinstance(shape, Rectangle):
            area += shape.width *shape.height
        else:
            area += shape.radius * shape.radius * math.pi
    return area

# Client code.
r = Rectangle(10,20)
c = Circle(10)
s = []
s.append(r)
s.append(c)


print(total_area(s))
