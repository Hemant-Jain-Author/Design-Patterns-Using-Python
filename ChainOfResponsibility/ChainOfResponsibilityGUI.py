from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, parent=None):
        self._parent = parent
        self._helpText = None

    @abstractmethod
    def showHelpText(self):
        pass

    def setHelperText(self, text):
        self._helpText = text



class Container(Handler):
    def showHelpText(self):
        if self._helpText is not None:  # Can handle request.
            print("Help :: ", self._helpText)
        elif self._parent is not None:
            print("Message passed to next in chain by Container")
            self._parent.showHelpText()



class Button(Handler):
    def __init__(self, label, parent=None ):
        super(Button, self).__init__(parent)
        self._label = label

    def showHelpText(self):
        if self._helpText is not None:  # Can handle request.
            print("Help :: ", self._helpText)
        elif self._parent is not None:
            print("Message passed to next in chain by Button")
            self._parent.showHelpText()


class Panel(Handler):
    def showHelpText(self):
        if self._helpText is not None:  # Can handle request.
            print("Help :: ", self._helpText)
        elif self._parent is not None:
            print("Message passed to next in chain by Panel")
            self._parent.showHelpText()


p = Panel()
p.setHelperText("Panel help text.")
b1 = Button("Ok", p)
b1.setHelperText("Ok button help text.")
b2 = Button("Cancel", p)


b1.showHelpText()
b2.showHelpText()