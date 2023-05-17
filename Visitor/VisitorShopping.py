from abc import ABC, abstractmethod

class Element(ABC):  
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Element):
    def __init__(self, price, isbn):
        self.price = price
        self.isbn = isbn
        
    def accept(self, visitor):
        return visitor.visit_book(self)

class Fruit(Element):
    def __init__(self, price, quantity, type):
        self.price = price
        self.quantity = quantity
        self.type = type

    def accept(self, visitor):
        return visitor.visit_fruit(self) * self.quantity

class Visitor(ABC):
    def visit_book(self, element):
        pass

    def visit_fruit(self, element):
        pass

class SundayDiscount(Visitor):
    def visit_book(self, element):
        return element.price - 50

    def visit_fruit(self, element):
        return element.price - 5

class SaleDiscount(Visitor):
    def visit_book(self, element):
        return (element.price / 2)

    def visit_fruit(self, element):
        return (element.price / 2)
        
class ShoppingCart:
    def __init__(self):
        self.list = []

    def add(self, o):
        self.list.append(o)

    def setDiscountVisitor(self, discount):
        self.visitor = discount

    def accept(self):
        cost = 0
        for o in self.list:
            cost += o.accept(self.visitor)
        print("total cost : ", cost)
    
    
# Client Code
os = ShoppingCart()
os.add(Fruit(100,10,"Apple"))
os.add(Book(100,12345))
os.setDiscountVisitor(SundayDiscount())
os.accept()

os.setDiscountVisitor(SaleDiscount())
os.accept()

"""
Output:
total cost :  1000
total cost :  550.0
"""
