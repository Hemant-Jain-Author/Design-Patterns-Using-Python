import unittest

class Rectangle():
    def __init__(self, l, w):
        self.height = l
        self.width = w

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

class Square(Rectangle):
    def __init__(self, l):
        self.height = l
        self.width = l

    def set_width(self, w):
        self.width = self.height = w

    def set_height(self, h):
        self.width = self.height = h

def testRect(rect):
    rect.set_height(10)
    rect.set_width(20)
    if 10*20 == rect.get_height()*rect.get_width():
        print("Test success")
    else:
        print("Test failed")

# Client code.
r = Rectangle(10, 20)
testRect(r)

s = Square(10)
s.set_width(20)
testRect(s)

"""
Test success
Test failed
"""