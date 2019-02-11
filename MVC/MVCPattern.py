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

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def setData(self, data):
        print("Controller: Receive data from client.")
        self.model.setData(data)

    def updateView(self):
        print("Controller: Receive update view from client.")
        data = self.model.getData()
        self.view.update(data)

class Client(object):
    print("Client: Pass trigger to Controller.")
    controller = Controller()
    controller.updateView()

    controller.setData("Hello, Students!")
    controller.updateView()