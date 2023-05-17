class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Model(object):
    # Dummy model which just have one object.  
    # Model is supposed to interact with database.
    def __init__(self):
        self.st = Student("Harry", 1)

    def setData(self, name, id):
        print("Model: Set data :", name, id)
        self.st.name = name
        self.st.id = id

    def getData(self):
        print("Model: Get data.")
        return self.st

class View(object):
    # Dummy view which is print some data to standard output.
    # View is supposed to intaract the UI. 
    def __init__(self, model):
        self.model = model

    # In classic MVC view interact with the model to get data.
    def update(self):
        st = self.model.getData()
        print("View: Student Info : ", st.name , st.id)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)

    def setData(self, name, id):
        print("Controller: Receive data from client.")
        self.model.setData(name, id)

    def updateView(self):
        print("Controller: Receive update view from client.")
        self.view.update()

# Client code
controller = Controller()
controller.updateView()

controller.setData("jack", 2)
controller.updateView()

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