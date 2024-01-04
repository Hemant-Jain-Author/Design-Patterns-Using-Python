class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Model(object):
    # Dummy model which just have one object.  
    # Model is supposed to interact with database.
    def __init__(self):
        self.st = Student("Harry", 1)

    def set_data(self, name, id):
        print("Model: Set data :", name, id)
        self.st.name = name
        self.st.id = id

    def get_data(self):
        print("Model: Get data.")
        return self.st

class View(object):
    # Dummy view which is print some data to standard output.
    # View is supposed to intaract the UI. 
    def __init__(self, model):
        self.model = model

    # In classic MVC view interact with the model to get data.
    def update(self):
        st = self.model.get_data()
        print("View: Student Info : ", st.name , st.id)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)

    def set_data(self, name, id):
        print("Controller: Receive data from client.")
        self.model.set_data(name, id)

    def update_view(self):
        print("Controller: Receive update view from client.")
        self.view.update()

# Client code
controller = Controller()
controller.update_view()

controller.set_data("jack", 2)
controller.update_view()

"""
Controller: Receive update view from client.
Model: Get data.
View: Student Info :  Harry 1
Controller: Receive data from client.
Model: Set data : jack 2
Controller: Receive update view from client.
Model: Get data.
View: Student Info :  jack 2
"""