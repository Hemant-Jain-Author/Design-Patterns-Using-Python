from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visitElementA(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visitElementB(self)

class Visitor(ABC):
    @abstractmethod
    def visitElementA(self, elementA):
        pass

    @abstractmethod
    def visitElementB(self, elementB):
        pass

class ConcreteVisitor1(Visitor):
    def visitElementA(self, elementA):
        print("ConcreteVisitor1", "visitElementA")

    def visitElementB(self, elementB):
        print("ConcreteVisitor1", "visitElementB")

class ConcreteVisitor2(Visitor):
    def visitElementA(self, elementA):
        print("ConcreteVisitor2", "visitElementA")

    def visitElementB(self, elementB):
        print("ConcreteVisitor2", "visitElementB")

visitor1 = ConcreteVisitor1()
elementA = ConcreteElementA()
elementA.accept(visitor1)