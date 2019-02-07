class adder :
    def __init__(self):
        self.__sum = 0   # private variable
    
    def increment(self, a):
        self.__sum += a   

    def increment(self):
        self.__sum += 1

    def getValue(self):
        return self.__sum


a = adder()
a.increment(10)
a.increment()
print(a.getValue())
