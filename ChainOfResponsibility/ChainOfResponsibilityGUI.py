from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, parent=None):
        self._parent = parent
        self._helpText = None

    @abstractmethod
    def show_helper_text(self):
        pass

    def set_helper_text(self, text):
        self._helpText = text



class Container(Handler):
    def show_helper_text(self):
        if self._helpText is not None:  # Can handle request.
            print("Help :: ", self._helpText)
        elif self._parent is not None:
            print("Message passed to next in chain by Container")
            self._parent.show_helper_text()



class Button(Handler):
    def __init__(self, label, parent=None ):
        super(Button, self).__init__(parent)
        self._label = label

    def show_helper_text(self):
        if self._helpText is not None:  # Can handle request.
            print("Help :: ", self._helpText)
        elif self._parent is not None:
            print("Message passed to next in chain by Button")
            self._parent.show_helper_text()


class Panel(Handler):
    def show_helper_text(self):
        if self._helpText is not None:  # Can handle request.
            print("Help :: ", self._helpText)
        elif self._parent is not None:
            print("Message passed to next in chain by Panel")
            self._parent.show_helper_text()


# Client Code
p = Panel()
p.set_helper_text("Panel help text.")
b1 = Button("Ok", p)
b1.set_helper_text("Ok button help text.")
b2 = Button("Cancel", p)
b1.show_helper_text()
b2.show_helper_text()

"""
Help ::  Ok button help text.
Message passed to next in chain by Button
Help ::  Panel help text.
"""
