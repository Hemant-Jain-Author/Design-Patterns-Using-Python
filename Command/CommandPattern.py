from abc import ABC, abstractmethod

class Invoker:  # Remote
    def __init__(self):
        self._commands = []

    def set_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
    
    def unexecute_commands(self):
        for command in self._commands:
            command.unexecute()
        

class Command(ABC): 
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def unexecute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action("Action 1")

    def unexecute(self):
        self._receiver.action("Action 2")


class Receiver: 
    def action(self, action):
        print(action)


#Client Code.
receiver = Receiver()
concrete_command = ConcreteCommand(receiver)
invoker = Invoker()
invoker.set_command(concrete_command)
invoker.execute_commands()
invoker.unexecute_commands()


"""
Action 1
Action 2
"""