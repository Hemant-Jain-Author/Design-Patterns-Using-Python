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
    def get_menu(self):
        pass
    
    @abstractmethod
    def get_button(self):
        pass
    

class WinFactory(GenFactory):
    def get_menu(self):
        return WinMenu()
    
    def get_button(self):
        return WinButton()

class MacFactory(GenFactory):
    def get_menu(self):
        return MacMenu()
    
    def get_button(self):
        return MacButton()


# Client code.
m = MacFactory()
m.get_menu().desc()
m.get_button().desc()

w = WinFactory()
w.get_button().desc()
w.get_menu().desc()

"""
Mac Menu!!
Mac Button!!
Win Button!!
Win Menu!!
"""