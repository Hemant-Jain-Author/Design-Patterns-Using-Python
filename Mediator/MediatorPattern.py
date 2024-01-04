from abc import ABC, abstractmethod

class IChatRoom(ABC):
    @abstractmethod
    def add_participant(self, participant):
        pass

    @abstractmethod
    def broadcast(self, message, origin):
        pass

    @abstractmethod
    def send_message(self, message, to):
        pass  
        
class ChatRoom(IChatRoom):
    def __init__(self):
        self.participants = {}
 
    def add_participant(self, participant):
        self.participants[participant.name] = participant

    def broadcast(self, message, origin):
        print("ChatRoom broadcast Message : " + message)
        for p in self.participants:
            if p != origin:
                self.participants[p].receive(message)
 
    def send_message(self, message, to):
        self.participants[to].receive(message)


class IParticipant(object):
    def __init__(self, name, chatRoom):
        pass
    
    def broadcast(self, message):
        pass

    def send(self, message, to):
        pass
 
    def receive(self, message):
        pass

class Participant(IParticipant):
    def __init__(self, name, chatRoom):
        self.name = name
        self.chatRoom = chatRoom 
        self.chatRoom.add_participant(self)
    
    def broadcast(self, message):
        print(self.name + " broadcast Message : " + message)
        self.chatRoom.broadcast(message, self.name)

    def send(self, message, to):
        print(self.name + " sent Message : " + message)
        self.chatRoom.send_message(message, to)
 
    def receive(self, message):
        print(self.name + " received Message : " + message)

# Client code.
chatRoom = ChatRoom()
James = Participant("James", chatRoom)
Michael = Participant("Michael", chatRoom)
Robert = Participant("Robert", chatRoom)
Michael.send("Good Morning.", "James")
James.broadcast("Hello, World!")

"""
Michael sent Message : Good Morning.
James received Message : Good Morning.
James broadcast Message : Hello, World!
ChatRoom broadcast Message : Hello, World!
Michael received Message : Hello, World!
Robert received Message : Hello, World!
"""