class Tyre(object):
    def __init__(self, type):   #constructor
        self.type= type         #data members / attributes
    
    def get_type(self):          # member function
        return self.type


class Car(object):
    def __init__(self, model): #constructor
        self.model = model
        self.tyres = []
        for i in range(4):
            self.tyres.append(Tyre("MRF"))

    def display(self):
        print("Car: %s, Tyre : %s" % (self.model, self.tyres[0].get_type())) 

# Client code
c = Car("BMW")
c.display()
