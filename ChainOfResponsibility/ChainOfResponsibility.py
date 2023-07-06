from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handleRequest(self):
        pass

class ConcreteHandler1(Handler):
    def handleRequest(self, request):
        if request == 'request1':
            print('ConcreteHandler1 handles the request.')
        elif self._successor:
            self._successor.handleRequest(request)

class ConcreteHandler2(Handler):
    def handleRequest(self, request):
        if request == 'request2':
            print('ConcreteHandler2 handles the request.')
        elif self._successor:
            self._successor.handleRequest(request)

class ConcreteHandler3(Handler):
    def handleRequest(self, request):
        if request == 'request3':
            print('ConcreteHandler3 handles the request.')
        elif self._successor:
            self._successor.handleRequest(request)


# Client Code
ch1 = ConcreteHandler1()
ch2 = ConcreteHandler2(ch1)
ch3 = ConcreteHandler3(ch2)

ch3.handleRequest('request1')
ch3.handleRequest('request2')
ch3.handleRequest('request3')
ch3.handleRequest('request4')

"""
Output:
ConcreteHandler1 handles the request.
ConcreteHandler2 handles the request.
ConcreteHandler3 handles the request.

"""
