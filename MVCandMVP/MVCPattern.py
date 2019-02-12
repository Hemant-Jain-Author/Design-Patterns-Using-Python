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
    # Dummy view which is print some data to standard output.
    # View is supposed to intaract the UI. 
    def __init__(self, model):
        self.model = model

    # In classic MVC view interact with the model to get data.
    def update(self):
        data = self.model.getData()
        print("View: Updating the view with data : ", data)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)

    def setData(self, data):
        print("Controller: Receive data from client.")
        self.model.setData(data)

    def updateView(self):
        print("Controller: Receive update view from client.")
        self.view.update()

class Client(object):
    controller = Controller()
    controller.updateView()

    controller.setData("Hello, Students!")
    controller.updateView()