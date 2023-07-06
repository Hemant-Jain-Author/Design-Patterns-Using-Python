
from abc import ABC, abstractmethod

class BookParser(ABC):
    @abstractmethod
    def __init__(self, book):
        pass
        
    @abstractmethod
    def num_pages(self, book):
        pass


class ConcreteBookParser(BookParser):
    def __init__(self, book):
        print("Concrete Subject Request Method")
        # Number of pages calculation heavy operation.
        # Suppose this calculation come to 1000 pages.
        self._num_pages = 1000

    def num_pages(self):
        print("Concrete Subject Request Method")
        return self._num_pages


class LazyBookParserProxy(BookParser):
    def __init__(self, book):
        self._book = book
        self._subject = None

    def num_pages(self):
        if self._subject == None:
            self._subject = ConcreteBookParser(self._book)
        return self._subject.num_pages()

# Client code
proxy = LazyBookParserProxy("LOTR")
print(proxy.num_pages())
