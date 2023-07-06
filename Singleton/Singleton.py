import sys

class Database(object):
    def __init__(self):
        print("Database created")
    
    def addData(self, data):
        print(data)

class Singleton(object):
    _instance = None  # Keep instance reference 

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls) # super(Singleton, cls)
            cls.db = Database()
        return cls._instance
    
    def addData(self, data):
        self.db.addData(data)
    

s1 = Singleton() 
s2 = Singleton()
print(s1)
print(s2)
s2.addData("Hello, world!")


"""
database created
<__main__.Singleton object at 0x7fccf49bec70>
<__main__.Singleton object at 0x7fccf49bec70>
Hello, world!
"""