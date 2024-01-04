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
        self._concSub = RealSubject()

    def request(self):
        self._concSub.request()


# Client code
proxy = Proxy()
proxy.request()

"""
Concrete Subject Request Method
"""