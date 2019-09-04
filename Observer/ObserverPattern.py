from abc import ABC, abstractmethod

class Subject:
    def __init__(self):
        self.__observers = []
        self.__state = None

    def attach(self, observer):
        observer._subject = self
        self.__observers.append(observer)

    def detach(self, observer):
        observer._subject = None
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update()

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
    def __init__(self, subect):
        super().__init__(subject)

    def update(self):
        print(self._subject.getState() + " notified to Observer1")

class ConcreteObserver2(Observer):
    def __init__(self, subject):
        super().__init__(subject)

    def update(self):
        print(self._subject.getState() + " notified to Observer2")


# Client Code.
subject = Subject()
observer1 = ConcreteObserver1(subject)
observer2 = ConcreteObserver2(subject)
subject.setState("First state")
subject.setState("Second state")
