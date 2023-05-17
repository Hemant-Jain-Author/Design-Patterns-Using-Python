from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self):
        pass

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == 'request1':
            print('ConcreteHandler1 handles the request1.')
        elif self._successor:
            self._successor.handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == 'request2':
            print('ConcreteHandler2 handles the request2.')
        elif self._successor:
            self._successor.handle_request(request)

class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == 'request3':
            print('ConcreteHandler3 handles the request3.')
        elif self._successor:
            self._successor.handle_request(request)

# Client Code
ch1 = ConcreteHandler1()
ch2 = ConcreteHandler2(ch1)
ch3 = ConcreteHandler3(ch2)

ch3.handle_request('request1')
ch3.handle_request('request2')
ch3.handle_request('request3')
ch3.handle_request('request4')

"""
ConcreteHandler1 handles the request1.
ConcreteHandler2 handles the request2.
ConcreteHandler3 handles the request3.
"""