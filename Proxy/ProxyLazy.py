
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("Concrete Subject Request Method")

class Proxy(Subject):
    def __init__(self):
        self._concSub = None

    def request(self):
        if self._concSub == None :
            self._concSub = RealSubject() # Lazy Init
        self._concSub.request()

# Client code
proxy = Proxy()
proxy.request()