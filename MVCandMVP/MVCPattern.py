class Model(object):
    def __init__(self):
        self.data = 'Hello, World!'

    def set_data(self, data):
        print("Model: Set data :", data)
        self.data = data

    def get_data(self):
        print("Model: Get data: ", self.data)
        return self.data

class View(object):
    # Dummy view which is print some data to standard output.
    # View is supposed to intaract the UI. 
    def __init__(self, model):
        self.model = model

    # In classic MVC view interact with the model to get data.
    def update(self):
        data = self.model.get_data()
        print("View: Updating the view with data : ", data)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)

    def set_data(self, data):
        print("Controller: Receive data from client.")
        self.model.set_data(data)

    def update_view(self):
        print("Controller: Receive update view from client.")
        self.view.update()

# Client code
controller = Controller()
controller.update_view()

controller.set_data("Hello, Students!")
controller.update_view()

"""
Controller: Receive update view from client.
Model: Get data:  Hello, World!
View: Updating the view with data :  Hello, World!
Controller: Receive data from client.
Model: Set data : Hello, Students!
Controller: Receive update view from client.
Model: Get data:  Hello, Students!
View: Updating the view with data :  Hello, Students!
"""
