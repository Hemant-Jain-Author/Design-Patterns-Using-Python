from abc import ABC, abstractmethod

class Invoker:  # Remote
    def __init__(self):
        self._commands = []

    def setCommand(self, command):
        self._commands.append(command)

    def executeCommands(self):
        for command in self._commands:
            command.execute()
    
    def unexecuteCommands(self):
        for command in self._commands:
            command.unexecute()
        

class ICommand(ABC): 
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def unexecute(self):
        pass


class ConcreteCommand(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action("Action 1")

    def unexecute(self):
        self._receiver.action("Action 2")


class Receiver: 
    def action(self, action):
        print(action)


receiver = Receiver()
concrete_command = ConcreteCommand(receiver)
invoker = Invoker()
invoker.setCommand(concrete_command)
invoker.executeCommands()
invoker.unexecuteCommands()