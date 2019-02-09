from abc import ABC, abstractmethod

class IChatRoom(ABC):
    @abstractmethod
    def sendMessage(self, message, participant):
        pass
    
    @abstractmethod
    def addParticipant(self, participant):
        pass
        
class ChatRoom(IChatRoom):
    def __init__(self):
        self.participants = {}
 
    def sendMessage(self, message, participant):
        for p in self.participants:
            if p != participant:
                self.participants[p].receive(message)
 
    def sendToMessage(self, message, to):
        self.participants[to].receive(message)

    def addParticipant(self, participant):
        self.participants[participant.name] = participant

class Participant(object):
    def __init__(self, name, chatRoom):
        self.name = name
        self.chatRoom = chatRoom 
        self.chatRoom.addParticipant(self)
    
    def send(self, message):
        print(self.name + " Send Message : " + message)
        self.chatRoom.sendMessage(message, self.name)

    def sendTo(self, message, to):
        print(self.name + " Send Message : " + message)
        self.chatRoom.sendToMessage(message, to)
 
    def receive(self, message):
        print(self.name + " Received Message " + message)

chatRoom = ChatRoom()
James = Participant("James", chatRoom)
Michael = Participant("Michael", chatRoom)
Robert = Participant("Robert", chatRoom)
 
James.send("Hello, World!")
Michael.sendTo("Good Morning.", "James")