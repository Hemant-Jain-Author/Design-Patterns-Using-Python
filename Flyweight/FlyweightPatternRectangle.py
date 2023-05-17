from abc import ABC, abstractmethod
import random

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

    def get_rectange(self, color):
        if color not in self._shapes:
            self._shapes[color] = Rectange(color)
        return self._shapes[color]
    
    def get_count(self):
        return len(self._shapes)

# Client code.
factory = RectangeFactory()
for i in range(100000):
    rect = factory.get_rectange(random.randint(1,1000))
    rect.draw(random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100))
print(factory.get_count())

