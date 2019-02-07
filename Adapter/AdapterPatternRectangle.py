from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.radious = r

    def draw(self):
        print("Draw the Circle.")


class RectangeAdapter(Shape):
    def __init__(self, x, y, l, w):
        self._adaptee = Rectange(x, y, l, w)
        
    def draw(self):
        self._adaptee.oldDraw()

class Rectange:
    def __init__(self, x, y, l, w):
        self.x = x
        self.y = y
        self.length = l
        self.width = w

    def oldDraw(self):
        print("Draw the Rectangle.")


adapter = RectangeAdapter(1,2,3,4)
adapter.draw()