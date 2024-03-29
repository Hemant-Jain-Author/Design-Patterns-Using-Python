from abc import ABC, abstractmethod

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class NonterminalExpression(AbstractExpression):
    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print("NonTerminalExpression:interpret")
        self._expression.interpret()


class TerminalExpression(AbstractExpression):
    def interpret(self):
        print("TerminalExpression:interpret")

#Client Code.
tree = NonterminalExpression(TerminalExpression())
tree.interpret()
