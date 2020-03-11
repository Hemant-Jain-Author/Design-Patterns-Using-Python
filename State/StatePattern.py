from abc import ABC, abstractmethod
import math

class BulbControl:
    def __init__(self):
        self.current = Off()
    
    def setState(self, state):
        self.current = state

    def flip(self):
        self.current.flip(self)

    def toString(self):
        return self.current.toString()

class BulbState(ABC):
    @abstractmethod
    def flip(self):
        pass

class On(BulbState):
    def flip(self, bc):
        bc.setState(Off())

    def toString(self):
        return "On"

class Off(BulbState):
    def flip(self, bc):
        bc.setState(On())

    def toString(self):
        return "Off"


c = BulbControl()
for i in range(10):
    c.flip()
    print(c.toString())
