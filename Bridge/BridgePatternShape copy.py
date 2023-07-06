# Abstraction
class Shape:
    def __init__(self, implementation):
        self.implementation = implementation
        
    def draw(self):
        pass
    
# Concrete Abstraction
class Square(Shape):
    def draw(self):
        self.implementation.draw_square()
        
class Circle(Shape):
    def draw(self):
        self.implementation.draw_circle()
    
# Implementation
class DrawingAPI:
    def draw_square(self):
        pass
    
    def draw_circle(self):
        pass
    
# Concrete Implementation
class WindowsAPI(DrawingAPI):
    def draw_square(self):
        print("Drawing a square on Windows.")
        
    def draw_circle(self):
        print("Drawing a circle on Windows.")
        
class MacAPI(DrawingAPI):
    def draw_square(self):
        print("Drawing a square on Mac.")
        
    def draw_circle(self):
        print("Drawing a circle on Mac.")
        
# Usage
windows_api = WindowsAPI()
mac_api = MacAPI()

square = Square(windows_api)
square.draw() # Output: Drawing a square on Windows.

circle = Circle(mac_api)
circle.draw() # Output: Drawing a circle on Mac.
