class Student(object):
    def __init__(self, name): #constructor
        self.name = name #data members / attributes
    
    def __str__(self): # member function
        return "Student: %s" % (self.name)


class Class(object):
    def __init__(self, cname): #constructor
        self.className = cname
        self.students = []

    def add_student(self, st):
        self.students.append(st)

    def display(self):
        for i in self.students:
            print(i)

# Client coode
c = Class("SS1")
s1 = Student("John Smith")
s2 = Student("Jane Smith")
c.add_student(s1)
c.add_student(s2)
c.display()

