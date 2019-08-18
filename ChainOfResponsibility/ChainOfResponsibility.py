from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handleRequest(self):
        pass

class ConcreteHandler1(Handler):
    def handleRequest(self):
        if True:  # Can handle request.
            print("Finally handled by ConcreteHandler1")
        elif self._successor is not None:
            print("Message passed to next in chain by ConcreteHandler1")
            self._successor.handleRequest()

class ConcreteHandler2(Handler):
    def handleRequest(self):
        if False:  # Can't handle request.
            print("Finally handled by ConcreteHandler2")
        elif self._successor is not None:
            print("Message passed to next in chain by ConcreteHandler2")
            self._successor.handleRequest()

ch1 = ConcreteHandler1()
ch2 = ConcreteHandler2(ch1)
ch2.handleRequest()

