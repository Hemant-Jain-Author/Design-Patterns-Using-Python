from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color='black'):
        self.__color = color
 
    def getColor(self):
        return self.__color
 
    def setColor(self, color):
        self.__color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass    
 



class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
 
    def getLength(self):
        return self.__length
 
    def setLength(self, length):
        self.__length = length
 
    def getBreadth(self):
        return self.__breadth
 
    def setBreadth(self, breadth):
        self.__breadth = breadth
 
    def area(self):
        return self.__length * self.__breadth
 
    def perimeter(self):
        return 2 * (self.__length + self.__breadth)



class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius
 
    def setRadius(self, radius):
        self.__radius = radius
 
    def area(self):
        return math.pi * self.__radius ** 2
 
    def perimeter(self):
        return 2 * math.pi * self.__radius


r = Rectangle(10, 20)
print(r.area(), r.perimeter())

c = Circle(10)
print(c.area(), c.perimeter())

# s = Shape()
# print(s.area(), s.perimeter())
# these line will not compile as abc cant be instantiated.