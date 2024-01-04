from abc import ABC, abstractmethod
import random
import timeit

class Shape(ABC):
    def __init__(self, color):
        self._color = color # Intrinsic State
        self._demoData = [0]*10000 # demo Intrinsic State.

    @abstractmethod
    def draw(self, x1, y1, x2, y2): # Extrinsic State
        pass

class RectangeIntrinsic(Shape):
    def draw(self, x1, y1, x2, y2):
        print("Draw rectange color:%s topleft: (%s,%s) rightBottom: (%s,%s)"%(self._color,x1, y1, x2, y2) )

class RectangeFactory:
    def __init__(self):
        self._shapes = {}

    def get_Rectange(self, color):
        if color not in self._shapes:
            self._shapes[color] = RectangeIntrinsic(color)
        return self._shapes[color]


class Rectangle:
    def __init__(self, factory, color, x1, y1, x2, y2):
        self.flyweitht = factory.get_Rectange(color)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        print("Operation inside Rectangle.")
        self.flyweitht.draw(self.x1, self.y1, self.x2, self.y2)

# Client code
def test():
    factory = RectangeFactory()
    rarr = []
    for i in range(10000):
        rarr.append(Rectangle(factory, random.randint(1,10), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)))


class Rectangle2:
    def __init__(self, color, x1, y1, x2, y2):
        self._color = color 
        self._demoData = [0]*10000 # demo Intrinsic State.
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Draw rectange color:%s topleft: (%s,%s) rightBottom: (%s,%s)"%(self._color,self.x1, self.y1, self.x2, self.y2) )
        

def test2():
    rarr2 = []
    for i in range(10000):
        rarr2.append(Rectangle2(random.randint(1,10), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)))


print(timeit.timeit(test, number=1))
print(timeit.timeit(test2, number=1))