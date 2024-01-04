import math

class Shape:
	def area(self):
		pass

class Rectangle(Shape):
	def __init__(self, h, w):
		self.height = h
		self.width = w

	def area(self):
		return self.height*self.width

class Circle(Shape):
	def __init__(self, r):
		self.radius = r
	
	def area(self):
		return math.pi*self.radius*self.radius

def total_area(shapes):
	area = 0
	for shape in shapes:
		area += shape.area()
	return area

# Client code.
r = Rectangle(10,20)
c = Circle(10)
s = []
s.append(r)
s.append(c)

print(total_area(s))
