import sys

class Database(object):
    def __init__(self):
        print("database created")
    
    def addData(self, data):
        print(data)

class Singleton(object):
    _instance = None  # Keep instance reference 
    db = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls) # super(Singleton, cls)
            cls.db = Database()
            print("constructor")
        return cls._instance
    
    def addData(self, data):
        self.db.addData(data)
    

s1 = Singleton() 
s2 = Singleton()
s1 = Singleton() 
s2 = Singleton()
s1 = Singleton() 
s2 = Singleton()
print(s1, s2)
s2.addData("Hello, world!")


