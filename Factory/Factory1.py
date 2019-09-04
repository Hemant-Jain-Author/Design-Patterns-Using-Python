from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def operation(self):
        pass

class SubClass1(BaseClass):
    def operation(self):
        print("SubClass1 Operation!")

class SubClass2(BaseClass):
    def operation(self):
        print("SubClass2 Operation!")

## factory defined
class Factory(object):
    def getObject(self, object_type):
        return eval(object_type)()

f = Factory()
a = f.getObject("SubClass1")
a.operation()

a = f.getObject("SubClass2")
a.operation()
