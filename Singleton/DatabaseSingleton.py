import sqlite3
import sys

class Database(object):
    _instance = None  # Keep instance reference 
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("database created")
            cls.connection = sqlite3.connect("db.sqlite3")
            cls.cursorobj = cls.connection.cursor()
        return cls._instance      
    
    def create_table(self):
        self.cursorobj.execute("CREATE TABLE IF NOT EXISTS students ( id integer ,name text);")

    def add_data(self, id, name):
        query = "INSERT INTO students (id, name) VALUES (%s, \'%s\');" % (id, name)
        self.cursorobj.execute(query)

    def display(self):
        self.cursorobj.execute("SELECT * FROM students;")
        rows = self.cursorobj.fetchall()
        for row in rows:
            print(row)

# Client code. 
db1 = Database()
db2 = Database()
print ("Database Objects DB1", db1)
print ("Database Objects DB2", db2)
db1.create_table()
db1.add_data(1, "john")
db2.add_data(2, "smith")
db1.display()