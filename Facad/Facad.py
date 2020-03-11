class SystemManagerFacade:
    def __init__(self):
        self._subsystem1 = ComplexSubsystem1()
        self._subsystem2 = ComplexSubsystem2()

    def operation(self):
        self._subsystem1.operation1()
        self._subsystem1.operation2()
        self._subsystem2.operation1()
        self._subsystem2.operation2()

class ComplexSubsystem1:
    def operation1(self):
        print("ComplexSubsystem1 operation1")

    def operation2(self):
        print("ComplexSubsystem1 operation2")


class ComplexSubsystem2:
    def operation1(self):
        print("ComplexSubsystem2 operation1")

    def operation2(self):
        print("ComplexSubsystem2 operation2")


facade = SystemManagerFacade()
facade.operation()

"""
Output:
ComplexSubsystem1 operation1
ComplexSubsystem1 operation2
ComplexSubsystem2 operation1
ComplexSubsystem2 operation2

"""
