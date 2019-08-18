from abc import ABC, abstractmethod
import random
import timeit

class Shape(ABC):
    def __init__(self, color):
        self._color = color # Intrinsic State

    @abstractmethod
    def draw(self, x1, y1, x2, y2): # Extrinsic State
        print

class Rectange(Shape):
    def draw(self, x1, y1, x2, y2):
        # print("Draw rectange color:%s topleft: (%s,%s) rightBottom: (%s,%s)"%(self._color,x1, y1, x2, y2) )
        pass

class RectangeFactory:
    def __init__(self):
        self._shapes = {}

    def get_Rectange(self, color):
        if color not in self._shapes:
            self._shapes[color] = Rectange(color)
        return self._shapes[color]


def test():
    factory = RectangeFactory()
    for i in range(10000):
        rect = factory.get_Rectange(random.randint(1,10))
        rect.draw(random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100))

class Rectange2(object):
    def __init__(self, color, x1, y1, x2, y2):
        self._color = color 
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        #print("Draw rectange color:%s topleft: (%s,%s) rightBottom: (%s,%s)"%(self._color,self.x1, self.y1, self.x2, self.y2) )
        pass
        
def test2():
    for i in range(100000):
        rect = Rectange2(random.randint(1,10), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100))
        rect.draw()

print(timeit.timeit(test, number=1))
print(timeit.timeit(test2, number=1))