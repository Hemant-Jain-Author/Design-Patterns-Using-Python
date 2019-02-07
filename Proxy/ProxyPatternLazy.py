
from abc import ABC, abstractmethod

class BookParser(ABC):
    @abstractmethod
    def __init__(self, book):
        pass
        
    @abstractmethod
    def numPages(self, book):
        pass


class ConcreteBookParser(BookParser):
    def __init__(self, book):
        print("Concrete Subject Request Method")
        # Number of pages calculation heavy operation.
        self._numPages = 1000

    def numPages(self):
        print("Concrete Subject Request Method")
        return self._numPages


class LazyBookParserProxy(BookParser):
    def __init__(self, book):
        self._book = book
        self._concSub = None

    def numPages(self):
        if self._concSub == None:
            self._concSub = ConcreteBookParser(self._book)
        return self._concSub.numPages()

# Client code
proxy = LazyBookParserProxy("LOTR")
print(proxy.numPages())