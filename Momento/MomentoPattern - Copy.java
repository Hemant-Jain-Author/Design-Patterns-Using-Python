# Main application
class Originator : 
    def __init__(self) :
        self.care_taker = CareTaker()
    
    def set_state(self, state) :
        self.state = state
        self.care_taker.add_memento(self.create_memento())
    
    def get_state(self) :
        return self.state
    
    def create_memento(self) :
        return Memento(self.state)
    
    def set_memento(self, m) :
        self.state = m.get_state()

    def undo(self) :
        self.set_memento(self.care_taker.undo())
        
    def redo(self) :
        self.set_memento(self.care_taker.redo())


# Wrapper around state.
class Memento : 
    def __init__(self, state) :
        self.state = state 

    # State is captured at init, no set_state(self, state) function.

    def get_state(self) :
        return self.state        


# CareTaker manages history.
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
    

# Client code
originator = Originator()
originator.set_state("State 1")
print(originator.get_state())
originator.set_state("State 2")
print(originator.get_state())
originator.set_state("State 3")
print(originator.get_state())

originator.undo()
print(originator.get_state())
originator.undo()
print(originator.get_state())
originator.redo()
print(originator.get_state())
originator.redo()
print(originator.get_state())
