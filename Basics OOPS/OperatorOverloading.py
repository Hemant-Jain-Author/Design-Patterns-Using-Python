import math

class Rectangle(object):
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
  
    def area(self):
        return self.__length * self.__breadth
 
    def perimeter(self):
        return 2 * (self.__length + self.__breadth)
    
    # overloading + operator
    def __add__(self, rec):
        return Rectangle(self.__length + rec.__length, self.__breadth + rec.__breadth)
 
    # overloading - operator
    def __sub__(self, rec):
        return Rectangle(abs(self.__length - rec.__length), abs(self.__breadth - rec.__breadth))
 
    # overloading == operator
    def __eq__(self, rec):
        return (self.__length == rec.__length) and (self.__breadth == rec.__breadt)
 
    # overriding __str__ function
    def __str__(self):
        return "Rectange length and width: %s %s" % (self.__length , self.__breadth )
 
 
r1 = Rectangle(4, 6)
r2 = Rectangle(10, 6) 
print("Is r1 == r2 ?", r1 == r2)   
 
r3 = r1 + r2  
r4 = r1 - r2  
print(r1)  
print(r2)  
print(r3)  
print(r4)  
