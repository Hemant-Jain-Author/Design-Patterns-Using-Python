from abc import ABC, abstractmethod

class IChatRoom(ABC):
    @abstractmethod
    def addParticipant(self, participant):
        pass

    @abstractmethod
    def broadcast(self, message, origin):
        pass

    @abstractmethod
    def sendMessage(self, message, to):
        pass
    

        
class ChatRoom(IChatRoom):
    def __init__(self):
        self.participants = {}
 
    def addParticipant(self, participant):
        self.participants[participant.name] = participant

    def broadcast(self, message, origin):
        print("ChatRoom broadcast Message : " + message)
        for p in self.participants:
            if p != origin:
                self.participants[p].receive(message)
 
    def sendMessage(self, message, to):
        self.participants[to].receive(message)


class Participant(object):
    def __init__(self, name, chatRoom):
        self.name = name
        self.chatRoom = chatRoom 
        self.chatRoom.addParticipant(self)
    
    def broadcast(self, message):
        print(self.name + " broadcast Message : " + message)
        self.chatRoom.broadcast(message, self.name)

    def send(self, message, to):
        print(self.name + " sent Message : " + message)
        self.chatRoom.sendMessage(message, to)
 
    def receive(self, message):
        print(self.name + " received Message : " + message)

chatRoom = ChatRoom()
James = Participant("James", chatRoom)
Michael = Participant("Michael", chatRoom)
Robert = Participant("Robert", chatRoom)

Michael.send("Good Morning.", "James")
print()
James.broadcast("Hello, World!")
