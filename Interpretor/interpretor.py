from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value
    
    def interpret(self):
        return self.value

class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Minus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Context:
    def __init__(self):
        self.variables = {}
    
    def get_value(self, name):
        return self.variables.get(name, 0)
    
    def set_value(self, name, value):
        self.variables[name] = value

def parse_expression(expression, context):
    if expression.isdigit():
        return Number(int(expression))
    elif "+" in expression:
        left, right = expression.split(" + ", 1)
        return Plus(parse_expression(left, context), parse_expression(right, context))
    elif "-" in expression:
        left, right = expression.split(" - ", 1)
        return Minus(parse_expression(left, context), parse_expression(right, context))
    else:
        return Number(int(context.get_value(expression)))

# Client code.
context = Context()
context.set_value("x", 10)
context.set_value("y", 5)

expression = parse_expression("x + y + 2", context)
result = expression.interpret()
print(result)
