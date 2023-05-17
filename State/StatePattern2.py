from abc import ABC, abstractmethod
import math

class Context:
    def __init__(self, state):
        self.current_state = state

    def change_state(self, state):
        self.current_state = state
    
    def request(self):
        self.current_state.handle(self)


class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class ConcreteState1(State):
    def handle(self, context):
        print("ConcreteState1 handle")
        context.change_state(ConcreteState2())


class ConcreteState2(State):
    def handle(self, context):
        print("ConcreteState2 handle")
        context.change_state(ConcreteState1())

# Client code.
state1 = ConcreteState1()
context = Context(state1)
context.request()
context.request()

"""
ConcreteState1 handle
ConcreteState2 handle
"""