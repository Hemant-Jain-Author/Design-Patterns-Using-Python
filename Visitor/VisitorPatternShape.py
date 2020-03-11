from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def name(self):
        return "Circle"    
        
    def accept(self, visitor):
        return visitor.visitCircle(self)

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def name(self):
        return "Rectangle"

    def accept(self, visitor):
        return visitor.visitRectange(self)

class Dot(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def name(self):
        return "Dot"

    def accept(self, visitor):
        return visitor.visitDot(self)

class Visitor(ABC):
    def visitCircle(self, element):
        pass

    def visitRectange(self, element):
        pass

    def visitDot(self, element):
        pass
        
class XMLVisitor(Visitor):
    def visitCircle(self, element):
        return "<circle>\n  <x>%s</x>\n  <y>%s</y>\n  <radius>%s</radius>\n</circle>"%(element.x, element.y, element.radius) 

    def visitRectange(self, element):
        return "<rectangle>\n  <x>%s</x>\n  <y>%s</y>\n  <width>%s</width>\n  <height>%s</height>\n</rectangle>"%(element.x, element.y, element.width, element.height)

    def visitDot(self, element):
        return "<dot>\n  <x>%s</x>\n  <y>%s</y>\n</dot>"%(element.x, element.y)

class TextVisitor(Visitor):
    def visitCircle(self, element):
        return "Circle ( (x : %s, y : %s), radius : %s) "%(element.x, element.y, element.radius)

    def visitRectange(self, element):
        return "Rectangle ( (x : %s, y : %s), width : %s, height : %s)"%(element.x, element.y, element.width, element.height)

    def visitDot(self, element):
        return "Dot ( x : %s, y : %s)"%(element.x, element.y)

class ObjectsStructure:
    def __init__(self):
        self.shapes = []

    def addShapes(self, shape):
        self.shapes.append(shape)

    def setVisitor(self, visitor):
        self.visitor = visitor

    def accept(self):
        for shape in self.shapes:
            print(shape.accept(self.visitor))

os = ObjectsStructure()
os.addShapes(Rectangle(6,7,8,9))
os.addShapes(Circle(6,7,8))
os.addShapes(Dot(6,7))
os.setVisitor(XMLVisitor())
os.accept()

os.setVisitor(TextVisitor())
os.accept()
