from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class ConcreteStrategy1(Strategy):
    def execute(self, data):
        print("ConcreteStrategy1 execute")        


class ConcreteStrategy2(Strategy):
    def execute(self, data):
        print("ConcreteStrategy2 execute")


class Context:
    def __init__(self, strategy = ConcreteStrategy1()):
        self.strategy = strategy

    def setStrategy(self, strategy):
        self.strategy = strategy
    
    def execute(self):
        data = 1 
        self.strategy.execute(data)

        
#Client code.
c = Context()
c.execute()

c.setStrategy(ConcreteStrategy2())
c.execute()