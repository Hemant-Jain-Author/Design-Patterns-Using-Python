from abc import ABC, abstractmethod

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# Terminal Expression
class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self):
        return self.number

# Non-terminal Expression
class AddExpression(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self):
        return self.left_expression.interpret() + self.right_expression.interpret()

# Context
class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def get_variable(self, variable):
        return self.variables.get(variable, 0)

# Client code
context = Context()
context.set_variable("x", 10)
context.set_variable("y", 5)

# Create the expression tree: x + (y + 2)
expression = AddExpression(
                NumberExpression(context.get_variable("x")),
                AddExpression(
                    NumberExpression(context.get_variable("y")),
                    NumberExpression(2)
                )
            )

result = expression.interpret()
print(f"Result: {result}")  # Output: Result: 17
