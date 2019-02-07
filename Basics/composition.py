class Teacher(object):
    def __init__(self, name): #constructor
        self.name = name #data members/ attributes
    
    def getName(self): # member function
        return self.name


class Class(object):
    def __init__(self, cname, tname): #constructor
        self.className = cname
        self.teacher = Teacher(tname)

    def display(self):
        print("Class: %s, Tracher: %s" % (self.className, self.teacher.getName())) 

c = Class("C1", "John")
c.display()