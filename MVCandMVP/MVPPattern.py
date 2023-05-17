# Model View Presenter
class Model(object):
    def __init__(self):
        self.data = 'Hello, World!'

    def setData(self, data):
        print("Model: Set data :", data)
        self.data = data

    def getData(self):
        print("Model: Get data: ", self.data)
        return self.data

class View(object):
    def update(self, data):
        print("View: Updating the view with data: ", data)

class Presenter(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def setData(self, data):
        print("Presenter: Receive data from client.")
        self.model.setData(data)

    def updateView(self):
        print("Presenter: Receive update view from client.")
        data = self.model.getData()
        self.view.update(data)

# Client code
print("Client: Pass trigger to Presenter.")
presenter = Presenter()
presenter.updateView()

presenter.setData("Hello, Students!")
presenter.updateView()

"""
Client: Pass trigger to Presenter.
Presenter: Receive update view from client.
Model: Get data:  Hello, World!
View: Updating the view with data:  Hello, World!
Presenter: Receive data from client.
Model: Set data : Hello, Students!
Presenter: Receive update view from client.
Model: Get data:  Hello, Students!
View: Updating the view with data:  Hello, Students!
"""