from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_elementA(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_elementB(self)

class Visitor(ABC):
    @abstractmethod
    def visit_elementA(self, elementA):
        pass

    @abstractmethod
    def visit_elementB(self, elementB):
        pass

class ConcreteVisitor1(Visitor):
    def visit_elementA(self, elementA):
        print("ConcreteVisitor1", "visit_elementA")

    def visit_elementB(self, elementB):
        print("ConcreteVisitor1", "visit_elementB")

class ConcreteVisitor2(Visitor):
    def visit_elementA(self, elementA):
        print("ConcreteVisitor2", "visit_elementA")

    def visit_elementB(self, elementB):
        print("ConcreteVisitor2", "visit_elementB")


# Client Code.
visitor1 = ConcreteVisitor1()
elementA = ConcreteElementA()
elementA.accept(visitor1)

elementA = ConcreteElementB()
elementA.accept(visitor1)

"""
ConcreteVisitor1 visit_elementA
ConcreteVisitor1 visit_elementB
"""
