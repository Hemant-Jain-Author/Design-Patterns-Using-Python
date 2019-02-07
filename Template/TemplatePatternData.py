from abc import ABC, abstractmethod

class AddDataTemplate(ABC):
    
    def addData(self): # Final
        self._open()
        self._add()
        self._close()

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _add(self):
        pass
    
    @abstractmethod
    def _close(self):
        pass


class AddDataToFile(AddDataTemplate):
    def _open(self):
        print("Open file.")

    def _add(self):
        print("Add data to file.")
    
    def _close(self):
        print("Close file")
        
class AddDataToDB(AddDataTemplate):
    def _open(self):
        print("Open Database.")

    def _add(self):
        print("Add data to Database.")
    
    def _close(self):
        print("Close Database")  

o = AddDataToDB()
o.addData()

