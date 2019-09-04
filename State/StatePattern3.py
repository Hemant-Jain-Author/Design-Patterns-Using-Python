from abc import ABC, abstractmethod
import math

class Context:
    def __init__(self, state):
        self.currentState = state
        self.states = {1:ConcreteState1(), 2:ConcreteState2()}

    def changeState(self, id):
        self.currentState = self.states[id]
    
    def request(self):
        self.currentState.handle(self)


class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class ConcreteState1(State):
    def handle(self, context):
        print("ConcreteState1 handle")
        context.changeState(2)


class ConcreteState2(State):
    def handle(self, context):
        print("ConcreteState2 handle")
        context.changeState(1)



state1 = ConcreteState1()
context = Context(state1)
context.request()
context.request()