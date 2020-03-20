# Main application
class Originator : 
    def __init__(self) :
        self.careTaker = CareTaker()
    
    def setState(self, state) :
        self.state = state
        self.careTaker.addMemento(self.createMemento())
    
    def getState(self) :
        return self.state
    
    def createMemento(self) :
        return Memento(self.state)
    
    def setMemento(self, m) :
        self.state = m.getState()

    def undo(self) :
        self.setMemento(self.careTaker.undo())
        
    def redo(self) :
        self.setMemento(self.careTaker.redo())


# Wrapper around state.
class Memento : 
    def __init__(self, state) :
        self.state = state 

    # State is captured at init, no setState(self, state) function.

    def getState(self) :
        return self.state        


# CareTaker manages history.
class CareTaker :
    def __init__(self):
        self.history = []
        self.top = -1
        self.max = -1
    
    def addMemento(self, m) :
        self.top += 1
        self.max = self.top
        if self.top <= len(self.history) - 1:
            self.history[self.top] = m
        else :
            self.history.append(m)
    
    def getMemento(self, index) :
        return self.history[index]
    
    def undo(self) :
        print("Undoing state.")
        if (self.top <= 0):
            self.top = 0
            return self.getMemento(0)
        
        self.top -= 1
        return self.getMemento(self.top)

    def redo(self) :
        print("Redoing state.")
        if (self.top >= (len(self.history) -  1) or self.top >= self.max) :
            return self.getMemento(self.top)
        
        self.top += 1
        return self.getMemento(self.top)
    
    def getStatesCount(self) :
        return len(self.history)
    

# Testing Code
originator = Originator()
originator.setState("State 1")
print(originator.getState())

originator.setState("State 2")
print(originator.getState())

originator.setState("State 3")
print(originator.getState())

originator.undo()
print(originator.getState())

originator.undo()
print(originator.getState())

originator.redo()
print(originator.getState())

originator.redo()
print(originator.getState())
