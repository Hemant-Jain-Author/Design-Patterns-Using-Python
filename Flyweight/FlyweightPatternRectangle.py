from abc import ABC, abstractmethod
import random

class Shape(ABC):
    def __init__(self, colour):
        self._colour = colour # Intrinsic State

    @abstractmethod
    def draw(self, x1, y1, x2, y2): # Extrinsic State
        print

class Rectange(Shape):
    def draw(self, x1, y1, x2, y2):
        print("Draw rectange colour:%s topleft: (%s,%s) rightBottom: (%s,%s)"%(self._colour,x1, y1, x2, y2) )

class RectangeFactory:
    def __init__(self):
        self._shapes = {}

    def get_rectange(self, colour):
        if colour not in self._shapes:
            self._shapes[colour] = Rectange(colour)
        return self._shapes[colour]
    
    def get_count(self):
        return len(self._shapes)

# Client code.
factory = RectangeFactory()
for i in range(1000):
    rect = factory.get_rectange(random.randint(1,1000))
    rect.draw(random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100))
print(factory.get_count())

