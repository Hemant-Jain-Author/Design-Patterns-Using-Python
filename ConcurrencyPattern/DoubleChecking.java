import threading
import sys

class Database(object):
    def __init__(self):
        print("database created")
    
    def add_data(self, data):
        print(data)

class Singleton(object):
    _instance = None  # Keep instance reference 
    db = None
    _lock = threading.Lock()  # Add a lock for thread synchronization
    
    def __new__(cls):
        if not cls._instance:
            with cls._lock:  # Acquire the lock
                if not cls._instance:
                    cls._instance = super(Singleton, cls).__new__(cls)
                    cls.db = Database()
        return cls._instance
    
    def add_data(self, data):
        self.db.add_data(data)

# Client code. 
s1 = Singleton() 
s2 = Singleton()
print(s1)
print(s2)
s2.add_data("Hello, world!")

"""
database created
<__main__.Singleton object at 0x000002260C56BCD0>
<__main__.Singleton object at 0x000002260C56BCD0>
Hello, world!
"""
