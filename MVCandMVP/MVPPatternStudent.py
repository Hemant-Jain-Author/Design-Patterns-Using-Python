
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
    def update(self, name, id):
        print("View: Student Info : ", name , id)

class Presenter(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def setData(self, name, id):
        print("Presenter: Receive data from client.")
        self.model.setData(name, id)

    def updateView(self):
        print("Presenter: Receive update from client.")
        data = self.model.getData()
        self.view.update(data.name, data.id)

class Client(object):
    presenter = Presenter()
    presenter.updateView()

    presenter.setData("jack", 2)
    presenter.updateView()