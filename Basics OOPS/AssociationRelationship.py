class Student(object):
    def __init__(self, name): #constructor
        self.name = name #data members / attributes
    
    def toString(self): # member function
        return "Student: %s" % (self.name)


class Class(object):
    def __init__(self, cname): #constructor
        self.className = cname
        self.students = []

    def addStudent(self, st):
        self.students.append(st)

    def display(self):
        for i in self.students:
            print(i.toString())


c = Class("SS1")
s1 = Student("John Smith")
s2 = Student("Jane Smith")
c.addStudent(s1)
c.addStudent(s2)
c.display()

