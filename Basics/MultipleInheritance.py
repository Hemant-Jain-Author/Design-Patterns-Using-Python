from abc import ABC, abstractmethod
import math

class Color(ABC):
    def __init__(self, color='black'):
        self.__color = color
 
    def getColor(self):
        return self.__color
 
    def setColor(self, color):
        self.__color = color

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass    
 

class Rectangle(Shape, Color):
    def __init__(self, length, breadth, color):
        Color.__init__(self, color)
        Shape.__init__(self)
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

r = Rectangle(10, 20, 'red')
print(r.area(), r.perimeter(), r.getColor())
r.setColor('white')
print(r.area(), r.perimeter(), r.getColor())