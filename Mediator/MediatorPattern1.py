from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def add_colleague(self, Colleague):
        pass

    @abstractmethod
    def send_message(self, message, ColleagueId):
        pass
    
        
class ConcreteMediator(Mediator):
    def __init__(self):
        self.Colleagues = {}
  
    def add_colleague(self, Colleague):
        self.Colleagues[Colleague.id] = Colleague

    def send_message(self, message, ColleagueId):
        print("Mediator pass Message : " + message)
        self.Colleagues[ColleagueId].receive(message)


class Colleague(ABC):
    @abstractmethod
    def __init__(self, mediator):
        pass 
    
    @abstractmethod
    def send(self, message, to):
        pass
 
    @abstractmethod
    def receive(self, message):
        pass


class ConcreteColleague1(object):
    def __init__(self, mediator):
        self.id = "First"
        self.mediator = mediator 
    
    def send(self, message, to):
        print(self.id + " Sent Message : " + message)
        self.mediator.send_message(message, to)
 
    def receive(self, message):
        print(self.id + " Received Message " + message)


class ConcreteColleague2(object):
    def __init__(self, mediator):
        self.id = "Second"
        self.mediator = mediator 
    
    def send(self, message, to):
        print(self.id + " Sent Message : " + message)
        self.mediator.send_message(message, to)
 
    def receive(self, message):
        print(self.id + " Received Message " + message)

# Client code.
mediator = ConcreteMediator()
first = ConcreteColleague1(mediator)
mediator.add_colleague(first)
second = ConcreteColleague2(mediator)
mediator.add_colleague(second)
first.send("Hello, World!", "Second")

"""
First Sent Message : Hello, World!
Mediator pass Message : Hello, World!
Second Received Message Hello, World!
"""