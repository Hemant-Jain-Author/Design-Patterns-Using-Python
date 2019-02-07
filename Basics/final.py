class Person(object):
    def __init__(self, name, age): #constructor
        self.name = name #data member
    
    def toString(self): # member function
        return "Person: %s:%s" % (self.name, self.oath)

    def setOath(self):
        self.oath = "Always tell truth"


class Citizen(Person):
    def __init__(self, name, id): #constructor
        self.name = name
        self.id = id

    def setOath(self):
        self.oath = "Country comes first"
    
p = Person("John", 32) # p is an object of type Person
p.setOath()
print(p.toString())

c = Citizen("Smith", 31)
c.setOath()
print(c.toString())
