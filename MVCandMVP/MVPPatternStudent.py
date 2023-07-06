
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
    def update(self, name, id):
        print("View: Student Info :", name , id)

class Presenter(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def set_data(self, name, id):
        print("Presenter: Receive data from client.")
        self.model.set_data(name, id)

    def update_view(self):
        print("Presenter: Receive update from client.")
        data = self.model.get_data()
        self.view.update(data.name, data.id)

# Client code
presenter = Presenter()
presenter.update_view()

presenter.set_data("jack", 2)
presenter.update_view()

"""
Presenter: Receive update from client.
Model: Get data.
View: Student Info : Harry 1
Presenter: Receive data from client.
Model: Set data : jack 2
Presenter: Receive update from client.
Model: Get data.
View: Student Info : jack 2
"""