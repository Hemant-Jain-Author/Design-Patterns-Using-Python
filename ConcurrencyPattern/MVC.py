# Model
class Model:
    def __init__(self):
        self.data = None
        self.observers = []

    def set_data(self, data):
        print("Model : Set data.")
        self.data = data
        self.notify_observers()

    def get_data(self):
        print("Model : Get data.")
        return self.data

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        print("Model : Notify observers.")
        for observer in self.observers:
            observer.update()


# View
class View:
    def __init__(self, model, controller):
        self.controller = controller
        self.model = model
        self.model.add_observer(self)

    def update(self):
        print("View : Update.")
        data = model.get_data()
        print("Data:", data)

    def get_user_input(self):
        user_input = input("View : Enter user input: ")
        self.controller.handle_user_input(user_input)


# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_user_input(self, user_input):
        print("Controller : Handle user input.")
        self.model.set_data(user_input)


# Client code
model = Model()
controller = Controller(model, None)  # The Controller sets itself as the observer in this case
view = View(model, controller)
controller.view = view
view.get_user_input()

"""
View : Enter user input: hello, world!
Controller : Handle user input.
Model : Set data.
Model : Notify observers.
View : Update.
Model : Get data.
Data: hello, world!
"""