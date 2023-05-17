from abc import ABC, abstractmethod

class DesiredInterface(ABC):
    @abstractmethod
    def operation(self):
        pass

class Adapter(DesiredInterface):
    def __init__(self):
        self._adaptee = Adaptee()
        
    def operation(self):
        self._adaptee.some_operation()

class Adaptee:
    def some_operation(self):
        print("Adaptee some_request() function called.")


# Client Code
adapter = Adapter()
adapter.operation()

"""
Adaptee some_request() function called.
"""
