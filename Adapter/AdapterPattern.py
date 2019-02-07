from abc import ABC, abstractmethod

class DesiredInterface(ABC):
    @abstractmethod
    def request(self):
        pass

class Adapter(DesiredInterface):
    def __init__(self):
        self._adaptee = Adaptee()
        
    def request(self):
        self._adaptee.some_request()

class Adaptee:
    def some_request(self):
        print("Adaptee some_request() function called.")


adapter = Adapter()
adapter.request()