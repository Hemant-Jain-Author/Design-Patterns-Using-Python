
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
        self._subject = None

    def request(self):
        if self._subject == None :
            self._subject = RealSubject() # Lazy Init
        self._subject.request()

# Client code
proxy = Proxy()
proxy.request()