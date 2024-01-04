from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
    def accept(self, visitor):
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectange(self)

class Visitor(ABC):
    def visit_circle(self, element):
        pass

    def visit_rectange(self, element):
        pass
        
class XMLVisitor(Visitor):
    def visit_circle(self, element):
        return "<circle>\n  <x>%s</x>\n  <y>%s</y>\n  <radius>%s</radius>\n</circle>"%(element.x, element.y, element.radius) 

    def visit_rectange(self, element):
        return "<rectangle>\n  <x>%s</x>\n  <y>%s</y>\n  <width>%s</width>\n  <height>%s</height>\n</rectangle>"%(element.x, element.y, element.width, element.height)

class TextVisitor(Visitor):
    def visit_circle(self, element):
        return "Circle ( (x : %s, y : %s), radius : %s) "%(element.x, element.y, element.radius)

    def visit_rectange(self, element):
        return "Rectangle ( (x : %s, y : %s), width : %s, height : %s)"%(element.x, element.y, element.width, element.height)

class ObjectsStructure:
    def __init__(self):
        self.shapes = []

    def add_shapes(self, shape):
        self.shapes.append(shape)

    def set_visitor(self, visitor):
        self.visitor = visitor

    def accept(self):
        for shape in self.shapes:
            print(shape.accept(self.visitor))

# Test Code
os = ObjectsStructure()
os.add_shapes(Rectangle(6,7,8,9))
os.add_shapes(Circle(6,7,8))
os.set_visitor(XMLVisitor())
os.accept()

os.set_visitor(TextVisitor())
os.accept()

"""
Output:
<rectangle>
  <x>6</x>
  <y>7</y>
  <width>8</width>
  <height>9</height>
</rectangle>
<circle>
  <x>6</x>
  <y>7</y>
  <radius>8</radius>
</circle>
<dot>
  <x>6</x>
  <y>7</y>
</dot>

Rectangle ( (x : 6, y : 7), width : 8, height : 9)
Circle ( (x : 6, y : 7), radius : 8) 
Dot ( x : 6, y : 7)
"""
