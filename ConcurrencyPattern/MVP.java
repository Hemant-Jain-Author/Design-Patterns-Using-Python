# Model
class Model:
    def __init__(self):
        self.data = None
        self.presenter = None

    def set_data(self, data):
        print("Model: Set data.")
        self.data = data
        self.presenter.model_update_event()

    def get_data(self):
        print("Model: Get data.")
        return self.data


# Presenter
class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_user_input(self, user_input):
        print("Presenter: Handle user input.")
        self.model.set_data(user_input)

    def model_update_event(self):
        print("Presenter: Model update event.")
        self.view.update(self.model.get_data())


# View
class View:
    def __init__(self):
        self.presenter = None

    def update(self, data):
        print("View: Update UI.")
        print("Data:", data)

    def get_user_input(self):
        user_input = input("View: Enter user input: ")
        self.presenter.handle_user_input(user_input)

# Client code
model = Model()
view = View()
presenter = Presenter(model, view)
model.presenter = presenter
view.presenter = presenter
view.get_user_input()


"""
View : Enter user input: Hello, world!
Presenter : Handle user input.
Model : Set data.
Presenter : Model update event.
View : Update UI.
Data: Hello, world!
"""