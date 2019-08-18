from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def addColleague(self, Colleague):
        pass

    @abstractmethod
    def sendMessage(self, message, ColleagueId):
        pass
    
        
class ConcreteMediator(Mediator):
    def __init__(self):
        self.Colleagues = {}
  
    def addColleague(self, Colleague):
        self.Colleagues[Colleague.id] = Colleague

    def sendMessage(self, message, ColleagueId):
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
        self.mediator.sendMessage(message, to)
 
    def receive(self, message):
        print(self.id + " Received Message " + message)


class ConcreteColleague2(object):
    def __init__(self, mediator):
        self.id = "Second"
        self.mediator = mediator 
    
    def send(self, message, to):
        print(self.id + " Sent Message : " + message)
        self.mediator.sendMessage(message, to)
 
    def receive(self, message):
        print(self.id + " Received Message " + message)


mediator = ConcreteMediator()

first = ConcreteColleague1(mediator)
mediator.addColleague(first)

second = ConcreteColleague2(mediator)
mediator.addColleague(second)

first.send("Hello, World!", "Second")
