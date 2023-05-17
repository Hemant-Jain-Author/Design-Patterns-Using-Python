from abc import ABC, abstractmethod
import math

class BulbControl:
    def __init__(self):
        self.current = Off()
    
    def set_state(self, state):
        self.current = state

    def flip(self):
        self.current.flip(self)

    def to_string(self):
        return self.current.to_string()

class BulbState(ABC):
    @abstractmethod
    def flip(self):
        pass

class On(BulbState):
    def flip(self, bc):
        bc.set_state(Off())

    def to_string(self):
        return "On"

class Off(BulbState):
    def flip(self, bc):
        bc.set_state(On())

    def to_string(self):
        return "Off"

# Client code.
c = BulbControl()
c.flip()
print(c.to_string())
c.flip()
print(c.to_string())