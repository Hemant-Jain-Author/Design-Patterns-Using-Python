import unittest

class Rectangle():
    def __init__(self, l, w):
        self.height = l
        self.width = w

    def setWidth(self, w):
        self.width = w

    def setHeight(self, h):
        self.height = h

    def getWidth(self):
        return self.width

    def getHeitht(self):
        return self.height

class Square(Rectangle):
    def __init__(self, l):
        self.height = l
        self.width = l

    def setWidth(self, w):
        self.width = self.height = w

    def setHeight(self, h):
        self.width = self.height = h

def testRect(rect):
    rect.setHeight(10)
    rect.setWidth(20)
    assert 10*20 == rect.getHeitht()*rect.getWidth()


r = Rectangle(10, 20)
testRect(r)

s = Square(10)
s.setWidth(20)
#testRect(s)
