class Person(object):
    def __init__(self, name, age, gender): #constructor
        self.name = name #data members / attributes
        self.age = age
        self.gender = gender
    
    def __str__(self): # member function
        return "Person: %s is a %s and %s years old." % (self.name, self.gender, self.age)

    def get_gender(self):
        return self.gender


class Citizen(Person):
    def __init__(self, name, age, id, gender): #constructor
        super().__init__(name, age, gender)
        self.id = id

    def voter_Id(self):
        return self.id
    
    def __str__(self):
        return "Citizen: %s is a %s and %s years old with voter id %s." % (self.name, self.gender, self.age, self.id)


#Client code
p = Person("John", 32, "Male")
print(p)
c = Citizen("Smith", 31, 1234, "Male")
print(c)

"""
Person: John is a Male and 32 years old.
Citizen: Smith is a Male and 31 years old with voter id 1234.
"""