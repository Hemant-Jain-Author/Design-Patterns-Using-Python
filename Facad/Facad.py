class SystemManagerFacade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        self._subsystem1.operation1()
        self._subsystem1.operation2()
        self._subsystem2.operation1()
        self._subsystem2.operation2()

class Subsystem1:
    def operation1(self):
        print("Subsystem1 operation1")

    def operation2(self):
        print("Subsystem1 operation2")


class Subsystem2:
    def operation1(self):
        print("Subsystem2 operation1")

    def operation2(self):
        print("Subsystem2 operation2")


facade = SystemManagerFacade()
facade.operation()

"""
Output:
Subsystem1 operation1
Subsystem1 operation2
Subsystem2 operation1
Subsystem2 operation2

"""
