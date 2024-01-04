import sqlite3
import sys

class Database(object):
    _instance = None  # Keep instance reference 

    def __new__(self):
        if not self._instance:
            self._instance = object.__new__(self)
            print("Database created")
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self._instance
    
    def createTable(self):
        self.cursorobj.execute("CREATE TABLE IF NOT EXISTS students ( id integer ,name text);")

    def addData(self, id, name):
        query = "INSERT INTO students (id, name) VALUES (?, ?);"
        self.cursorobj.execute(query, (id, name))

    def display(self):
        self.cursorobj.execute("SELECT * FROM students;")
        rows = self.cursorobj.fetchall()
        for row in rows:
            print(row)

    
db1 = Database()
db2 = Database()
print ("Database Objects DB1", db1)
print ("Database Objects DB2", db2)
db1.createTable()
db1.addData(1, "john")
db2.addData(2, "smith")
db1.display()

"""
"""
