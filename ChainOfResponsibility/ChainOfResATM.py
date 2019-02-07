from abc import ABC, abstractmethod

class ATMHandlerAbstract(ABC):
    def __init__(self, successor, denomination):
        self._successor = successor
        self._denomination = denomination

    @abstractmethod
    def handleRequest(self, amount):
        pass

class ATMHandler(ATMHandlerAbstract):
    def handleRequest(self, amount):
        q = int(amount // self._denomination)
        r = amount % self._denomination
        if q != 0:
            print("%s notes of %s"%(q,self._denomination))

        if r != 0 and self._successor is not None:
            self._successor.handleRequest(r)

ch = ATMHandler(ATMHandler(ATMHandler(ATMHandler(None, 10), 50), 100), 1000)
ch.handleRequest(5560)