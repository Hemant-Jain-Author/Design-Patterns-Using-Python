from abc import ABC, abstractmethod
import datetime
import math

class Context:
    def __init__(self, state):
        self.current_state = state
        
    def change_state(self, state):
        self.current_state = state
    
    def request(self):
        #print(self.current_state)
        self.current_state.handle(self)


class State(object):
    def handle(self, context):
        pass


class ConcreteState1(State):
    _instance = None  # Keep instance reference 
    @staticmethod
    def instance(): # Singleton pattern
        if not ConcreteState1._instance:  
            ConcreteState1._instance = ConcreteState1()
        return ConcreteState1._instance


    def handle(self, context):
        context.change_state(ConcreteState2.instance())


class ConcreteState2(State):
    _instance = None  # Keep instance reference 
    @staticmethod
    def instance(): # Singleton pattern
        if not ConcreteState2._instance:  
            ConcreteState2._instance = ConcreteState2()
        return ConcreteState2._instance


    def handle(self, context):
        context.change_state(ConcreteState3.instance())


class ConcreteState3(State):
    _instance = None  # Keep instance reference 
    @staticmethod
    def instance(): # Singleton pattern
        if not ConcreteState3._instance:  
            ConcreteState3._instance = ConcreteState3()
        return ConcreteState3._instance


    def handle(self, context):

        context.change_state(ConcreteState4.instance())


class ConcreteState4(State):
    _instance = None  # Keep instance reference 
    @staticmethod
    def instance(): # Singleton pattern
        if not ConcreteState4._instance:  
            ConcreteState4._instance = ConcreteState4()
        return ConcreteState4._instance


    def handle(self, context):
        context.change_state(ConcreteState1.instance())

class St(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class ConcreteSt1(St):
    def handle(self, context):
        context.change_state(ConcreteSt2())


class ConcreteSt2(St):
    def handle(self, context):
        context.change_state(ConcreteSt3())


class ConcreteSt3(St):
    def handle(self, context):
        context.change_state(ConcreteSt4())


class ConcreteSt4(St):
    def handle(self, context):
        context.change_state(ConcreteSt1())


def test(state, count):
    context = Context(state)
    a = datetime.datetime.now()
    for i in range(count):
        context.request()
    b = datetime.datetime.now()
    delta = b - a
    print(delta.total_seconds())

state1 = ConcreteSt1()
test(state1, 10)

#using singleton.
state1 = ConcreteState1.instance()
test(state1, 10)

"""
Singleton pattern is used to ristrict the numbrer of object creation. 
Same way system is automatically reusing the memory. Since ideally the statepattern
states does not have its internal state or internal variables so the state object 
which is just freed is resued by the system to create new object. 
"""