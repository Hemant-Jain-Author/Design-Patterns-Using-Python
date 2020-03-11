class Tyre(object):
    def __init__(self, type):   #constructor
        self.type= type         #data members / attributes
    
    def getType(self):          # member function
        return self.type


class Car(object):
    def __init__(self, model): #constructor
        self.model = model
        self.tyres = []
        for i in range(4):
            self.tyres.append(Tyre("MRF Tyre"))

    def display(self):
        print("Car: %s, Tyre : %s" % (self.model, self.tyres[0].getType())) 

c = Car("BMW")
c.display()
