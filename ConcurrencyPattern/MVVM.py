# Model
class Model:
    def __init__(self):
        self._data = None

    def set_data(self, data):
        print("Model: Set data.")
        self._data = data

    def get_data(self):
        print("Model: Get data.")
        return self._data


# ViewModel
class ViewModel:
    def __init__(self, model):
        self.model = model
        self.data = None
        self.update_data()

    def update_model(self, data):
        print("ViewModel: Update data.")
        self.model.set_data(data)
        self.update_data()

    def update_data(self):
        print("ViewModel: Fetch data.")
        self.data = self.model.get_data()


# View
class View:
    def __init__(self, view_model):
        self.view_model = view_model

    def display_data(self):
        print("Display Data:", self.view_model.data)

    def get_user_input(self):
        #user_input = input("Enter data: ")
        user_input = "Hello, world!"
        self.view_model.update_model(user_input)


# Client code
model = Model()
view_model = ViewModel(model)
view = View(view_model)

# Display initial data
view.display_data()

# Get user input and update data
view.get_user_input()

# Fetch updated data
view_model.update_data()

# Display updated data
view.display_data()


"""
ViewModel: Fetch data.
Model: Get data.
Display Data: None
Enter data: Hello, world!
ViewModel: Update data.
Model: Set data.
ViewModel: Fetch data.
Model: Get data.
Display Data: Hello, world!
"""