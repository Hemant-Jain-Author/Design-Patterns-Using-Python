from abc import ABC, abstractmethod

class AddDataTemplate(ABC):
    
    def add_data(self): # Final
        self.open()
        self.add()
        self.close()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def close(self):
        pass


class AddDataToFile(AddDataTemplate):
    def open(self):
        print("Open file.")

    def add(self):
        print("Add data to file.")
    
    def close(self):
        print("Close file")
        
class AddDataToDB(AddDataTemplate):
    def open(self):
        print("Open Database.")

    def add(self):
        print("Add data to Database.")
    
    def close(self):
        print("Close Database.")  

# Client Code 
o = AddDataToDB()
o.add_data()

"""
Open Database.
Add data to Database.
Close Database.
"""



