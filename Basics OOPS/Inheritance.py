class Person(object):
    def __init__(self, name, age, gender): #constructor
        self.name = name #data members / attributes
        self.age = age
        self.__gender = gender
    
    def toString(self): # member function
        return "Person: %s:%s" % (self.name, self.age)

    def getGender(self):
        return self.__gender


class Citizen(Person):
    def __init__(self, name, age, id, gender): #constructor
        self.name = name
        self.age = age
        self.id = id
        self.__gender = gender

    def voterId(self):
        return self.id
    
    def toString(self):
        return "Citizen: %s:%s:%s:%s" % (self.name, self.age, self.__gender, self.id)



p = Person("John", 32) # p is an object of type Person
r = p.toString()
print("Type of Object:", type(p), r, p.age, p.getGender(), "Memory Address:", id(p))

c = Citizen("Smith", 31, 1234, "M")
print(c, c.toString(), c.voterId())
