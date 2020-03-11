from abc import ABC, abstractmethod
class Menu(ABC):
    @abstractmethod
    def desc(self):
        pass

class WinMenu(Menu):
    def desc(self):
        print("Win Menu!!")

class MacMenu(Menu):
    def desc(self):
        print("Mac Menu!!")


class Button(ABC):
    @abstractmethod
    def desc(self):
        pass

class WinButton(Button):
    def desc(self):
        print("Win Button!!")

class MacButton(Button):
    def desc(self):
        print("Mac Button!!")


## Factory defined
class GenFactory(ABC):
    @abstractmethod
    def getMenu(self):
        pass
    
    @abstractmethod
    def getButton(self):
        pass
    

class WinFactory(GenFactory):
    def getMenu(self):
        return WinMenu()
    
    def getButton(self):
        return WinButton()

class MacFactory(GenFactory):
    def getMenu(self):
        return MacMenu()
    
    def getButton(self):
        return MacButton()



m = MacFactory()
m.getMenu().desc()
m.getButton().desc()

w = WinFactory()
w.getButton().desc()
w.getMenu().desc()

"""
Output:

Mac Menu!!
Mac Button!!
Win Button!!
Win Menu!!

"""

