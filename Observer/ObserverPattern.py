from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        observer._subject = self
        self.__observers.append(observer)

    def detach(self, observer):
        observer._subject = None
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update()


class ConcreteSubject(Subject):
    def __init__(self):
        self.__state = None
        super().__init__()

    def getState(self):
        return self.__state

    def setState(self, arg):
        self.__state = arg
        self.notify()


class Observer(ABC):
    def __init__(self, sub):
        self._subject = sub
        self._subject.attach(self)

    @abstractmethod
    def update(self):
        pass

class ConcreteObserver1(Observer):
    def __init__(self, subject):
        super().__init__(subject)

    def update(self):
        print(self._subject.getState() + " notified to Observer1")

class ConcreteObserver2(Observer):
    def __init__(self, subject):
        super().__init__(subject)

    def update(self):
        print(self._subject.getState() + " notified to Observer2")


# Client Code.
subject = ConcreteSubject()
observer1 = ConcreteObserver1(subject)
observer2 = ConcreteObserver2(subject)
subject.setState("First state")
subject.setState("Second state")


"""
Output:
First state notified to Observer1
First state notified to Observer2
Second state notified to Observer1
Second state notified to Observer2
"""

