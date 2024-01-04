from abc import ABC, abstractmethod

class ATMHandlerAbstract(ABC):
    def __init__(self, successor, denomination):
        self._successor = successor
        self._denomination = denomination

    @abstractmethod
    def handle_request(self, amount):
        pass

class ATMHandler(ATMHandlerAbstract):
    def handle_request(self, amount):
        q = int(amount // self._denomination)
        r = amount % self._denomination
        if q != 0:
            print("%s notes of %s"%(q,self._denomination))

        if r != 0 and self._successor is not None:
            self._successor.handle_request(r)


# Client Code
ch = ATMHandler(ATMHandler(ATMHandler(ATMHandler(None, 10), 50), 100), 1000)
ch.handle_request(5560)

"""
5 notes of 1000
5 notes of 100
1 notes of 50
1 notes of 10
"""
