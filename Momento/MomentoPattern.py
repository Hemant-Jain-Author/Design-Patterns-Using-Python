
class Originator :    
    def set_state(self, state) :
        self.state = state
    
    def get_state(self) :
        return self.state
    
    def create_memento(self) :
        return Memento(self.state)
    
    def set_memento(self, m) :
        self.state = m.get_state()

class Memento :
    def __init__(self, state) :
        self.state = state 

    # State is captured at init, no set_state(self, state) function.

    def get_state(self) :
        return self.state
    
class CareTaker :
    def __init__(self):
        self.history = []
        self.top = -1
        self.max = -1
    
    def add_memento(self, m) :
        self.top += 1
        self.max = self.top
        if self.top <= len(self.history) - 1:
            self.history[self.top] = m
        else :
            self.history.append(m)
    
    def get_memento(self, index) :
        return self.history[index]
    
    def undo(self) :
        print("Undoing state.")
        if (self.top <= 0):
            self.top = 0
            return self.get_memento(0)
        
        self.top -= 1
        return self.get_memento(self.top)

    def redo(self) :
        print("Redoing state.")
        if (self.top >= (len(self.history) -  1) or self.top >= self.max) :
            return self.get_memento(self.top)
        
        self.top += 1
        return self.get_memento(self.top)
    
    def get_states_count(self) :
        return len(self.history)
    
# Client code.
originator = Originator()
care_taker = CareTaker()

originator.set_state("State 1")
care_taker.add_memento(originator.create_memento())
print(originator.get_state())
originator.set_state("State 2")
care_taker.add_memento(originator.create_memento())
print(originator.get_state())
originator.set_state("State 3")
care_taker.add_memento(originator.create_memento())
print(originator.get_state())

originator.set_memento(care_taker.undo())
print(originator.get_state())
originator.set_memento(care_taker.undo())
print(originator.get_state())
originator.set_memento(care_taker.redo())
print(originator.get_state())
originator.set_memento(care_taker.redo())
print(originator.get_state())

"""
State 1
State 2
State 3
Undoing state.
State 2
Undoing state.
State 1
Redoing state.
State 2
Redoing state.
State 3
"""